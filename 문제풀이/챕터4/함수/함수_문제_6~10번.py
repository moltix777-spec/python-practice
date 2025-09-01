# 문제 6. 안전 나눗셈 (키워드 전용 인자)
# a/b 결과를 소수점 ndigits 자리로 반올림해 반환. b=0이면 None 반환.

# def safe_divide(a: float, b: float, ndigits: int = 2) :
#     if b == 0:
#         return None
#     c = a/b
#     return f"{c:.{ndigits}f}"
# print(safe_divide(3,5))

# 결과물 지금은 문자열인데 수치로 연결해서 쓸려면 return round(c, ndigits)

# 문제 7. URL 생성 (**kwargs)
# 기본 URL과 쿼리 파라미터를 받아 정렬된 쿼리스트링을 붙여 반환. 값은 URL 인코딩 가정 생략.

# def build_url(base: str, **params) -> str:
#     if not params:
#         return base
#     # {'q': 'python', 'page': 2}
#     query = "&".join(f"{k}={v}" for k, v in params.items())
#     return f"{base}?{query}"

# print(build_url("google.com/search", q="python", page=2))
# url 구조를 몰라서 헤맸음 딕셔너리 형태로 인수를 받아서 리턴값을 url 구조에 맞춰서 for문에 .items() 딕셔너리 문법써서 가공

# 문제 8. 피보나치 리스트
# 정수 n을 받아 앞에서부터 n개 피보나치 수를 리스트로 반환. (반복문 사용, 재귀 금지)

# def fibonacci_list(n: int) :
#     seq = []
#     a,b = 0,1
#     for _ in range(n):
#         seq.append(a)
#         a,b = b, a+b
#     return seq
# print(fibonacci_list(10))

# for _ in 할떄 _ 이거는 반복만할거고 변수_ 이거는 안쓸거야 라는 국룰표시 
# 빈리스트에는 a만 담으면댐

# 문제 9. 소수 판별 (√n 최적화)
# n이 소수면 True, 아니면 False 반환. n ≤ 1은 False. 약수 탐색은 2..⌊√n⌋까지만

# def is_prime(n: int) -> bool:
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# print(is_prime(1993))

# int(n**0.5) -> 루트 n을 기준으로 삼고 돌려도댐

# 문제 10. 주문 합계 계산
# 주문 문자열을 파싱해 총액을 반환. 포맷 예: "americano:2, latte:1, tea:3"

# 메뉴 가격: americano=1500, latte=2000, tea=1200
# 공백은 자유롭게 들어올 수 있음
# 정의되지 않은 메뉴는 무시

# def order_total(s: str) -> int:
#     menu = {"아메리카노":1500,"라떼":2000,"차":1200}
#     total = 0
#     orders = s.split(",")
#     for order in orders:
#         name , count = order.split(":")
#         count = int(count)
#         if name in menu:
#             total = total + menu[name] * count

#     return total
# print(order_total("아메리카노:10,라떼:120,차:12030"))

# 주문 문자열을 파싱해 메뉴판과 매칭하여 총액 계산
# 7번이랑 차이점 머릿속에 집어넘