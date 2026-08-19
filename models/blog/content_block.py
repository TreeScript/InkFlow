from typing import Literal

from pydantic import BaseModel, Field


class ContentBlock(BaseModel):
    type: Literal[
        "text",
        "heading",
        "image",
        "video",
        "bullet_list",
        "numbered_list",
        "quote",
        "divider",
        "link",
        "place",
    ] = Field(
        description="콘텐츠 블록의 종류"
    )

    content: str = Field(
        default="",
        description="text, heading, quote 블록에서 사용하는 본문 내용"
    )

    level: int = Field(
        default=0,
        description="heading 블록의 제목 레벨. 일반적으로 1 또는 2"
    )

    query: str = Field(
        default="",
        description="image 또는 video 블록에서 사용할 검색 키워드"
    )

    caption: str = Field(
        default="",
        description="image 또는 video 블록의 설명"
    )

    items: list[str] = Field(
        default_factory=list,
        description="bullet_list 또는 numbered_list 블록의 항목"
    )

    title: str = Field(
        default="",
        description="link 블록의 표시 제목"
    )

    url: str = Field(
        default="",
        description="link 블록의 실제 URL"
    )

    name: str = Field(
        default="",
        description="place 블록의 장소명"
    )

    address: str = Field(
        default="",
        description="place 블록의 주소"
    )

    description: str = Field(
        default="",
        description="place 블록의 장소 설명"
    )