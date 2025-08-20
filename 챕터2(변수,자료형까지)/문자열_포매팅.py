name = "민수"
age = 27
print(f"{name}는 {age}살입니다.")

n = 42 
print(f"{n:>6}")

x = 3.141592
print(f"{x:.3f}")

money = 1234567
print(f"{money:,}")

s = "python"
print(f"{s.upper():^12}")

item = "USB"
price = 9800
print(f"{item}:{price:,}원")

a=5
b =8
print(f"{a}+{b} = {a+b}")

import math
r = 2.5
print(f"{2*math.pi*r:.3f}")

d = {"lang":"Python","ver":3.12}
# print("{lang} {ver}".format(**d))
# print("{0[lang]} {0[ver]}".format(d))
# print(f"{d["lang"]} {d["ver"]}")- 따옴표 '로 수정

first = "Kim"
last = "Minsoo"
print(f"{first}{last}")