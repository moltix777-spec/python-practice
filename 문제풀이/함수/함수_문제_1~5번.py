# 제 1. 1부터 n까지 합
# 양의 정수 n이 주어지면 1..n의 합을 반환.

# def sum_to_n(n):
#     total = sum(range(1,n+1))
#     return total
# print(sum_to_n(10))
# n*(n+1)//2 = 수학공식을 쓰면 더 큰 n값에서 빠르게 구할수있

# 문제 2. 최댓값/최솟값
# 정수 리스트에서 (최댓값, 최솟값) 튜플을 반환.

# def max_min(nums):
#     mx = nums[0]
#     mn = nums[0]
#     for n in nums:
#         if n > mx:
#             mx = n
#         if n < mn:
#             mn = n
#     return (f"최대값 -> {mx} , 최소값 -> {mn}")
# print(max_min([2,10,-4,29,138]))

# def max_min(nums):
#     return (max(nums), min(nums))
# print(max_min([2,10,-4,29,138]))
# # 내장함수 딸깍

# 문제 3. 이름 포맷팅 (기본값 인자)
# first, last로 이름을 받아
# "Last, First" 문자열 반환. upper=True면 대문자로.

# def formt_name(first, last,upper=False):
#     formetted = last + ", " + first
#     if upper :
#         formetted = formetted.upper()
#     return formetted
# print(formt_name("park","jone"))
# print(formt_name("park","jone",upper = True))

# 매개변수에 조건을 넣고 조건분기 설정 인수에 조건 제어 출력

# 문제 4. 모음 개수 세기
# 문자열에서 모음(a e i o u, 대소문자 구분 X) 개수 합을 반환.

# def count_alpha(s:str):
#     a = s.lower().count('a')
#     e = s.lower().count('e')
#     i = s.lower().count('i')
#     o = s.lower().count('o')
#     u = s.lower().count('u')

#     result = a+e+i+o+u
#     return result
# print(count_alpha("Hello World"))

# 내장함수 .count()로 직관적 표현

# def count_alpha(s:str):
#     b = s.lower()
#     result = 0
#     for i in b:
#         if i in ('a','e','i','o','u'):
#             result += 1
#     return result
# print(count_alpha("afjioqrwqiopsapiqwopq"))

# .count() 로직을 반복문, 조건문 로직으로 구현 

# 문제 5. 할인 쿠폰 적용 (*args)
# 기본 가격에 쿠폰 코드를 여러 개 적용. *coupons는 문자열 집합 중 일부일 수 있음.
# 기본 가격: 정수(원)
# 쿠폰: 'S10'(10%↓), 'S20'(20%↓), 'M1000'(1000원↓)
# 음수 불가 → 최소 0원 보장

# def h(price: int, *coupons: str):
#     result = price
#     for c in coupons:
#         if c == "S10":
#             result *= 0.9
#         if c == "S20":
#             result *= 0.8
#         if c == "M1000":
#             result -= 1000
#     return max(int(result), 0)

# print(h(12000, "S10", "S20" , "M1000"))

# *coupons 여러개 튜플이기 땜시 for로 하나씩 담고 if if if 독립 조건으로 중복적용까지 (조건문10번문제 참조)
# gpt가 if eilf eilf 로 피드백주길래 실수잡아냄 뿌듯함

