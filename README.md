# 🚀 JobMatch AI Backend

Production-ready FastAPI backend for AI-driven job intelligence.
Analyzes job descriptions using LLMs to generate structured insights including fit score, apply/skip decision, and reasoning.

Designed for real-world usage, automation workflows (n8n), and scalable job matching systems.

---

## 📌 Features

* 🔍 AI-powered job analysis using OpenAI models
* 📊 Fit scoring (0–100) based on tech stack relevance
* ✅ Decision engine: APPLY or SKIP
* 🧠 Concise reasoning generation
* ⚙️ Environment-based configuration (`.env`)
* 🔗 Easy integration with tools like n8n
* 🚀 FastAPI-based high-performance backend

---

## 🏗️ Tech Stack

* Backend: FastAPI
* AI: OpenAI API (GPT models)
* Validation: Pydantic
* Config: python-dotenv
* Automation: n8n (optional integration)

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/jobmatch-ai-backend.git
cd jobmatch-ai-backend
```

---

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create `.env` file

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4.1-mini
```

---

### 5. Run the server

```bash
uvicorn main:app --reload
```

---

### 6. Open API docs

```text
http://127.0.0.1:8000/docs
```

---

## 📡 API Usage

### Endpoint

```http
POST /analyze-job
```

### Request Body

```json
{
  "job_description": "Python + React developer with 2 years experience..."
}
```

### Response

```json
{
  "score": 88,
  "decision": "APPLY",
  "reason": "Strong match for Python and React with relevant experience"
}
```

---

## 🔗 n8n Integration

Use HTTP Request node:

* Method: `POST`
* URL: `https://your-api-url/analyze-job`
* Body: JSON

This allows full automation:

```text
Job Source → n8n → FastAPI → AI Analysis → Store/Notify
```

---

## 🧠 How It Works

1. Job description is received via API
2. Prompt is constructed dynamically
3. LLM analyzes based on:

   * Tech stack relevance
   * Experience level
   * Language requirements
4. Structured response is returned

---

## ⚠️ Current Limitations

* No authentication (yet)
* No rate limiting
* No database storage
* Depends on external LLM response quality

---

## 🚀 Roadmap

* [ ] Structured JSON validation with strict schema
* [ ] User authentication (JWT)
* [ ] Job history storage (PostgreSQL)
* [ ] Dashboard UI (React)
* [ ] Resume vs Job matching
* [ ] Multi-model support

---

## 💣 Why This Project Matters

Most job applications are blind and inefficient.
This system turns job hunting into a data-driven process by:

* Filtering irrelevant jobs
* Prioritizing high-fit opportunities
* Saving time and effort

---

## 👨‍💻 Author

Raju Kola

---

## 📄 License

MIT License
