import uvicorn

from app import app as main_app
from scripts.config import BEServiceConf

if __name__ == "__main__":
    uvicorn.run(main_app, host=BEServiceConf.BE_HOST, port=BEServiceConf.BE_PORT,
                reload=False)
