# # result = 0
# # def add(num):
# #     global result
# #     result += num
# #     return result
# # print(add(3))
# # print(add(3))

# class FourCal:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second       

#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
#     def mul(self):
#         result = self.first * self.second
#         return result
#     def sub(self):
#         result = self.first - self.second
#         return result
#     def div(self):
#         result = self.first / self.second
#         return (result)

# # a = FourCal()
# # a.setdata(10,8)
# # print(a.add())
# # print(a.mul())
# # print(a.sub())
# # print(a.div())

# # b = FourCal()
# # b.setdata(3,100)
# # print(b.add())
# # print(b.mul())
# # print(b.sub())
# # print(b.div())

# class MoreFourCal(FourCal):
#     def pow(self):
#         result = self.first ** self.second
#         return result
# class SafeFourCal(FourCal):
#     def div(self):
#         if self.second == 0:
#             return 0
#         else:
#             return self.first / self.second

# # a = MoreFourCal(4,2)
# # print(a.pow())

# a = SafeFourCal(4,0)
# print(a.div())

# class Family:
#     lastname = "김"   # 클래스 변수 (공유)

# # 객체 2개 생성
# a = Family()
# b = Family()

# print(a.lastname)  # 김
# print(b.lastname)  # 김

# import mod1
# print(mod1.add(3,120))
# print(mod1.sub(100,2))

# from mod1 import add
# print(add(3,4))
# from mod1 import sub
# print(sub(10,3))

# import mod1

# import mod2
# # print(mod2.PI)
# a= mod2.Math()
# print(mod2.add(5,4))
# print(a.solv(2))
# import sys
# sys.path.append("C:/Users/홍진규/Desktop/파이썬왕초보/조코딩/python-practice/python-practice/문제풀이/반복문")

# import mod3

# a = mod3.Math()
# print(a.solv(5))

