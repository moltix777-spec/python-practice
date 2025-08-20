a = {1:'hi'}
a = {1:[1,2,3]}

a = {1:'a'}
a[2] = 'b'
a['name'] = 'ghd'
del a[2]

print(a['name'])

a = {'name': 'Hong'}
a['phone'] = '010-1234-5678'
a['birth'] = '0811'
# print((a.keys()))
# print(a.values())
# print(a.items())
# a.clear()
# print(a)
# print(a.get('name'))
# print('name' in a)
print(a.get('nokey','키가없음')) 