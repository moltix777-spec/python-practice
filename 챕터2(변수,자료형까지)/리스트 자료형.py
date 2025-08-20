odd = [1,3,4,7,9]
print(type(odd))

a = [1,2,["Life","is}"]]
print(type(a))

a = [1,2,3,4,5]
print(a[0])
print(a[3])
print(a[-2])
print(a[0]+a[-1])

a = [1,2,3,['a','b','c']]
print(a[0])
print(a[3])
print(a[-1][1])

a = [1,2,3,['a','b',['Life','is']]]
print(a[3][2][0])

a = [1,2,3,['a','b',['Life','is']]]

print(a[3][2][1:])

a = [1,2,3]
# b = ["a","b","c"]

# print(a+b*2)
# print(len(b))

print(str(a[2])+"hi")

a = [1,2,3,4]

a[3] = 10
print(a)

a = [1,2,3,4]
del a[3]
print(a)

a = [1,2,3,4,5,6,7,8]
del a[-2:]
print(a)

a = [1,2,3]
a.append([4,5,6])
print(a)
# 이거 append 뒤에는 1개의 요솟값만 가능

a = [1,10,399,485289,120,4330,24,58,331,24]
# a.sort() 숫자 오름차순 정리
# a.reverse() 리스트 값을 거꾸로 
# print(a)
# print(a.index(120)) 몇번째에 있는지
# a.insert(4,999) 4번째 자리에 999집어넣어라
# a.remove(24) 처음나오는 24 제거해라
# a.remove(24) 2번쓰면 2번쨰 까지도 제거
# b = a.pop(3)
# print(b)
# print(a) pop으로 뺀 요솟값은 반환이 되는구나!
# print(a.count(24))
a.extend([24,10])
b = [77]
a.extend(b)
print(a.count(24))

a = "  hello  "
print(a.rstrip(a))
