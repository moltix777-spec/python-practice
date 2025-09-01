# try:
#     #오류가 발생할 수 있는 구문
# except:
#     #오류 발생
# else:
#     #오류 발생하지 않음
# finally:
#     #무조건 마지막 실행

# try:
#     4/0
# except ZeroDivisionError as e:
#     print("오류 발생 ! 비상 !")

# try:
#     f = open('foo.txt', 'w')

# finally:
#     f.close()  # 중간에 무슨일이 일어나더라도 실행하는 것

# many_error.py
# try:
#     a = [1,2]
#     print(a[3])
#     4/0
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# except IndexError:
#     print("인덱싱 할 수 없습니다.")
