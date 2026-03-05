import google.generativeai as genai

# STEP 1: Configure API key
genai.configure(api_key="AIzaSyC_-ke1h_nQQEaC-J5SHgz_UQS1fCDu8qI")

# STEP 2: Load model
model = genai.GenerativeModel("gemini-2.5-flash")

# STEP 3: Simple test prompt
prompt = """
You are a senior construction site engineer.
Write a short professional site report for foundation concreting work.
"""

# STEP 4: Generate content
response = model.generate_content(prompt)

print(response.text)





