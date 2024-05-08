# Person2.py 
#1)클래스 형식 정의
class Person:
    #클래스 멤버 변수
    num_person = 0 
    def __init__(self):
        self.name = "default name"
        Person.num_person += 1 
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스 생성
p1 = Person()
p2 = Person()

#3)메소트 호출
print("숫자:{0}".format(Person.num_person))
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)


