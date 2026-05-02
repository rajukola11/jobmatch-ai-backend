import json
import re
from services.openai_client import client
from core.config import OPENAI_MODEL


def analyze_job_logic(job_description: str):
    prompt = f"""
    Analyze job and return JSON only.

    {{
      "score": number,
      "decision": "APPLY" or "SKIP",
      "reason": "short"
    }}

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