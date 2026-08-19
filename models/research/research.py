from pydantic import BaseModel, Field

class ResearchSource(BaseModel):
    url: str = Field(
        description = "자료의 원문 URL"
    )
    domain: str = Field(
        default = "",
        description = "출처 도메인"
    )
    source_type: str = Field(
        default = "other",
        description = "출처 유형 . 예: government, academic, wiki, other"
    )
    priority: int = Field(
        default = 5,
        description = "출처 우선순위 . 숫자가 낮을수록 우선순위 높음"
    )
    

class ResearchFact(BaseModel):
    fact: str = Field(
        description = "블로그 글 작성에 사용할 수 있는 검증된 핵심 사실"
    )
    context: str = Field(
        description = "해당 사실의 의미나 배경 설명"
    )
    

class ResearchTimelineItem(BaseModel):
    period: str = Field(
        description = "연도, 날짜 또는 시기"
    )
    event: str = Field(
        description = "해당 시기에 발생한 주요 사건"
    )
    
    
class ResearchStatistic(BaseModel):
    label: str = Field(
        description = "수치 또는 통계의 이름"
    )
    value: str = Field(
        description = "수치와 단위를 포함한 값"
    )
    context: str = Field(
        description = "이 수치가 의미하는 내용"
    )


class ResearchData(BaseModel):
    topic: str = Field(
        description = "사용자가 입력한 원래 주제"
    )
    summary: str = Field(
        description = "전체 조사 내용을 요약한 개요"
    )
    key_facts: list[ResearchFact] = Field(
        default_factory = list,
        description = "글의 핵심 근거가 될 사실 목록"
    )
    timeline: list[ResearchTimelineItem] = Field(
        default_factory = list,
        description = "시간 순서로 정리할 수 있는 주요 사건"
    )
    statistics: list[ResearchStatistic] = Field(
        default_factory = list,
        description = "주제와 관련된 의미 있는 수치나 통계"
    )
    sources: list[ResearchSource] = Field(
        default_factory = list,
        description = "조사에 사용된 출처 목록"
    )