menu = {
    '에스프레소':3000,
    '아메리카노':3000,
    '카페 라떼':3500,
    '카푸치노':3500,
    '카페 모카':4000
}

for key in menu:
    print('{:<1}가격 : {}원'.format(key,menu[key]))

order = input('위의 메뉴중 하나를 선택하세요:')
if order in menu:
    print('{}는 {}원 입니다. 결제를 부탁합니다.'.format(order,menu[order]))
else:
    print('미안합니다. {}는 메뉴에 없습니다.'.format(order))
