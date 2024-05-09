# db1.py
import sqlite3

#전역함수:임시로 메모리에 작업
#con은 연결객체(인스턴스)
# con = sqlite3.connect(":memory:")
# 영구적으로 데이터베이스 파일에 저장
con = sqlite3.connect("c:\\work2\\sample.db")

#실제 구문을 실행할 커서 객체
cur = con.cursor()

#테이블구조(데이터 저장소) : 만약에 테이블이 없으면 생성하라는 명령어 'if not exists'
cur.execute("CREATE TABLE if not exists PhoneBook (Name text, PhonNum text);")

#입력
cur.execute("insert into PhoneBook values ('전우치', '010-222');")
#입력 파라메터 처리
name = "홍길동"
phoneNumber = "010-123"
cur.execute("insert into PhoneBook values (?,?);", (name,phoneNumber))
#한번에 2개를 입력(다중 레코드) : 2차원 배열(Tuple 안의 Tuple)
datalist = (("이순신", "010-222"), ("박문수", "010-567"))
cur.executemany("insert into PhoneBook values (?,?);", datalist)


#검색
cur.execute("select * from PhoneBook;")
# for row in cur:
#     print(row[0], row[1])

# print("---fetchone()---")
# print(cur.fetchone())
# print("---fetchmany()---")
# print(cur.fetchmany(2))
print("---fetchall()---")
cur.execute("select * from PhoneBook;")
print(cur.fetchall())
#작업 정상 완료
con.commit()