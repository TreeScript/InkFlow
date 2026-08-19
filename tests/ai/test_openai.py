import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)

response = client.responses.create(
    model = "gpt-5-mini",
    input = "InkFlow OpenAI API 연결 테스트입니다. '연결 성공'이라고만 답해주세요."
)

print(response.output_text)