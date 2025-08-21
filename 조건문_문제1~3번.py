# 문제 1. 배송비 계산기
# 입력: 주문금액(정수, 원), 회원등급(문자열: basic, silver, gold)
# 규칙:
# 기본 배송비 3,000원
# 주문금액이 50,000원 이상이면 무료
# 회원등급이 gold면 주문금액이 30,000원 이상이면 무료
# 출력: 최종 배송비 (원)

amount = int(input("주문금액을 입력해주세요.(정수) : "))
level = input("등급을 입력해주세요,(basic,silver,gold): ")
if amount >= 30000 and level == "gold":
    print(f"{level}등급과 주문금액이 30,000d원 이상이므로 무료배송!")
elif amount >= 50000:
    print("주문 금액이 50,000원 이상이므로 무료배송!")
# elif amount < 50000:
#     print(f"배송비는 {amount+3000}원 입니다.")
# else:
#     pass
else:
    print(f"배송비 3,000원 추가 총 {amount+3000}원 입니다.")
# 2번째 elif는 빼고 그걸 else에 넣으면 더 깔끔한 구조

# 문제 2. 학점(플러스/마이너스)
# 입력: 점수(0~100 정수)
# 규칙: A/B/C/D/F 구간 판정 후, 각 구간에서 7 이상이면 +, 3 미만이면 - (예: 93 → A, 97 → A+ , 81 → B-)
# 출력: 등급 문자열
score = int(input("점수를 입력해주세요 (정수): "))
num = score // 10
digit = score % 10
if num >= 9 and digit >= 7:
    print(f"{score}점 -> A+ 입니다!")
elif num >=9 and digit < 3:
    print(f"{score}점 -> A- 입니다!")
elif num >=9 and 3 <= digit <7:
    print(f"{score}점 -> A 입니다!")
elif num >=8 and digit >=7:
    print(f"{score}점 -> B+ 입니다!")
elif num >=8 and digit < 3:
    print(f"{score}점 -> B- 입니다!")
elif num >=8 and 3 <= digit <7:
    print(f"{score}점 -> B 입니다!")
elif num >= 7 and digit >= 7:
    print(f"{score}점 -> C+ 입니다!")
elif num >=7 and digit < 3:
    print(f"{score}점 -> C- 입니다!")
elif num >=7 and 3 <= digit <7:
    print(f"{score}점 -> C 입니다!")
elif num >= 6 and digit >= 7:
    print(f"{score}점 -> D+ 입니다!")
elif num >=6 and digit < 3:
    print(f"{score}점 -> D- 입니다!")
elif num >=6 and 3 <= digit <7:
    print(f"{score}점 -> D 입니다!")
else:
    print(f"{score} -> F 입니다.")
# 이것도 num는 grade 변수로 값 모으고 digit는 sign변수로 값모아서 
# 마지막 포매팅으로 깔끔하게 구조 단축
score = int(input("점수를 입력해주세요 (정수): "))
num = score // 10
digit = score % 10
grade = ""
sign = ""
if num >=9:
    grade = "A"
elif num == 8:
    grade = "B"
elif num == 7:
    grade = "C"
elif num == 6:
    grade = "D"
else:
    grade = "F"

if grade !="F":
    if digit >= 7:
        sign = "+"
    elif digit <3:
        sign ="-"
    else:
        sign=""
print(f"{score}점 -> {grade}{sign}입니다!")
#내가 위의 코드를 생각하면서 앞자리 뒷자리 쪼갰는데
# 조건문 밑에 print 출력이 묶여있다는 생각이 지배적이였음

# 문제 3. 주차 요금 계산
# 입력: 요일(문자열: weekday 또는 weekend), 시간(0~23 정수)
# 규칙:
# 기본 요금 2,000원
# 주중 18~23시는 야간 할증 +1,000원
# 주말(weekend)은 12~17시에 한해 할인 -500원 (단, 최소 0원)
# 출력: 최종 요금 (원)
day = input("무슨 요일입니까?: ")
time = int(input("몇 시 입니까? (정수): "))
weekday = day == "월", "화", "수","목","금"
weekend = day == "토", "일"
night = 18 <= time <=23
sun = 0 <= time <= 18
charge = 2000
if weekend and sun:
    print(f"주말,낮 ->{charge-500}")
elif weekend and night:
    print("주말 ")

# 뭔가 너무 어렵게 하는거같아서 gpt hlep
# 요금 계산은 charge에 누적하고 마지막에 포매팅이용해서 프린트
# 조건 주중 야간, 주말 낮 만 조건문하고 나머지는 기본요금

day = input("무슨 요일입니까?")
time = int(input("몇 시 입니까? (0~23): "))
is_weekend = day in ("토","일")
charge = 2000

if not is_weekend and 18 <= time <= 23: # 주중 야간 할증
    charge += 1000
elif is_weekend and 12 <= time <= 17: # 주말 낮 할인
    charge -=500
if charge <0:
    charge = 0
print(f"최종 요금: {charge}원 입니다!")
