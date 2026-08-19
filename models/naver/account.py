from pydantic import BaseModel, Field

class NaverAccount(BaseModel):
    login_id: str = Field(
        min_length = 1,
        description = "네이버 로그인 아이디"
    )
    
    password: str = Field(
        min_length = 1,
        description = "네이버 로그인 비밀번호"
    )