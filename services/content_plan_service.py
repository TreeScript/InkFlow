from openai import OpenAI

from config.settings import OPENAI_MODEL
from models.content_plan import ContentPlan
from models.research import ResearchData
from prompts.content_plan_prompt import build_content_plan_prompt

def create_content_plan(client: OpenAI, topic: str, research_data: ResearchData) -> ContentPlan:
    prompt = build_content_plan_prompt(
        topic = topic,
        research_data = research_data
    )
    
    response = client.responses.parse(
        model = OPENAI_MODEL,
        input = prompt,
        text_format = ContentPlan
    )
    
    content_plan = response.output_parsed
    if content_plan is None:
        raise RuntimeError(
            "ContentPlan 생성에 실패했습니다."
        )
        
    return content_plan