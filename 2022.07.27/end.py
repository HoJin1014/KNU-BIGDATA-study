import os, os.path
import time as t
IFM_PATH='./CtmBook/'
menuCost_1 = {'11':5000, '12':4500}
menuCost_2 = {'21':3000, '22':3500}
total = []
def menu_1():
    print("="*7+'머먹조카페에 어서오세요!'+'='*7)
    print(" "*7+'1. 매    장')
    print(" "*7+'2. 테이크아웃')
    print(" "*7+'3. 종    료')
    print('=' * 26)
def menu_2():
    print("="*7+'어떻게 하시겠어요?'+'='*7)
    print(" "*7+'1. 추천메뉴')
    print(" "*7+'2. 직접선택')
    print(" "*7+'3. 이전화면')
    print('=' * 26)
def menu_2_1():
    print("="*7+'추천메뉴를 선택해주세요.'+'='*7)
    print(" "*7+'11. 아메리카노+치즈케이크')
    print(" "*7+'12. 아메리카노+타르트')
    print(" "*7+'3. 주문완료')
    print(" "*7+'4. 이전화면')
    print('=' * 26)
def menu_2_2():
    print("="*7+'메뉴를 선택해주세요.'+'='*7)
    print(" "*7+'21. 아메리카노   3000원')
    print(" "*7+'22. 카페라떼     3500원')
    print(" "*7+'3. 주문완료')
    print(" "*7+'4. 이전화면')
    print('=' * 26)
def menu_3():
    print("="*7+'결제방식을 선택해주세요.'+'='*7)
    print(" "*7+'21. 아메리카노   3000원')
    print(" "*7+'22. 카페라떼     3500원')
    print(" "*7+'3. 이전화면')
    print('=' * 26)
def initApp():
    if not os.path.exists(IFM_PATH): os.mkdir(IFM_PATH)
def addCost_1(num):
#    total=menuCost_1.get(num)
    filename=t.strftime('%Y-%m-%d %A %I:%M:%S')+'.txt'
    #filename = ',' + t.strftime('%Y-%m-%d %A %I:%M:%S') + '.txt'
    # 파일명 리스트 추가
    # CtmBook 폴더에 파일 생성
    with open(IFM_PATH+filename, mode='a', encoding='utf-8') as f:
        f.write(f'{select_3(total)}')
def addCost_2(num):
#    total=menuCost_1
#    2.get(num)
    filename=t.strftime('%Y-%m-%d %A %I:%M:%S')+'.txt'
    #filename = ',' + t.strftime('%Y-%m-%d %A %I:%M:%S') + '.txt'
    # 파일명 리스트 추가
    # CtmBook 폴더에 파일 생성
    with open(IFM_PATH+filename, mode='a', encoding='utf-8') as f:
        f.write(f'{select_3(total)}')
def select_1():
    while True:
        menu_1()
        select = input("어디서 드실건가요?: ")
        if select == '3': break
        elif select == '1':
            select_2()
        elif select == '2':
            select_2()
        else:
            print('<<<잘못 입력하셨어요.>>>')
    print('프로그램을 종료합니다.')
def select_2():
    while True:
        menu_2()
        select = input("어떻게 하시겠어요?: ")
        if select == '3': break
        elif select == '1':
            select_2_1()
        elif select == '2':
            select_2_2()
        else:
            print('<<<잘못 입력하셨어요.>>>')
def select_2_1():
    while True:
        menu_2_1()
        select = input("추천메뉴를 선택해주세요.: ")
        if select == '4': break
        elif select == '11':
            addCost_1(select)
        elif select == '12':
            addCost_1(select)
        elif select == '3':
            print(select_3(total))
            print("주문완료")
            quit()
        else:
            print('<<<잘못 입력하셨어요.>>>')
def select_2_2():
    while True:
        menu_2_2()
        select = input("메뉴를 선택해주세요.: ")
        if select == '4': break
        elif select == '21':
            addCost_2(select)
        elif select == '22':
            addCost_2(select)
        elif select == '3':
            print(select_3(total))
            print("주문완료")
            quit()
        else:
            print('<<<잘못 입력하셨어요.>>>')
def select_3(some_list):
    value = 0
    for list_member in range(len(some_list)):
        value += int(some_list[list_member][1])
    return value
initApp()
select_1()