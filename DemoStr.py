#정규표현식
import re

result = re.search("[0-9]*th", "35th")
print(result)
print(result.group())

#연도
result = re.search("\d{4}","올해는 2024년입니다.")
print(result.group())

#우편번호
result = re.search("\d{5}","우리 동네는 52111")
print(result.group())

#단어
result = re.search("apple","this is apple")
print(result.group())