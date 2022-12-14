# -------------------------------------------------------
# 함수 (Function) : 자주 사용되는 기능을 묶어서 이름을 붙여 놓은것
# - 코드 재상용 위한 것
# 형태
# def 함수명(   재료,......,재료n):
# 코드
# 코드
# return 결과
# --------------------------------------------------------

# --------------------------------------------------------
# 기       능  : 숫자 2개 더한 후 결과 돌려주는 기능
# 함   수   명  :   addTwo
# 재료(매개변수) : num1 num2
# 결과(반환값)   : 더한 값
# HISTORY      : 2022-04-03 SO create
# ---------------------------------------------------------
def addTwo(num1, num2):
    '''
    숫자 2개 더한 후 결과 반환
    :param num1:
    :param num2:
    :return:
    '''
    value=num1+num2
    return value

# 함수 사용하기 => 함수 호출
result=addTwo(10, 20)

# 화면에 출력하기 => print(데이터)
print( result )

# ------------------------------------------------------
# 기   능 : 문자 2개 더하는 기능의 함수
# 함 수 명 : minusTwo
# 재     료: num3 num4
# 반     환: 뺄셈

def minusTwo(num3, num4):
    '''

    :param num3:
    :param num4:
    :return:
    '''
    value=num3-num4
    return value

result=minusTwo(50, 15)
print(result)
# ------------------------------------------------------

# ------------------------------------------------------
# 기   능 : 원하는 단의 구구단을 출력하는 기능의 함수
# 함 수 명 : multi
# 재     료: num5
# 반     환: 곱셈


###for n in range(1, 10):
###    print(f'{m} * {n} = {m*n:2d}')

def multi(m):
    for n in range(1, 10):
        print(f'{m} * {n} ={m*n:2d}')
multi(3)


###def gugudan(dan):
  ###for num in [1,2,3,4,5,6,7,8,9]:
      ###print(dan, "x", num, "=", dan*num)
# ------------------------------------------------------
########## 강사님 ##########
# 기 능: 문자 2개 더하는 기능의 함수
# 함수명: addStr
# 재료: data1 data2
# 반환: 더한 결과
# -----------------------------------------------------
def addStr(data1, data2):
    return data1+data2

def addStr(data1, data2):
    result=data1+data2
    return result

## 기 능: 문자 2개 더하는 기능의 함수
# 함수명: addStr
# 재료: data1 data2
# 반환: 더한 결과
def addStr(data1, data2):
    print(data1+data2)
print(addStr('Good', 'Happy'))

#data=addStr('Good','Happy')
#data.upper()
#data.strip

## 기 능: 원하는 단의 구구단을 출력하는 기능의 함수
# 함수명: displayGuGu
# 재료: num
# 반환: 없음
# -----------------------------------------
def displayGuGu(num):
     #2*1=2
    for i in range(1, 10):
        print(f'{num} * {i} = {num*i}')

# ------------------------------------------
## 기 능: 원하는 단의 구구단을 출력하는 기능의 함수
# 함수명: displayGuGu
# 재료: num
# 반환: 구구단 결과
# ------------------------------------------

def addTwo(num1, num2):
    """..."""
    value=num1+num2
    return

def addFive(num1, num2, num3, num4, num5):
    """..."""
    value=num1+num2
    return value

def addTen(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10):
    """..."""
    value=num1+num2+num3+num4+num5+num6+num7+num8+num9+num10
    return value

# 가변인자 함수 => 매개변수 0개 ~ N개
def addNum(*nums):
    print(f'nums type : {type(nums)}')
    total=0
    for num in nums: total = total+num
    return total

# 함수 사용하기 => 함수 호출
result=addTwo(10, 20)
#addTwo(10)
print(addNum(10))
print(addNum(1,1,1,1,1,1,1))
print(addNum())

# 화면에 출력하기 => print(데이터)
print(result)

# ---------------------------------------------
# 기   능: 평균 구하는 함수
# 함수명: getAvg
# 파라미터: 과목명 - 점수 유동적 => **subjects
# 반환값(리턴값): 평균 --- float
# 가변인자 함수 => 매개변수 0개 ~ N개
# ---------------------------------------------
def getAvg(**subjects):
    print(f'subjects type: {type(subjects)}')
    values=subjects.values()
    total=0
    for value in values: total = total + value
    print(f'total => {total}')
    return total / len(values) if len(values)>0 else -1

# 함수 사용하기 => 함수 호출
print(getAvg(국어=12, 영어=98, 수학=88))
print(getAvg(영어=98, 수학=88))
print(getAvg())

print(daaTwo(10))
print(addTwo(10,9))
print(addTwo())

# ------------------------------------------------------
# 함수=(function)의 데이터 타입 => class function
print(type(addTwo()))m\, id(addTwo())

list=addTwo, getAvg

print(list[0(1,2)])
print(List)

