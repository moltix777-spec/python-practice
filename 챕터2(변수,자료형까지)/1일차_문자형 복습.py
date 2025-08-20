# 1번 문제 답
text = "20250808Rainy"
연도 = text[:4]
월 = text[4:6]
일 = text[6:8]
날씨 = text[8:]

print("연도 :" + 연도)
print("월 :",월)
print("일 :",일)
print("날씨 :",날씨)

# 2번 문제 답
word = "Pithon"

print(word[:1]+ "y" + word[2:])

# 3번문제
name = "민수"
age = 27

print(f"안녕하세요. 제 이름은 {name}이고, 내년엔 {age + 1}살이 됩니다.")

# 문제1.주민등록번호 분리

number = (input("주민등록번호를 입력해주세요."))

생년월일 = number[:6]
성별코드 = number[7:8]
뒷자리 = number[8:]

print("생년월일: ",생년월일)
print("성별코드: ",성별코드)
print("뒷자리: ",뒷자리)

a = "Python"

print(a[::-1])

year=2025
month=8
day=8
weather="Sunny"

print(f"오늘은 {year}년 {month}월 {day}일, 날씨는 {weather}입니다.")