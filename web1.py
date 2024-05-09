# web1.py
# 웹크롤링을 위한 선언
from bs4 import BeautifulSoup

#페이지를 로딩:메소드체인, 열고 읽는걸 바로(open과 .read)
page = open("Chap09_test.html", "rt", encoding="utf-8").read()

#검색이 용이한 스프객체 생성(html, xml)
soup = BeautifulSoup(page, "html.parser")
# print(soup.prettify())
# <p>태그 전체 검색
# print(soup.find_all("p"))
# <p>태그 한개 검색
# print(soup.find("p"))
#필터링 : <p class='outer-text'>
#파이썬 class 키워드를 사용할 수 없기 때문에 class_ 사용
# print(soup.find_all("p",class_="outer-text"))
#attrs는 속성을 지정(attributes)
# print(soup.find_all("p",attrs={"class":"outer-text"}))
#<p id='first'> 찾기
# print(soup.find_all("p",id="first"))

#내부에 컨텐츠를 추출: .text 속성
for tag in soup.find_all("p"):
    title = tag.text.strip() #strip은 앞뒤 공백과 문자 제거. 즉 태그와 공백 제거
    title = title.replace("\n","")
    print(title)