def h(a,b):
    result = a*b
    return result
y = h(5,9)
print(y)

def h(a,b):
    result = a + b
    print(result)
h(3,4)

def h():
    return "Hi"
x = h()
print(x)

def check_even_odd(num):
    if num % 2 == 0:
        return "짝수"
    else:
        return "홀수"

print(check_even_odd(3))  # 홀수
print(check_even_odd(10)) # 짝수
print(check_even_odd(100))
   
def calc_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)

    if bmi >= 25:
        status = "비만"
    elif bmi >= 18.5:
        status = "정상"
    else:
        status = "저체중"
    return bmi, status

b,c = calc_bmi(67,180)
print(f"BMI={b:.2f}, 상태 ={c}")
a = calc_bmi(67,180)
print(f"BMI={a[0]:.2f}, 상태 = {a[1]}")

print(calc_bmi(76, 175))  # (22.8..., '정상')

# 함수 파트부터는 지금까지 실전문제 스크립터들을 함수화 시키고
# 응용하듯이.

# 오늘은 내가 if문으롤 만든 bmi 스크립트를 함수로 바꿨음
# 헷갈린부분은 출력부분에서 보통 print에 변수 생각만 하다가
# 여기에 인수를 넣고 나오는게 리턴값이 나온다.
# 리턴값을 내 입맛대로 가공하는법.
