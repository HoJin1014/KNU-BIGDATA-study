price1 = 8700
price2 = 6200
price3 = 1500

print("=== 롯데리아 ===")
print("1.불고기 버거 :", price1)
print("2.새우   버거 :", price2)
print("3.콜       라 :", price3)

cnt1 = 0
cnt2 = 0
cnt3 = 0

i = 1
while i <= 5:
    choice = int(input("메뉴를 선택하세요 : "))

    if choice == 1:
        cnt1 = cnt1 + 1
    elif choice == 2:
        cnt2 = cnt2 + 1
    elif choice == 3:
        cnt3 = cnt3 + 1

    i = i + 1

total = cnt1*price1 + cnt2*price2 + cnt3*price3
print("총 금액 =", total)

my_money = int(input("돈을 입력하세요 : "))

charge = my_money - total
if charge < 0:
    print("현금이 부족합니다.")
else:
    print("=== 롯데리아 영수증===")
    print("1.불고기 버거 :", cnt1)
    print("2.새우   버거 :", cnt2)
    print("3.콜       라 :", cnt3)
    print("총 금액 =", total)
    print("잔돈 =", charge)