a = 10
b = 3
print(a*b)
print(a+b)

s = 'Hello World'
print(s.replace('World','Python'))

nums = [4,1,7,1,4]
s = set(nums)
li = list(s)
li.sort()
print(li)

t = (1,2,3)
li = list(t)
li.append(4)
print(li)

d ={'name':'Jin','age':20}
d['age']+=1
print(d)

set1 = {1,2,3}
set2 = {3,4,5}
print(set1 & set2)
print(set1 | set2)

text = "   Python   "
a = text.strip()
print(a.upper())
print("   Python   ".strip().upper())

s = 'abBacCaaBB'
print(s.lower().count("ab"))

phone ='010-1234-5678'
a = phone.replace("-","")
print(a[-4:])

nums = [3,10,3,2,10,5]
s = set(nums)
print(sum(s))

data = [('Jin', 20), ('Yu', 22), ('Kim', 21)]
a = data[0][0],data[1][0],data[2][0]
print(a)

word = 'mississippi'
print(word.count("i"))
print(word.count("s"))

d = {'a':1,'b':2}
e = {'b':5,'c':3}
d.update(e)
print(d)

s = '   Hello, Python!!!   '
a = s.strip()
print(a.replace(",","").replace("!!!","").lower())
print('   Hello, Python!!!   '.strip().replace(",","").replace("!!!","").lower())

p = (2,5)
q = (7,1)
x1,y1 = p
x2,y2 = q
print(abs(x1-x2) + abs(y1-y2))

prices = [1200, 3000, 1200, 5000, 3000]
a = set(prices)
li = list(a)
li.sort()
print(li)
print(sum(li)/len(li))

sentence = 'Python is fun and FUN for pythonistas'
print(sentence.lower().count("fun"))
