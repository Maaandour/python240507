# DemoFile.py

# 파일쓰기
f = open("demo.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

# 파일읽기
f = open("demo.txt", "rt", encoding="utf-8")
result = f.read()
print(result)
print("---readline()메소드---")
f.seek(0)
print(f.readline())
print(f.readline())
print("---readlines()메소드---")
f.seek(0)
print(f.readlines())

f.close()