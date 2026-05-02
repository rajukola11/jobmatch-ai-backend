from services.openai_client import client
from core.config import OPENAI_MODEL


def generate_cv_logic(job_description: str, base_cv: str):
    prompt = f"""
    Rewrite CV based on job.

    Job:
    {job_description}

    CV:
    {base_cv}
    """

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content