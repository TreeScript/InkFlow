# 환경설정
import os

from dotenv import load_dotenv

load_dotenv()

def get_openai_api_key() -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY가 설정되어 있지 않습니다.")
    
    return api_key


OPENAI_MODEL = "gpt-5-mini"