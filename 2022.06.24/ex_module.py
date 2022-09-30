# -----------------------------------------------------------------
# 모듈(Module) : 하나의 파이썬(.py) 파일
#               특정 목적에 관련된 변수, 함수, 클래스 존재
#               필요한 파일에서 사용 가능 함
# 사용법 => import 모듈명
# -----------------------------------------------------------------
# 5! => 1*2*3*4*5     /    10! => 1*2*3*4*5*6*7*8*9*10
# 종이모양-모듈   / 파일모양-패키지
# 모듈 포함 하기 ----------------------------------------------------
###import math
##import math as m
###from math import factorial
#from math import factorial, pi, fabs

import ex_func

def factorial(num):
    print(f'My Factorial - {num}')

# 모듈 안에 기능 사용하기 ---------------------------------------------
###print(math.factorial(5))
##print(m.factorial(5))
###print(factorial(10))
#print(factorial(10), pi, fabs(2))
print(factorial(10))
print(ex_func.YEAR, ex_func.printYear())

print("-------")

