# 문제 4. 문자열 정규화 비교
# 입력: 문자열 두 개
# 규칙: 앞뒤 공백 제거 후(strip()), 대소문자 무시(lower())하고 비교
# 출력: 같으면 같음, 다르면 다름

    # 1) 입력
a = input("비교할 단어 입력: " )
b = input("비교할 단어 입력(1): ")

    # 2) 로직 (누적/판정 변수 사용)
if a.lower().strip() == b.lower().strip():
    print("같다")
else:
    print("다르다")

# 문제 5. 좌표 사분면/축 판정
# 입력: 정수 x, y
# 규칙: (0,0)이면 원점, x 또는 y가 0이면 각각 x축 / y축, 그 외에는 1~4사분면 판정
# 출력: 판정 문자열

# 1) 입력
x = int(input("x 값을 입력하시오: "))
y = int(input("y 값을 입력하시오: "))

# 2) 로직
if (x,y) == (0,0) :
    print("원점")
elif x == 0:
    print("y축")
elif y == 0:
    print("x축")
elif x > 0 and y > 0:
    print("제1사분면")
elif x < 0 and y > 0:
    print("제2사분면")
elif x < 0 and y < 0:
    print("제3사분면")
else:
    print("제4사분면")

# label 변수 만들어서 print 중복 줄이기

x = int(input("x 값을 입력: "))
y = int(input("y 값을 입력: "))
label = ""

if (x,y) == (0,0):
    label = "원점"
elif x == 0:
    label = "y축"
elif y == 0:
    label = "x축"
else:
    if x > 0 and y > 0:
        label = "제1사분면"
    elif x < 0 and y > 0:
        label = "제2사분면"
    elif x < 0 and y < 0:
        label = "제3사분면"
    else:
        label = "제4사분면"
print(f"결과 -> {label}입니다!")

# 문제 6. 삼각형 판정
# 입력: 세 변 길이 a, b, c (정수)
# 규칙:
# 삼각형 조건 미충족(두 변의 합 ≤ 나머지 변) → 불가능
# 가능하면: 정삼각형 / 이등변 / 직각 / 일반 중 하나 출력 (직각 판정은 가장 긴 변 기준 피타고라스)

# 1) 입력
a = int(input("각 변의 길이를 입력하시오"))
b = int(input("각 변의 길이를 입력하시오"))
c = int(input("각 변의 길이를 입력하시오"))
triangle = sorted([a,b,c])
a,b,c = triangle
angle = ""

# 2) 로직
if a+b <= c:
    angle = "불가능"
else:
    if len(set(triangle)) == 1:      #리스트 -> 중복 제거 -> len()으로 개수 판별 이게 ㅈㄴ크랙
        angle = "정삼각형"
    elif len(set(triangle)) == 2:
        angle = "이등변 삼각형"
    elif a**2+b**2==c**2:
        angle = "직각 삼각형"
    else:
        angle = "삼각형"
# 3) 출력
print(f"결과 -> {angle} 입니다!")

#입력을 부분을
# a,b,c = map(int, input("세 변 입력 (a b c): ").split())
# triangle에 a,b,c 리스트 정렬 .sort()쓰면 NONE으로 반환 되니까 sorted()로 쓰고
# 다시 a,b,c에 triangle을 집어넣어줘야 정렬된 값이 들어감 -> 직각삼각형 조건에 쓰임

# 문제 7. 카페 라스트오더
# 입력: 요일(weekday/weekend), 시각(0~23 정수)
# 규칙: 기본 라스트오더 21시, 주말은 22시
# 출력: 주문 가능(가능) / 마감(마감)

# 1) 입력
a, day = (input("현재 시각 및 요일 입력(시,요일 생략): ").split())
time = int(a)
weekend = day in "토","일"
result = ""
# 2) 로직
if weekend and time > 22:
    result = "마감"
elif day and time > 21:
    result = "마감"
else:
    result = "주문 가능"
# 3) 출력
print(f"{result}")

# day in ("토","일") -> 튜플/리스트로 안전하게 비교
# 조건식에서 day를 = not weekend로 고쳐야댐
# --> 이러면 날짜 말고 다른 문자열 집어넣어도 로직 작동
# 요일 검증 추가
# 다른 문자열-> not weekend가 Ture 판정이니까 주중 마감으로 나옴 
# 추가 변수에 내가 입력받고싶은 요일 집어넣고 조건문 추가

# 1) 입력
a, day = (input("현재 시각 및 요일 입력(시,요일 생략): ").split())
time = int(a)
vaild_day = ("월","화","수","목","금","토","일")
result = ""
# 2) 로직
if day not in vaild_day:
    result = "오류"
else:
    if day in ("토","일") and time > 22:     #주말 마감
        result = "마감"
    if day not in ("토","일") and time > 21: #평일 마감
        result = "마감"
# 3) 출력
print(f"{result}")

