import re

def check_email(email):
    # 이메일 주소를 검증하는 정규 표현식
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, email):
        return True
    else:
        return False

# 테스트를 위한 이메일 주소 샘플
email_samples = [
    "example1@gmail.com",
    "example2@yahoo.com",
    "example3@hotmail.com",
    "example4@naver.com",
    "example5@daum.net",
    "example6@nate.com",
    "example7@outlook.com",
    "example8@icloud.com",
    "example9@aol.com",
    "example10@zoho.com"
]

# 각 이메일 주소가 유효한지 검사
for email in email_samples:
    print(f"{email} is valid: {check_email(email)}")
