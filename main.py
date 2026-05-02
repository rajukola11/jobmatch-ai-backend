from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv
import json
import re

load_dotenv()

app = FastAPI()

api_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

class CVRequest(BaseModel):
    job_description: str
    base_cv: str

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set")

client = OpenAI(api_key=api_key)


class JobRequest(BaseModel):
    job_description: str


@app.post("/analyze-job")
async def analyze_job(data: JobRequest):

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
    {data.job_description}
    """

    response = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
    )

    raw_output = response.choices[0].message.content

    # Clean markdown if model still adds it
    cleaned = re.sub(r"```json|```", "", raw_output).strip()

    try:
        parsed = json.loads(cleaned)
    except:
        parsed = {
            "score": 0,
            "decision": "SKIP",
            "reason": "Parsing failed"
        }

    return parsed

@app.post("/generate-cv")
async def generate_cv(data: CVRequest):

    prompt = f"""
    Rewrite the CV to match the job.

    Focus:
    - Highlight relevant skills
    - Make it short and clear
    - No lies

    Job:
    {data.job_description}

    CV:
    {data.base_cv}
    """

    response = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
    )

    return {
        "tailored_cv": response.choices[0].message.content
    }