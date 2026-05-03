from services.openai_client import client
from core.config import OPENAI_MODEL


def generate_cover_letter_logic(job_description: str, company: str, base_cv: str):
    prompt = f"""
You are writing a professional EU-style cover letter for a junior software engineer role.

STRICT RULES:
- Max 300–400 words
- Clear structure:
  1. Short introduction (who you are + role)
  2. Skills match (Python, FastAPI, React, APIs, etc.)
  3. Motivation (why this company)
  4. Closing (confident, not desperate)
- No generic phrases like "I am passionate"
- No fake experience
- Tailor content to the job description
- Keep tone professional but human
- Suitable for Germany / EU hiring culture

OUTPUT FORMAT:
- Paragraph style (no bullet points)

JOB DESCRIPTION:
{job_description}

COMPANY:
{company}

BASE CV:
{base_cv}
"""

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content.strip()