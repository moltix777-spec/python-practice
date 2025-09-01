# # 문제 8. 쿠폰 적용 로직
# # 입력: 상품가(정수), 쿠폰 코드(문자열: NONE, S10, FREESHIP)
# # 규칙:
# # S10: 10% 할인
# # FREESHIP: 배송비 3,000원 면제 (단, 상품가 20,000원 미만이면 쿠폰 무효)
# # 출력: 최종 결제 금액(원)

# 1) 입력
price = int(input("상품가 입력하세요(정수) : "))
code = input("쿠폰 코드 입력 해주세요 (NONE, S10, FREESHIP) : ").upper()
valid_code = ("NONE","S10","FREESHIP")
result = ""

# 2) 로직
if code not in valid_code:               # 틀린 문자열 거르기
    print("쿠폰 다시 입력하시오")
else:
    if code in ("FREESHIP") and price >= 20000 :
        result = (f"{price-3000}원 배송비 면제(-3000)")
    elif code in ("S10") :
        result = (f"{price*0.9:.0f}원 ") #:.0f로 소수점 없애기
    else:
        result = (f"{price}원 ")

# 3) 출력
    print(f"최종 결제 금액 -> {result}원 입니다.")

# 소수점 제거 -> int(price * 0.9) / :.0f -> 지정자리에서 반올림 후 표현
# 계산/금액 로직에선 int() → 안정적 (항상 내림, 타입 int 유지) / 화면 출력 꾸밀 땐 :.Nf → 깔끔한 포맷, 반올림 포함
# ("FREESHIP") -> ("FREESHIP",) ','표 확실히 하고 튜플,리스트는 여러개 후보를 검사할때만 쓰고 위의 코드는 문자열로만 !
# result = "" -> result = None  # 잘못된 쿠폰 입력 → 그대로 빈 문자열 남음 파이썬에선 ""가 False 취급되긴 하지만, 문자열로 타입이 묶여 있어서 나중에 함수로 만들거나 로직 확장할 때 “정상 결과 vs 에러 상태” 구분이 애매해짐
# → 디버깅할 때 “왜 빈 문자열이지?” 하면서 헷갈릴 가능성 있음

# 1) 입력
price = int(input("상품가 입력하세요(정수) : "))
code = input("쿠폰 코드 입력 해주세요 (NONE, S10, FREESHIP) : ").upper()
valid_code = ("NONE","S10","FREESHIP")
result = None

# 2) 로직
if code not in valid_code:               # 틀린 문자열 거르기
    print("쿠폰 코드 다시 입력해주세요.")
else:
    if code == "FREESHIP" and price >= 20000:
        result = f"{price - 3000}원 (배송비 면제 -3000)"
    elif code == "S10":
        result = f"{int(price * 0.9)}원 (10% 할인)"
    else:  # NONE or FREESHIP but 조건 미달
        result = f"{price}원"

# 3) 출력
if result is not None:
    print(f"최종 금액 -> {result}")


# 문제 9. 비밀번호 정책(간단)
# 입력: 비밀번호 문자열
# 규칙: 길이 8 이상이고, @ 또는 # 또는 $ 중 하나를 포함하면 통과, 아니면 실패
# 출력: 통과/실패

# 1) 입력
password = input("생성할 비밀번호를 입력해주세요.(@ or # or $ 1개 포함 및 8자 이상)")
result = ""

# 2) 로직
if len(password) >= 8 and ('@' in password or '#' in password or '$' in password ):
    result = "통과"
else:
    result = "생성 실패"

# 3) 출력
print(result)

# if len(password) >= 8 and password == "@" or "#" or "$": -> 파이썬에서 (if len(password) >= 8 and password == "@") or ~ 이래 해석한다
# 지금까지 valid 유효한 애들 튜플로 넣고 in 변수 하다보니 없이 할라니까 모르겠었음 '@' in password

# 문제 10. 영화 요금
# 입력: 나이(정수), 상영 시간대(문자열: day/night), 멤버십(yes/no)
# 규칙:
# 기본요금 12,000원
# 야간(night) +2,000원
# 청소년(만 13~18) -3,000원
# 멤버십 yes면 추가로 -1,000원
# 최소 요금은 0원
# 출력: 최종 요금(원)

# 1) 입력
age = int(input("나이를 입력하세요 : "))
time = input("day/night : ")
membership = input("yes/no :")

night = (time == "night")
youth = (13 <= age <= 18)
member = (membership == "yes")

money = 12000
final = money

# 2) 로직
if night:
    final += 2000
if youth:
    final -= 3000
if member:
    final -= 1000

# 3) 출력
print(f"최종 금액 -> {final}원")

# 10번 문제 if-elif-else로 하려니 청소년,야간,멤버쉽 모든 경우의 수를 다 적고 있는 내 자신을 발견 이건 잘못됐다
# 독립된 조건들을 엮을려고 해서 그럼 -> 내가 모든 경우의 수의 조건문을 적고있다 ? -> if,if,if !
# 입력 부분을 세부 조건에 맞춰서 가공 -> 심플한 조건문 만듬

#이 조건들이 서로 겹치면 안 되나? → if/elif/else

# 이 조건들이 겹칠 수 있고 동시에 적용되나? → if, if, if