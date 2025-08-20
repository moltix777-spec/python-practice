s1 = set([1,2,3])
print(s1)

s2 = set("hello")
print(s2)
a = list(s1)
a[2]
b = tuple(s1)
b[1]
print(b)

s1 = set([1,2,3])
t1 = tuple(s1)
print(t1[2])

s1 = set([1,2,3,4,5,6,])
s2 = set([4,5,6,7,8,9])
print(s1 & s2)
print(s1.intersection(s2))

print(s1|s2)
print(s1.union(s2))

print(s1 -s2)
print(s2 -s1)
print(s1.difference(s2))
print(s2.difference(s1))

s1.add(10)
print(s1)

s1.update([10,11,12])
print(s1)

s1.remove(3)
s1.remove(4)
s1.remove(5)
s1.remove(6)
print(s1)