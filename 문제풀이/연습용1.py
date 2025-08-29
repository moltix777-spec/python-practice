
# def integer_check(n:int):

#     if n < 0 :
#         result = "음수"
#     elif n == 0:
#         result = "제로"
#     else:
#         result = "양수"
    
#     return result

# print(integer_check(12020302))

# def accumulate_until_100():
#     total = 0
#     while total < 100:
#         n = int(input("정수를 입력하세요: "))
#         total += n
#     return total
# print(accumulate_until_100())

# def even_number_list(a):
#     b =[]
#     for li in a:
#         if li % 2 == 0:
#             b.append(li**2)

#     return sorted(b)
    
# print(even_number_list([3,7,11,15,23,42,24,12,6,8]))

# 문제:
# 숫자 리스트를 입력받아,
# 짝수의 합
# 홀수의 곱
# 가장 큰 값과 가장 작은 값
# 각 숫자의 등장 횟수(빈도수 딕셔너리)
# 를 한 번에 계산해서 반환하는 함수를 작성하시오.


# def analyze_list(nums: list):
#     even=[]
#     odd = []
#     max1 = max(nums)
#     min1 = min(nums)
#     b = 1
#     h = {}
#     for li in nums:
#         if li % 2 == 0:
#             even.append(li)
#         else:
#             odd.append(li)
#     for n in odd:
#         b *= n        

#     for k in nums:                    #---> 여기서 제일 고비 딕셔너리 개념 보충
#         if k not in h:
#             h[k] = 1
#         else:
#             h[k] +=1

#     return f"짝수 합: {sum(even)}\n홀수 곱: {b}\n최댓값: {max1}\n최솟값: {min1}\n{h}"

# print(analyze_list([3, 7, 2, 7, 3, 2, 2, 8]))

# h[k] = h.get(k,0) + 1 이래하면 저 57번~61번줄 코드 대체 가능 
# b = 1 곱셈의 항등원 