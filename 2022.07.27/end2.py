import time as t
from menu import *
from point import *

menuPrice={'1':3000,'2':3000,'3':3500,'4':4000,'5':3500,'6':5000,'7':5000,'8':4000,'9':3500,'10':2500,
           '11':7200,'12':5800,'13':4900,'14':9900,'15':8500,'16':7600}
menuName={'1':'에스프레소','2':'아메리카노','3':'카페라떼','4':'카페모카','5':'카푸치노',
          '6':'초코케이크','7':'치즈케이크','8':'타르트(에그/치즈)','9':'베이글','10':'마카롱(딸기/녹차/초코)',
          '11':'1인세트 아메리카노+치즈케이크','12':'1인세트 아메리카노+베이글','13':'1인세트 아메리카노+마카롱',
          '14':'2인세트 아메리카노2+치즈케이크','15':'2인세트 아메리카노2+베이글','16':'2인세트 아메리카노2+마카롱'}
#딕셔너리로 저장

def selectMenu1():#매장에서 먹을지 포장할지 선택하는 함수
    while True:
        menu_1()
        select=input('번호 선택: ')
        if select=='A': selectMenu2()
        elif select=='B': selectMenu2()
        elif select=='C': quit()
        else: print('잘못된 접근입니다.')

def selectMenu2():#음료나 디저트 선택하는 함수
    while True:
        menu_2()
        select=input('번호 선택: ')
        if select=='A': selectMenu3()
        elif select=='B': selectMenu1()
        elif select=='C': quit()
        else: print('잘못된 접근입니다.')

def selectMenu3():#메뉴 선택해서 리스트에 저장하는 함수
    total=0
    name=[]
    price=[]
    point=0
    count=[]
    while True:
        menu_3()
        i=1
        select=input('주문할 메뉴 선택: ')
        if select=='A': selectMenu2()
        elif select=='B': quit()
        elif select=='C':
            point=int(total)*0.05#포인트 5% 적립
            pointAdd(int(point))
            receipt(name,price,total,point,count)#영수증 출력 함수
            quit()
        elif int(select)>0 and int(select)<17:
            count.append(i)
            total=total+menuPrice.get(select)#총 가격
            price.append(menuPrice.get(select))#각자 가격
            name.append(menuName.get(select))#각자 메뉴
            i+=1

# def selectMenu4():
#     select=input('회원이신가요? [Y/N] ')
#     if select=='Y':
#         selectMenu2()
#     elif select=='N':
#         quit()

def receipt(n,p,r,pp,c):#메뉴 이름, 가격, 총합, 포인트, 개수
    t.sleep(0.8)#한줄당 0.8초씩 출력
    print('\n[RECEIPT]')
    t.sleep(0.8)
    print('-'*9,'먹어조 CAFE','-'*9)
    t.sleep(0.8)
    print('결제수단: 카드 결제')
    t.sleep(0.8)
    print('-'*30)
    i=0
    while i<len(n):
        t.sleep(0.8)
        print(n[i],c[i],' ',p[i])#메뉴 이름, 개수, 가격 출력
        i+=1
    t.sleep(0.8)
    print('-'*30)
    t.sleep(0.8)
    print('{0:>24}'.format('total:'),r)#총합 출력
    t.sleep(0.8)
    print('{0:>24}'.format('point:'),int(pp))#포인트 출력

selectMenu1()