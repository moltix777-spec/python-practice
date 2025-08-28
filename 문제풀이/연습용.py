# #조건문 문제 1. 배송비 계산기

# def delivery_fee(s:int,h: str):
#     result = 0
#     if h not in ("basic","silver","gold"):
#         return ("오류")

#     if h == "gold" and s >= 30000: # 골드등급 및 3만원 이상 무료 배송
#         result = s
#     elif s >= 50000: # 5만원 이상 무료 배송
#         result = s
#     else:
#         result = s + 3000

#     return f"최종 배송비 -> {result}원 입니다"
       
# print(delivery_fee(30000,"gold"))

# 연습 문제 (kwargs 버전)
# 문제:
# 학생의 이름과 점수를 **kwargs로 입력받아,
# "이름: 점수" 형식으로 이어붙인 문자열을 리턴하는 함수를 작성하시오.

# def report_score(**kwargs):
#     b = []
#     for name,score in kwargs.items():
#         b.append(f"{name}:{score}")
#     return ','.join(b)         

# print(report_score(철수=90, 영희=85, 민수= 100))

# 📝 연습 문제 (심화 kwargs)
# 문제:
# 가게에서 여러 물품을 판매한다.
# 물품과 수량을 **kwargs로 받아서 총 가격을 계산하는 함수를 작성하시오.
# 단, 가격표는 함수 안에 딕셔너리로 고정되어 있다.
# 없는 물품이 들어오면 "메뉴에 없음" 메시지를 출력하고 무시한다.

# def calc_total(**kwargs):
#     menu = {"사과": 1000, "바나나": 1500, "딸기": 2000}
#     total = 0
#     for fruit in kwargs.keys():
#         if fruit not in menu:
#             print(f"메뉴에 없음 : {fruit}")
#     for fruit,count in kwargs.items():
#         count = int(count)
#         if fruit in menu:
#             total += menu[fruit] * count

#     return total

# print(calc_total(사과=2, 바나나=3, 수박=1))
# 메뉴에 없음: 수박
# 총액 = 6500원

# 연습 문제 (심화)

# 문제:
# 학생들의 시험 점수를 받아서,
# 평균 점수를 구하고
# 최고점 학생, 최저점 학생을 출력하며
# 평균 이상인 학생들의 명단을 리스트로 반환하는 함수를 작성하시오.

# 조건
# 함수 매개변수는 **scores (학생이름=점수 형식).
# 점수는 0~100 사이 정수라 가정.
# 출력 형식은 자유.


# def analyze_scores(**scores):
#     if not scores :
#         return "오류"
#     average = sum(scores.values())/len(scores) # 평균값 구함
#     max1 = max(scores.values())            
#     min1 = min(scores.values())

#     x = []
#     top_names = []
#     low_names = []
    
#     for name,score in scores.items():
#         if score == max1:
#             top_names.append(name)
#         if score == min1:
#             low_names.append(name)

#     for name,b in scores.items():
#         if b >= average:
#             x.append(name)
            
#     return f"평균 점수: {average:.1f}\n1등 : {','.join(top_names)}({max1})\n꼴등 : {','.join(low_names)}({min1})\n {x}"
   
# print(analyze_scores(철수=2, 영희=91, 민수=77, 지훈=95, 수진=2))


# 평균: for문 안에서 계속 갱신하지 말고, 전체 점수 다 모은 뒤 한 번에 계산.
# 최고/최저: 루프 중간에 찾지 말고, 전체 데이터 기준으로 계산.
# 리스트 b: 점수만 따로 모으는 리스트 불필요 → scores.values()에서 바로 평균/최대/최소 가능.
# 동점자 있을수도 있으니 리스트 모아둬서 출력때 join활용