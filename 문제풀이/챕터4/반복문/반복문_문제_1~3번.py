# 문제 1. 1부터 n까지의 합
# 입력: 정수 n
# 출력: 1부터 n까지의 합

# n = int(input("정수 입력 : "))
# print(sum(range(1,n+1)))

# n = int(input("정수 입력 : "))
# i = 1
# result = 0

# while i <= n:
#     result += i
#     i += 1
# print(result)

# n = int(input("정수 입력 : "))
# result = 0

# for i in (range(1,n+1)):
#     result = result+i
# print(result)

# 문제 2. n부터 1까지 출력
# 입력: 정수 n
# 출력: n, n-1, …, 1

# # n = int(input("정수 입력 : "))
# # i = 0
# # result = ""
# # a = []
# # while i < n:
# #     result = n - i
# #     a.append(str(result))
# #     i += 1
# # print(a)

# # result join 안쓸꺼면 문자열로 변환할 필요없

# n = int(input("정수 입력 : "))
# i = n
# a = []
# while i > 0:
#     a.append(i)
#     i -= 1
# print(a)


# n = int(input("정수 입력 : "))
# result = 0
# a = []
# for i in range(1, n+1):
#     result = i
#     a.append(str(result))
# a.reverse()
# print(a)

# # 역순 range(n,0,-1)이렇게 고치면 직관적
# # 변수 result 지정 굳이 하지마

# n = int(input("정수 입력 : "))
# a = []
# for i in range(n, 0, -1):   # 역순 range
#     a.append(i)
# print(a)

# 문제 3. 짝수 합 구하기
# 입력: 정수 n
# 출력: 1부터 n까지의 짝수 합

# n = int(input("정수 입력 : "))
# i = 0
# result = 0

# while i <= n:
#     if i % 2 ==0 :
#         result += i
#     i += 1
# print(result)

# n = int(input("정수 입력 : "))
# result = 0

# for i in (range(1,n+1)):
#     if i % 2 == 0:
#         result += i
# print(result)

