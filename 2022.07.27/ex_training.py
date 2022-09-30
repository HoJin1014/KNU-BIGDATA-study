
coffe_price=0
order=input("커피 종류를 선택하세요. 번호 입력")

if order==1:
    coffe_price=1800
elif order==2:
    coffe_price=2700
elif order==3:
    coffe_price=2300

cups=int(input("몇 잔을 드릴까요?"))
total_price=coffe_price*cups

received=int(input(f"총 금액은 {total_price}원 입니다. 돈을 투입해 주세요." ))

if received >= total_price:
    change=received-total_price
    print(f"{received}원을 받았습니다. 거스름돈은 {change}원입니다.")

else:
    print("금액이 부족합니다. 주문이 취소되었습니다.")
