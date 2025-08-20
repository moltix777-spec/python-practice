s = "Python"
print(s[0])
print(s[5])
# print(s[2]=x) 오류발생
print(s.replace("t","x"))

a = [10,20,30,40,50]
a.remove(30)
print(a)
a = [10,20,30,40,50]
a.pop(2)
print(a)
a = [10,20,30,40,50]
del a[2]
print(a)
# .remove는 값30을 제거했고
# .pop는 인덱스 2번째 위치한 요솟값을 날려버린거고
# del 은 인덱스 2번째 위치한 요솟값을 삭제 시킨거

nums = [1,2,3,4,5]
x, *mid, y = nums
print(mid)

num = -123
print(abs(num))

print("   Hello world!   ".strip().lower().replace("hello","hi"))

deta = [5,10,15]
print(sum(deta,100))

s = "apple banana apple grape apple"
print(s.count("apple"))
print(s.split('ap'))

tu = (42,)

# .replace()
# .sort()

text = "red,blue,green,blue,yellow,blue"
print(text.split())
print(text.count("blue"))
print(text.split("blue").count("blue"))

# bool 복습
print(type(True))
print(type(False))
print(bool(0),bool(1),bool(""),bool("Python"))

a = 10
b = 20
print(a > b)
print(a == b)
print(a <= b)

fruits = ["apple", "banana", "grape"]
print( "apple" in fruits)
print( "melon" not in fruits)

x = True
y = False
print(x and y)
print(x or y)
print(not x)
print(not y)

age = 25
country = "Korea"
print( age >= 20 and country == "Korea")
print( age < 20 or country == "USA")