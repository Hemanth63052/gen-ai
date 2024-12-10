from fastapi import FastAPI
from scripts.core.services.genai_services import gen_ai_router

app = FastAPI()

app.include_router(router=gen_ai_router, prefix="/genai")