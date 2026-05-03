from services.openai_client import client
from core.config import OPENAI_MODEL


def generate_message_logic(job_description: str, company: str, recipient_name: str = "", base_cv: str = ""):
    if recipient_name and recipient_name.strip():
        greeting_rule = f'- Start with "Hi {recipient_name.strip()}," as the greeting'
    else:
        greeting_rule = f'- Start with "Hi {company} Hiring Team," as the greeting'

    signoff_rule = (
        "- Sign off with 'Best regards,' followed by the candidate's real name extracted from the BASE CV below"
        if base_cv.strip()
        else "- Sign off with 'Best regards,' followed by the candidate's name"
    )

    prompt = (
        f"You are writing a LinkedIn outreach message to a recruiter or employee at {company}.\n\n"
        "STRICT RULES:\n"
        f"{greeting_rule}\n"
        "- Max 3-4 lines\n"
        "- Friendly, confident, NOT desperate\n"
        "- No buzzwords, no fluff\n"
        "- Show relevance (Python, FastAPI, React if applicable)\n"
        f'- Use the company name "{company}" directly — do NOT use placeholders like [Company] or template variables\n'
        f"{signoff_rule}\n"
        "- Do NOT use placeholders like [Your Name] — use the actual name from the CV\n"
        "- End with a soft call-to-action (not begging)\n\n"
        "STYLE:\n"
        "- Natural, human tone\n"
        "- Short sentences\n"
        "- Suitable for Germany / EU hiring culture\n\n"
        "OUTPUT:\n"
        "Only the final message text. No explanations. No placeholders. No template variables.\n\n"
        f"JOB DESCRIPTION:\n{job_description}\n\n"
        f"COMPANY:\n{company}\n"
        + (f"\nBASE CV:\n{base_cv}\n" if base_cv.strip() else "")
    )

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content.strip()