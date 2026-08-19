from services.naver import input_naver_account


def test_naver_account_input() -> None:
    account = input_naver_account()
    
    print()
    print("네이버 로그인 정보 입력 완료")
    print(f"아이디: {account.login_id}")
    print(
        f"비밀번호 입력 여부: "
        f"{bool(account.password)}"
    )
    
if __name__ == "__main__":
    test_naver_account_input()