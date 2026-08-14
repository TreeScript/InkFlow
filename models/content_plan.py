from pydantic import BaseModel, Field


class ContentPlanSection(BaseModel):
    heading: str = Field(
        description = "본문에서 사용할 소제목"
    )
    purpose: str = Field(
        description = "이 섹션에서 독자에게 전달해야 할 핵심 목적"
    )
    
    key_points: list[str] = Field(
        default_factory = list,
        description = "이 섹션에서 반드시 다룰 핵심 내용"
    )
    
    
class ContentPlan(BaseModel):
    content_type: str = Field(
        description = "게시글 유형"
    )
    tone: str = Field(
        description = "게시글에 적합한 문체와 분위기"
    )
    target_reader: str = Field(
        description = "이 글을 읽을 것으로 예상되는 독자"
    )
    title_direction: str = Field(
        description = "제목을 어떤 방향으로 작성해야 하는지"
    )
    intro_direction: str = Field(
        description = "도입부 구성 방향"
    )
    sections: list[ContentPlanSection] = Field(
        description = "본문에서 다룰 섹션 구성"
    )
    conclusion_direction: str = Field(
        description = "마무리 구성 방향"
    )
    recommend_image_count: int = Field(
        description = "글의 내용과 길이에 적절한 이미지 수"
    )
    depth: str = Field(
        description = "글의 정보 깊이. light, standard, deep 중 하나"
    )