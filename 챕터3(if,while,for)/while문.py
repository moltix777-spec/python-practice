treeHit = 0
while treeHit < 10:
    treeHit += 1
    print(f"헛짜 나무를 {treeHit}번 찍었습니다 ! ")
    if treeHit == 10:
        print("어어 쓰러진다 형씨 조심해 !")
    
prompt = """
1. 게임입장
2. 삭제
3. 설정
4. 나가기
Enter number:"""
number = 0
while number !=4 :
    print(prompt)
    number = int(input())

coffee = 10
money = 300
while money:
    print("300원 확인 커피 줄게")
    coffee -= 1
    print(f"남은 커피 수량은 {coffee}입니다.")
    if coffee == 0:
        print("장사종료")
        break

coffee = 10
while True:
    money = int(input("돈 줘"))
    if money == 1200:
        print("자 여기 커피 받아")
        coffee -=1
        print(f"남은 커피는 {coffee}입니다")
    elif money > 1200:
        print(f"거스름돈 {money-1200}받고 커피 받아")
        coffee -=1
        print(f"남은 커피는 {coffee}입니다")
    else:
        print("꺼져")
        print(f"남은 커피는 {coffee}입니다")
    if coffee == 0:
        print("장사 종료 퇴근")
        break

# 10까지 홀수들을 리스트에 이쁘게 담아봄
nums = []
a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    nums.append(str(a))
print(",".join(nums))

