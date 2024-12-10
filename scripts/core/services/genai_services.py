from scripts.core.handler.genai_handler import GenAIHandler
from scripts.core.services import gen_ai_router
from fastapi import UploadFile, File
import logging as logger


@gen_ai_router.post("/upload_pdf")
async def upload_pdf(template_data: UploadFile = File(...)):
    try:
        logger.info("Uploading the pdf file")
        upload_pdf = GenAIHandler()
        return await upload_pdf.upload_template_to_lite_llm(file=template_data)
    except Exception as e:
        print(e)
        return {}
