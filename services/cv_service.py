from services.openai_client import client
from core.config import OPENAI_MODEL

def generate_cv_logic(job_description: str, cv_text: str):
    if not job_description or not job_description.strip():
        raise ValueError("job_description is required and cannot be empty.")
    if not cv_text or not cv_text.strip():
        raise ValueError("cv_text is required and cannot be empty.")
    prompt = f"""
You are an expert CV writer for software engineering roles in Europe.

Rewrite the CV to match the job description.

STRICT RULES:
- Keep it concise and professional
- Focus on relevant skills (Python, FastAPI, React, APIs, PostgreSQL)
- Optimize for ATS (use keywords from job description)
- Emphasize junior-level suitability (0-2 years)
- Do NOT add fake experience
- Use clear bullet points

OUTPUT FORMAT:
- Title
- Summary
- Skills
- Experience (bullet points)
- Projects

JOB DESCRIPTION:
{job_description}

BASE CV:
{cv_text}
"""

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content.strip()