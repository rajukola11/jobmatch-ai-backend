import json
import re
from services.openai_client import client
from core.config import OPENAI_MODEL


def analyze_job_logic(job_description: str):
    prompt = f"""
    Analyze the job description and respond ONLY in valid JSON.
    Respond ONLY with raw JSON.
    Do NOT use markdown.
    Do NOT use ```.

    Format:
    {{
    "score": number (0-100),
    "decision": "APPLY" or "SKIP",
    "reason": "short reason"
    }}

    Rules:
    - Consider React, JavaScript, FastAPI relevance
    - Prefer junior roles (0-2 years)
    - Prefer English-friendly roles
    - Be strict (don't give high scores easily)

    Job:
    {job_description}
    """

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = response.choices[0].message.content
    cleaned = re.sub(r"```json|```", "", raw).strip()

    try:
        return json.loads(cleaned)
    except:
        return {
            "score": 0,
            "decision": "SKIP",
            "reason": "Parsing failed"
        }