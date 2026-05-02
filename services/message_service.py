from services.openai_client import client
from core.config import OPENAI_MODEL


def generate_message_logic(job_description: str, company: str):
    prompt = f"""
    Write short LinkedIn message (3-4 lines).

    Job:
    {job_description}

    Company:
    {company}
    """

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content