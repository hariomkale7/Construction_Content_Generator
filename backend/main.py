from dotenv import load_dotenv
load_dotenv()

import os
import tempfile
import logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from google import genai
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4

# ==============================
# 1️⃣ Logging Setup
# ==============================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# ==============================
# 2️⃣ FastAPI App
# ==============================
app = FastAPI(title="Construction Content Generator API")

# ==============================
# 3️⃣ CORS Configuration
# ==============================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==============================
# 4️⃣ Request Models
# ==============================

class ContentRequest(BaseModel):
    content_type: str
    project_name: str | None = None
    location: str | None = None
    report_date: str | None = None
    topic: str


class PDFRequest(BaseModel):
    text: str


# ==============================
# 5️⃣ Gemini Setup
# ==============================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL","gemini-3-flash-preview")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY missing in .env file")

client = genai.Client(api_key=GEMINI_API_KEY)


# ==============================
# 6️⃣ Prompt Builder
# ==============================

def build_prompt(request: ContentRequest) -> str:

    content_map = {
        "site_report": "Generate a professional Construction Site Report.",
        "safety_report": "Generate a Construction Safety Inspection Report.",
        "daily_log": "Generate a Daily Construction Activity Log."
    }

    base_instruction = content_map.get(request.content_type)

    if not base_instruction:
        raise HTTPException(status_code=400, detail="Invalid content type")

    prompt = f"""
You are a licensed senior construction engineer.

{base_instruction}

STRICT RULES:
- Use ONLY the provided information.
- If any data is missing, write "Not Provided".
- Do NOT invent details.
- Maintain professional technical tone.
- No markdown formatting.

Project Name: {request.project_name or "Not Provided"}
Location: {request.location or "Not Provided"}
Date: {request.report_date or "Not Provided"}
Details: {request.topic}
"""

    return prompt


# ==============================
# 7️⃣ Generate AI Text Endpoint
# ==============================

@app.post("/generate-text")
async def generate_text(request: ContentRequest):

    try:
        logger.info("Generating AI content")

        prompt = build_prompt(request)

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        if not response.text:
            raise HTTPException(status_code=500, detail="Empty AI response")

        return {"generated_text": response.text.strip()}

    except Exception as e:
        logger.error(f"AI generation failed: {str(e)}")
        raise HTTPException(status_code=500, detail="AI content generation failed")


# ==============================
# 8️⃣ Generate PDF Endpoint
# ==============================

@app.post("/generate-pdf")
async def generate_pdf(request: PDFRequest):

    try:
        logger.info("Generating PDF")

        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
        file_path = temp_file.name

        doc = SimpleDocTemplate(file_path, pagesize=A4)
        elements = []

        styles = getSampleStyleSheet()
        normal_style = styles["Normal"]

        for line in request.text.split("\n"):
            elements.append(Paragraph(line, normal_style))
            elements.append(Spacer(1, 0.2 * inch))

        doc.build(elements)

        return FileResponse(
            path=file_path,
            filename="Construction_Content.pdf",
            media_type="application/pdf"
        )

    except Exception as e:
        logger.error(f"PDF generation failed: {str(e)}")
        raise HTTPException(status_code=500, detail="PDF generation failed")