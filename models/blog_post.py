from pydantic import BaseModel, Field

from models.content_block import ContentBlock


class BlogPost(BaseModel):
    title: str = Field(
        description="네이버 블로그 게시글 제목"
    )

    content_type: str = Field(
        description="게시글 유형. 예: 시사, 맛집, 여행, 생활정보, IT"
    )

    tone: str = Field(
        description="게시글의 전체적인 문체와 분위기"
    )

    blocks: list[ContentBlock] = Field(
        description="네이버 블로그에 표시될 순서대로 구성된 콘텐츠 블록"
    )

    tags: list[str] = Field(
        description="게시글 내용과 직접적으로 관련된 태그"
    )