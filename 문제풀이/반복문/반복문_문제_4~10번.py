# 문제 4. 구구단 출력
# 입력: 단 수 (예: 7)
# 출력: 7×1 ~ 7×9

# n = int(input("2~9까지 숫자 입력 : "))
# i = 1
# result = 0
# a = []

# while i < 10 :
#     result = n * i
#     i += 1
#     a.append(result)
# print(a)

# n = int(input("2~9까지 숫자 입력 : "))
# result = 0
# a = []

# for i in range(1,10) :
#     result = n * i
#     a.append(result)
# print(a)

# 루프안에 출력을 넣으면 한줄로 나옴 그냥 나는 이쁘게 리스트에 담아봤음

# n = int(input("2~9까지 숫자 입력 : "))
# i = 1
# result = 0
# a = []

# while i < 10 :
#     result = n * i
#     i += 1
#     print(result,end =" ")


# 문제 5. 약수 구하기
# 입력: 정수 n
# 출력: n의 모든 약수 (1, …, n)

# n = int(input("정수 n을 입력 : "))
# i = 1
# a = []
# while i <= n :
#     if n % i == 0:
#         a.append(str(i))
#     i += 1
# print(",".join(a))
 
# print(a)

# n = int(input("정수 n을 입력 : "))
# a = []
# for i in range(1,n+1) :
#     if n % i == 0:
#         a.append(str(i))
# print(",".join(a))

# 문제 6. 별 찍기 (왼쪽 직각삼각형)
# 입력: 정수 n
# 출력:
# *
# **
# ***
# ...

# n = int(input("정수 n 입력 : "))
# i = 1
# while i <= n:
#     print('*'* i)
#     i+=1

# n = int(input("정수 n 입력 : "))

# for i in range(1, n+1):
#     print('*' * i)

# 문제 7. 1부터 n까지 합 (단, 3의 배수는 제외)
# 입력: 정수 n
# 출력: 3의 배수를 제외한 합

# n = int(input("정수 n을 입력 : "))
# i = 1
# result = 0
# while i <= n:
#     if not i % 3 == 0:
#         result += i
#     i += 1
# print(result)

# n = int(input("정수 n을 입력 : "))
# result = 0
# for i in range(1,n+1):
#     if not i % 3 == 0:
#         result += i
# print(result)

# if not i % 3 == 0: --> if i % 3 != 0 / != 이거 까먹었냐 까먹지마라 간편한거 있다

# 문제 8. 문자열 거꾸로 출력
# 입력: 문자열
# 출력: 입력받은 문자열을 거꾸로 출력

# a = input("편하게 적어 : ")
# i = len(a)-1 # -> 인덱스 0번부터 시작하니까 ..

# # print(a[::-1])

# while i >= 0 :
#     print(a[i],end="")
#     i -= 1

# a = input("편하게 적어 : ")

# for i in range(len(a)-1,-1,-1):
#     print(a[i],end="")

# 문제 9. 소수 판별
# 입력: 정수 n
# 출력: n이 소수면 "소수", 아니면 "합성수"

# n = int(input("정수 n 입력 : "))
# i = 2
# result = "소수"

# while i < n :
#     if n % i ==0:
#         result = "합성수"
#         break
#     i += 1
# if n <= 1:
#     result = "합성수"

# print(result)

# n = int(input("정수 n 입력 : "))
# result = '소수'

# for i in range(2,n):
#     if n % i == 0:
#         result = '합성수'
#         break # --> 불필요하게 덮어쓰는 과정 최소화
# if n <= 1:
#     result = '합성수'

# print(result)

# 문제 10. 피보나치 수열
# 입력: 정수 n
# 출력: n번째 항까지 피보나치 수열

# n = int(input("정수 n 을 입력 : "))
# i = 0
# a,b = 0,1
# while i < n :
#     print(a,end=' ')
#     a,b = b,a+b
#     i +=1

n = int(input("정수 n 을 입력 : "))
a,b = 0,1

for i in range(n):
    print(a,end =" ")
    a,b = b, a+b


# range(star,stop,step) 
# range(5)         # 0~4
# range(2, 6)      # 2~5
# range(1, 10, 2)  # 1,3,5,7,9 (홀수만)
# range(10, 0, -2) # 10,8,6,4,2 (역순 짝수)
