a = [1,2,3,['a','b','c']]
print(a[3][1])

a = "안녕하세요"
# print(a.count("요"))

# a = [10,20,30]
# a.append([40,50])
# print(len(a))

# text = "Python is fun"
# print(text.find('i'))
# print(text.find('z'))

# word = "hello"
# print(word.upper())
# print(word.isalpha())

# a = [1,2,3,4]
# a[2]=99
# del a[0]
# print(a)

# text = "     hi     "
# print(text.lstrip())
# print(text.rstrip())
# print(text.strip())

# nums = [10, 2, 33, 4]
# nums.sort()
# nums.reverse()
# print(nums)

# a = "Life is too short"
# print(a.replace("short", "long"))
# print(a.startswith("Life"))
# print(a.endswith("short"))

# a = [1, 2, 3]
# b = ["a", "b", "c"]
# print(a + b)
# print(b * 2)

a = "20250809Sunny"
print("연도: "+a[:4])
print("월: "+a[4:6])
print("일: "+a[6:8])
print("날씨: "+a[8:])

a = "Pithon"

print(a[0]+"y"+a[2:])

a = "Life is too short"
print(a.replace("short","long"))

a = "Python is the best choice"

print(a.find("t"))
print(a.find("b"))

a = [1,2,3,['a','b',['Life','is']]]

print(a[3][2][0])

a =[1,10,399,485289,120,4330,24,58,331]
a.sort()
a.reverse()
print(a)

a = [1,2,3]
a.append([4,5,6])
print(a)

a = [10,20,30,20,40]
a.remove(20)
a.remove(20)
print(a)

a = [100,200,300,400,500]
print(a.pop(2))
print(a)

a = [1,2,3]
b = [4,5]
a.extend(b)
print(a)