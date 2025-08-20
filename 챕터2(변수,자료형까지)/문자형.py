food = "\"python's favorite food is perl\""
print(food)

mutiline = """Life is too short 
You need pythin"""
# print(mutiline)

a = "Hello to"
b = " my little friend"
print(a + b)
print(a*2)

print("-" * 30)
print("안녕하세요 사용자님")
print("-" * 30)

a = "안녕하세요 만나서 반갑습니다"
print(len(a))  #-- 문자열 길이구하기

a = "Life is too short, You need Python"
# print(len(a))
print(a[:27])

a = "20250808FridaySunny"
date = a[:8]
day = a[8:14]
weather = a[14:]

print(date,day,weather)

a = "Pithon"

print(a[:1]+"y"+a[2:])

number = 77
print("Error is %d%%." % number)

# print("%-10sjane" % "hi")
print("%7.4f" % 3.1415926545)

print("나는 {0}를 {number}개 먹었데이.".format("사과",number=10))
print("나는 {0}를 {1}개 먹었데이.".format("사과",10))

print("{:^10}".format("hi"))
print("{0:-^10}".format("hi"))
print("{0:@>20}".format("hi"))

name = "홍길동"
age = 42
print(f"""나의 이름은 {name}입니다.
나이는 {age}입니다.""")

print(f"난 {100000000:,}원을 가지고 있어")

ㅁ = "안녕하세요"
print(ㅁ.count('녕'))

a = "Python is the best choice"
print(a.find('b'))
print(a.find('t'))

# .index는 넘어가 find랑 효과는 같은데 없으면 오류가남
# .join은 앞에 리스트와 튜플에 곧 배우니깐 눈으로 넘어감

a = "hi"
print(a.upper())

a.lower() #은 대문자를 소문자로 

a = "       hi      "
print(a.lstrip())

a = "       hi      "
print(a.rstrip())

a = "       hi      "
print(a.strip())

a = "Life is too short"
print(a.replace("short","FUCK!!"))

# split 2-3에서 자세히 알아볼 예정

a = "Python"
print(a.isalpha())
a = "Python100"
print(a.isalpha())
a = "Python"
print(a.isdigit())
a = "12344324"
print(a.isdigit())

a = "Life is too short"
print(a.startswith("Life"))
print(a.startswith("short"))
print(a.endswith("Life"))
print(a.endswith("short"))
