from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv

load_dotenv()

class __StreamlitServiceConf(BaseSettings):
    UI_HOST: str = Field(default="0.0.0.0")
    UI_PORT: int= Field(default=9502)

class __BEServiceConf(BaseSettings):
    BE_HOST: str = Field(default='0.0.0.0')
    BE_PORT: int = Field(default=9503)

class __OpenAiConf(BaseSettings):
    OPENAI_API_KEY:str = Field(default="")


StreamlitServiceConf = __StreamlitServiceConf()
BEServiceConf = __BEServiceConf()
OpenAIConf = __OpenAiConf()

__all__ = ['StreamlitServiceConf', 'BEServiceConf', OpenAIConf]
