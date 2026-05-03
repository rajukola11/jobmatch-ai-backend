from services.openai_client import client
from core.config import OPENAI_MODEL


def generate_message_logic(job_description: str, company: str):
    prompt = f"""
You are writing a LinkedIn outreach message to a recruiter or employee.

STRICT RULES:
- Max 3–4 lines
- Friendly, confident, NOT desperate
- No buzzwords, no fluff
- Show relevance (Python, FastAPI, React if applicable)
- Mention interest in the specific role/company
- End with a soft call-to-action (not begging)

STYLE:
- Natural, human tone
- Short sentences
- Suitable for Germany / EU hiring culture

OUTPUT:
Only the message. No explanations.

JOB DESCRIPTION:
{job_description}

COMPANY:
{company}
"""

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content.strip()