menu = {"아메리카노": 2000, "카페라떼": 2500, "그린티 라떼": 3000, "모카 라떼": 3500}

menu_name = ', '.join(list(menu.keys()))
print('Menu : ', menu_name)

order = input('메뉴에서 주문 : ')

if order in menu.keys():
    print(menu[order])

else:
    print("메뉴에 없습니다.")