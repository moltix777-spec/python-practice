f = open("새파일.txt", 'w')
for i in range(1,11):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close()

for i in range(1,11):
    data = f"{i}번째 줄입니다."
    print(data)

f = open("새파일.txt", 'r')
line = f.readline()
print(line)
f.close()

f = open("새파일.txt", 'r')
while True:
    line = f.readline()
    line = line.strip()
    if not line:
        break
    print(line)
f.close()

while True:
    data = input()
    if not  data:
        break
    print(data)

f = open("새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    line = line.strip()
    print(line)
f.close()

f = open("새파일.txt", 'r')
data = f.read()
print(data)
f.close()

f = open("새파일.txt",'r')
for line in f:
    line = line.replace("\n",'')
    print(line)
#     line = line.strip()
#     print(line)
# #   print(line, end= "")
f.close()

f = open("새파일.txt",'a')
for i in range(11,20):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close()

with open("hong.txt",'w') as f:
    f.write("Life is too short, you need Python")
