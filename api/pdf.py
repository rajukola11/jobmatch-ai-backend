from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from models.pdf import PDFRequest
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
import io

router = APIRouter()

def build_single_pdf(title: str, content: str) -> io.BytesIO:
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4,
                            rightMargin=2*cm, leftMargin=2*cm,
                            topMargin=2*cm, bottomMargin=2*cm)

    heading = ParagraphStyle('h', fontSize=14, spaceAfter=12, fontName='Helvetica-Bold')
    body = ParagraphStyle('b', fontSize=10, spaceAfter=5, leading=14)

    elements = [Paragraph(title, heading), Spacer(1, 0.4*cm)]
    for line in content.split('\n'):
        elements.append(Paragraph(line.strip() or "&nbsp;", body))

    doc.build(elements)
    buffer.seek(0)
    return buffer


@router.post("/generate-cv-pdf")
async def generate_cv_pdf(data: PDFRequest):
    pdf = build_single_pdf(
        title=f"Tailored CV — {data.job_title} @ {data.company}",
        content=data.tailored_cv
    )
    filename = f"{data.company}_{data.job_title}_CV.pdf".replace(" ", "_")
    return StreamingResponse(pdf, media_type="application/pdf",
                             headers={"Content-Disposition": f"attachment; filename={filename}"})


@router.post("/generate-cl-pdf")
async def generate_cover_letter_pdf(data: PDFRequest):
    pdf = build_single_pdf(
        title=f"Cover Letter — {data.job_title} @ {data.company}",
        content=data.cover_letter
    )
    filename = f"{data.company}_{data.job_title}_Cover_Letter.pdf".replace(" ", "_")
    return StreamingResponse(pdf, media_type="application/pdf",
                             headers={"Content-Disposition": f"attachment; filename={filename}"})


@router.post("/generate-msg-pdf")
async def generate_message_pdf(data: PDFRequest):
    pdf = build_single_pdf(
        title=f"Message — {data.job_title} @ {data.company}",
        content=data.message
    )
    filename = f"{data.company}_{data.job_title}_Message.pdf".replace(" ", "_")
    return StreamingResponse(pdf, media_type="application/pdf",
                             headers={"Content-Disposition": f"attachment; filename={filename}"})