# 가벼운복합
t = (1,2,2,3)
I= [3,3,4,1]
y = set(t)|set(I)
d = {"score" : 10}
a = list(y)
a.sort()
d["score"] += len(a)
print(a)
print(d)

# 문자열변환
text = "Python is fun"
a = text.replace("fun","awesome")
print(a.upper())

# 리스트조작
nums = [10, 20, 30, 40]
nums[0], nums[-1] = nums[-1], nums[0]
del nums[len(nums)//2] # < 이 부분 이해가안됨
print(nums)

# 튜플 <> 리스트변환+ 값변경
data = (100, 200 ,300 ,400)
li = list(data)
li[1] = 999
tu = tuple(li)
print(tu)

# 집합연산
a = {1,2,3}
b = {3,4,5}
s = a & b
s.add(99)
print(s)

# 딕셔너리 수정
colors = {"red":1, "blue":2, "green":3}
colors["blue"] = 7
colors["yellow"] = 5
print(colors)

# 문자열 가공
text = "    machine learning     "
a = text.strip()
a = a.lower()
a = a.replace("learning","vision")
print(a)  
#  저 위에 3개 메서드 함수는 원본을 안바꾸고 새로운 문자열 반환했으니 변수안에 넣어줘야대

# 문자열 검색
word = "abracadabra"
print(word.find("bra"))

# 중복제거 + 정렬
nums = [5, 3, 5, 2, 8, 3]
a = set(nums)
li = list(a)
li.sort()
li.reverse()
print(li)

# 집합수정
s = {1, 3, 5, 7}
li = list(s)
del li[2]
li.append(9)
print(set(li))
# ---집합 순서없어서 3번째줄이 예측 불가임 ---
s = {1,3,5,7}
s.remove(5)
s.add(9)
print(s)
# --- 이게 정답 집합 전용 메서드 까먹지마

# 딕셔너리 추가
pets = {"cat":2,"dog":4}
pets["bird"] = 3
print(pets)

# 문자열 판별
word = "Python3"
print(word.isalpha())

# 리스트 값 변경 + 추가
nums = [100, 200, 300]
nums[0] = 500
nums.append(999)
print(nums)

# 문자 개수 세기
text = "hello world"
print(text.count("l"))