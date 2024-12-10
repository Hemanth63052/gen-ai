from scripts.config import OpenAIConf
from scripts.constants import OpenAIConstants
import openai

class OpenAIUtil:
    def __init__(self):
        openai.api_key = OpenAIConf.OPENAI_API_KEY

    def generate_embeddings(self, text):
        response = openai.Embedding.create(
            input=text,
            model=OpenAIConstants.embedding_model_mapping['text_embedding']
        )
        return response["data"][0]["embedding"]
