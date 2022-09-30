# ----------------------------------------------------------
# EXCEPTION Handling : 예외처리
# 프로그램 실행 시 발생하는 오류(Error)에 대한 처리
# 오류가 발생해도 프로그램 중단하지 않고 실행될 수 있도록 하는 것
# ----------------------------------------------------------

try:
    num1, num2=10,0

    print(f'{num1}/{num2} = {num1/num2}')

except ZeroDivisionError as e:
    print("0으로 나눌 수 없음")

except Exception as ex :
    print("에러발생 ", ex)
    # pass
finally:
    # 오류 발생 여부 상관없음
    # 무조건 실행
    print('finally~~~')


print("END")

try:
    file=open('agaga.jpg', modef='r')
    print(file.read())
    file.close()
except Exception as e:
    print(f'Error 발생 : {e}')

### 파일 있는지 확인
import os

if os.path.exists('agag.jpg'):
    file=open('agaga.jpg', mode='r')
    print(file.read())
    file.close()
else:
    print('없는 파일입니다.')