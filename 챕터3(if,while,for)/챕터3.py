# num =10
# if num > 5:
#     print("크다")

# age = int(input("나이를 입력하시오"))
# if age >= 18:
#     print("성인")

# else:
#     age < 18 ->어차피 참이 아니면 무조건 거짓이니까 조건빼
#     print("미성년자")

# pw = (input("4자리 숫자를 입력하시오"))
# if pw =="1234":
#     print("로그인 성공")
# else:
#     print("꺼져")
# int(intput()) 하면 pw == 1234로 하고 통일시키야댄다

# score = int(input("점수를 입력하시오"))
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# else:
#     print("F")    

# num = int(input("숫자 입력"))
# if num > 0:
#     print("양수")
# elif num == 0:
#     print("0")
# else:
#     print("음수")

# hour = int(input("현재 시각은?"))
# if 6 <= hour <= 11:
#     print("아침")
# elif 12 <= hour <=17:
#     print("점심")
# elif 18 <= hour <=21:
#     print("저녁")
# else:
#     print("밤")

# n = int(input("숫자를 입력하시오"))
# if n % 15==0:
#     print("FizzBuzz")
# elif n%5==0:
#     print("Buzz")
# elif n%3==0:
#     print("Fizz")
# else:
#     print(n)

# weight = float(input("몇 kg 입니까: "))
# height = float(input("몇 cm입니까?: "))/100
# bmi = weight / (height **2)
# if bmi >= 25:
#     status="돼지"
# elif bmi >= 18.5:
#     status ="정상"
# else:
#     status= "멸치" 
# print(f"당신의 bmI는 {bmi:.1f} -> {status}")

# socre = int(input("점수를 입력해주세요: "))
# message = "success" if socre >= 60 else "failure"
# print(message)