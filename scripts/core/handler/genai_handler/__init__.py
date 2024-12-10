from fastapi import UploadFile

from scripts.utils.langchain_util import FAISSUtil
from scripts.utils.common_util import CommonHandler
from scripts.utils.openai_util import OpenAIUtil

class GenAIHandler:
    def __init__(self):
        self.common_handler = CommonHandler()
        self.openai_util = OpenAIUtil()
        self.faiss_util = FAISSUtil(embedding_dim=768)

    async def upload_template_to_lite_llm(self, file:UploadFile):
        if file.filename.split(".")[-1].lower() in ['pdf']:
            pdf_path = f"temp_{file.filename}.txt"
            with open(pdf_path, "wb") as buffer:
                buffer.write(await file.read())
            extracted_text = self.common_handler.extract_text_from_pdf(pdf_path)
            chunks = self.common_handler.split_text(extracted_text)
            for _, chunk in enumerate(chunks):
                embedding = self.openai_util.generate_embeddings(chunk)
                self.faiss_util.store_embedding(f"chunk_{_}", chunk, embedding)
        else:
            return {"status":"failed", "message":"Failed to process please check uploaded file"}
        return {"status":"success", "message":"PDF uploaded successfully"}

    async def search_by_question(self, question: str):
        question_embedding = self.openai_util.generate_embeddings(question)
        results = self.faiss_util.search_similar_chunks(question_embedding, k=5)
        return {"status": "success", "results": results}


            




