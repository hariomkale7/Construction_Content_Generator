🏗️ AI-Powered Construction Content Generator

An AI-powered web application that automatically generates construction site reports, safety reports, and daily log summaries using Google Gemini AI.
The system allows users to input project details and instantly generate professional construction documentation that can also be exported as a PDF file.

🚀 Project Overview

The AI-Powered Construction Content Generator is designed to simplify the process of creating structured construction reports. Instead of manually writing reports, users can enter project details and the system generates professional documentation using AI.

The application uses a FastAPI backend, integrates Google Gemini AI for content generation, and provides a simple web interface for user interaction.

✨ Features

Generate Construction Site Reports

Generate Safety Reports

Generate Daily Log Summaries

AI-powered report generation using Gemini API

Simple and user-friendly web interface

Real-time content generation

PDF export and download

Fast backend powered by FastAPI

🛠️ Tech Stack
Backend

Python

FastAPI

Google Gemini AI API

ReportLab (PDF Generation)

Pydantic

Python-dotenv

Frontend

HTML5

CSS3

JavaScript

Concepts & Tools

REST APIs

JSON APIs

Async Programming

Git & GitHub

🏗️ Project Architecture
User Interface (HTML + JavaScript)
            │
            ▼
       REST API Request
            │
            ▼
       FastAPI Backend
            │
            ▼
      Google Gemini AI
            │
            ▼
     Generated Report
            │
            ▼
       PDF Generation
📂 Project Structure
construction-content-generator
│
├── backend
│   ├── main.py
│   ├── requirements.txt
│   └── .env
│
├── frontend
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── README.md
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/yourusername/construction-content-generator.git
cd construction-content-generator
2️⃣ Create Virtual Environment
python -m venv venv

Activate it:

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Create Environment Variables

Create a .env file and add your Gemini API key.

GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.0-flash
5️⃣ Run the Backend Server
uvicorn main:app --reload

Server will run at:

http://127.0.0.1:8000
6️⃣ Open the Frontend

Open index.html in your browser to use the application.

📡 API Endpoint
Generate Report
POST /generate-report

Example Request:

{
  "content_type": "site_report",
  "project_name": "Skyline Tower",
  "location": "Mumbai",
  "report_date": "2026-02-22",
  "topic": "Foundation excavation completed"
}
📄 Output

The system generates:

AI Generated Construction Report

Downloadable PDF file

🎯 Use Cases

Construction site documentation

Daily progress tracking

Safety reporting

Automated construction reporting

🔮 Future Improvements

AI chatbot for construction queries

Cost estimation system

Material planning assistant

Cloud deployment

User authentication

👨‍💻 Author

Hariom Kale
B.Tech Computer Science Engineering

Skills:

Python

FastAPI

AI API Integration

Backend Development

⭐ If you find this project useful, consider giving it a star on GitHub.
