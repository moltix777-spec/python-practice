list = ['one','two','three']
for i in list:
    print(i)

a = [(1,2),(3,4),(5,6)]
for (b,c) in a :
    print(b+c)

socre = [90,25,67,45,80]
num = 0
for a in socre:
    num += 1
    if a >= 60:
        print(f"{num}번 학생 합격")
    elif a >= 40:
        print(f"{num}번 학생 재시험")
    else:
        print(f"{num}번 학생 사형")
for a in socre:
    num += 1
    if a < 60:
        continue
    print(f"{num}번 학생 축하합니다. 합격입니다")

score = [90,25,67,45,80]
for num in range(len(score)):
    if score[num] < 60:
        continue
    print(f"{num}번 학생 축하합니다. 합격")

# len스코어는 5 -> range 5는 0부터4까지 그걸 socre[0부터4까지 대입]
# 이런 흐름

a = 0
for i in range(1,11):
    a = a + i
print(a)
# 프린터 에이를 for문 밖으로 빼면 한번에 반복된 마지막값이 나오고 안으로 넣으면 피라미드맹키로 출력

add = 0 
for i in range(1, 11): 
     add = add + i 
print(add)

for i in range(2,10):
    for j in range(1,10):
        print(i*j,end=" ")
    print(' ')

a = [1,2,3,4,5]
b = []
for num in a:
    b.append(num*3)
print(b)

print(*(num *3 for num in a),sep=",")
print([num *3 for num in a])

for i in range(10):
    if i == 5:
        print("종료")
        break
    print(i,end=(" "))

for i in range(10):
    print(i)
else:
    print("끝")

fruits = ['apple','banana','orange']
for i,fruits in enumerate(fruits,1):
    print(f"{i}: {fruits}",end=(" - "))

name = ['홍길동', '김길동', '박길동']
score = [85,92,78]
results = []
for a,b in zip(name,score):
    if b > 80:
        results.append(f"{a}: {b}점 합격")
    else:
        results.append(f"{a}: {b}점 불합격")
print(", ".join(results))
    
print(*[f"{a}: {b}점 합격" if b > 80 else f"{a}: {b}점 불합격" for a,b in zip(name, score)],sep =",")