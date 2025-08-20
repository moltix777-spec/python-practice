name = input("이름이 뭐에요?")
food = input("좋아하는 음식 뭐에요?")
print(f"{name}는 {food}를 좋아합니다.")

name = "민수"
food = "김치찌개"
hobby = "게임"

# 한 줄에 ,로 구분된 소개문
print(f"이름: {name}", f"음식: {food}", f"취미: {hobby}", sep=", ")

# 줄바꿈 없이 순차 출력
print(f"안녕하세요 {name}입니다.", end=" ")
print(f"저는 {food}를 좋아하고, {hobby}를 즐겨합니다.")

colors = ["red","blue","green"]
colors[1]= "yellow"
print(colors)

sentence = "I love Python programing"
li = sentence.split()
print("-".join(li))

a = 7
b =3
print(f"{a} 나누기 {b} = {a/b:.2f}")

word = "hello world"
print(word.upper())

num_list = [1,2,3,4,5]
print(f"합계: {sum(num_list)}")

text = "apple,banana,grape"
li = text.split(",")
print("/".join(li))

animals = ["dog","cat","tiger"]
animals[2]= "lion"
print(animals)

x = 3.141592
print(f"{x:.3f}")

num =10
if num > 5:
    print("크다")

age = int(input("나이를 입력하시오"))
if age >= 18:
    print("성인")

else:
    age < 18 # ->어차피 참이 아니면 무조건 거짓이니까 조건빼
    print("미성년자")

pw = int(input("4자리 숫자를 입력하시오"))# ->int 빼 어차피 문자열로 받으니까
if pw =="1234":
    print("로그인 성공")
else:
    print("꺼져")