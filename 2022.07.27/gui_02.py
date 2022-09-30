# 예시 2
import tkinter as tk

price_meal = {'초코케이크': 5000, '치즈케이크': 5000, '타르트': 4000, '베이글': 3500, '마카롱': 2500}
price_drink = {'에스프레소': 3000, '아메리카노': 3000, '카페라떼': 3500, '카페모카': 4000, '카푸치노': 3500}

order_meal = {}
order_drink = {}

total_price = 0


def show_meal():
    btn_meal.configure(bg="yellow")
    btn_drink.configure(bg="white")
    frame4.pack_forget()
    frame3.pack_forget()
    frame2.pack(fill="both", expand=True)
    frame4.pack(fill="both", expand=True)

def show_drink():
    btn_meal.configure(bg="white")
    btn_drink.configure(bg="yellow")
    frame4.pack_forget()
    frame2.pack_forget()
    frame3.pack(fill="both", expand=True)
    frame4.pack(fill="both", expand=True)

def meal_add(m):
    global price_meal, order_meal, total_price
    if m not in price_meal:
        print("입력한 메뉴가 존재하지 않습니다.")
        # text_1['text'] = "입력한 메뉴가 존재하지 않습니다."
        this_price = price_meal.get(m)
        total_price += this_price

        if m in order_meal:
            order_meal[m] = order_meal.get(m) + 1
        else:
            order_meal[m] = 1
        print_order()
        print_price()

def drink_add(m):
    global price_meal, order_meal, total_price
    if m not in price_drink:
        print("입력한 메뉴가 존재하지 않습니다.")
        # text_1['text] = "입력한 메뉴가 존재하지 않습니다."
    this_price = price_drink.get(m)
    total_price += this_price

    if m in order_drink:
        order_drink[m] = order_drink.get(m) + 1
    else:
        order_drink[m] = 1
    print_order()
    print_price()

def print_order():
    global order_meal, order_drink

    tmp = ""
    for i in order_meal:
        tmp = tmp + i + " X " + str(order_meal.get(i)) + "\n"
    for i in order_drink:
        tmp = tmp + i + " X " + str(order_drink.get(i)) + "\n"

    text_1.delete('1.0', tk.END)
    text_1.insert(tk.INSERT, tmp)

def order_end():
    global total_price, order_meal, order_drink
    total_price = 0
    del order_meal
    del order_drink

    order_meal = {}
    order_drink = {}
    print_price()
    print_order()
    show_meal()

def print_price():
    global total_price
    label_price.configure(text=str(total_price)+" 원")


window = tk.Tk()
window.title("주문 프로그램")
window.geometry("700x400+400+200")
window.resizable(False, False)

frame1 = tk.Frame(window, width="600", height="10")
frame1.pack(fill="both")

frame2 = tk.Frame(window, width="600") #height="10")
frame2.pack(fill="both", expand=True)

frame3 = tk.Frame(window, width="600", height="10")
#frame2.pack(fill="both", expand=True)

frame4 = tk.Frame(window, width="600", height="10")
frame4.pack(fill="both", expand=True)

frame5 = tk.Frame(window, width="600", height="10")
frame5.pack(fill="both", expand=True)

btn_meal = tk.Button(frame1, text="식사", padx="10", pady="10", bg="yellow", command=show_meal)
btn_meal.grid(row=0, column=0, padx=10, pady=10)

btn_drink = tk.Button(frame1, text="음료", padx="10", pady="10", bg="white", command=show_drink)
btn_drink.grid(row=0, column=1, padx=10, pady=10)

btn_end = tk.Button(frame1, text="주문종료", padx="10", command=order_end)
btn_end.grid(row=0, column=2, padx=10, pady=10)

label_price = tk.Label(frame1, text="0 원", width="20", padx=10, pady="10", fg="blue", font='Arial 15')
label_price.grid(row=0, column="3", padx="10", pady="10")

# 식사
btn_meal_1 = tk.Button(frame2, text="초코케이크\n(5000원)", padx="10", pady="10", width="10", command=lambda: meal_add("초코케이크"))
btn_meal_1.grid(row=0, column=0, padx=0, pady=10)

btn_meal_2 = tk.Button(frame2, text="치즈케이크\n(5000원)", padx="10", pady="10", width="10", command=lambda: meal_add('치즈케이크'))
btn_meal_2.grid(row=0, column=1, padx=0, pady=10)

btn_meal_3 = tk.Button(frame2, text="타르트\n(4000원)", padx="10", pady="10", width="10", command=lambda: meal_add('타르트'))
btn_meal_3.grid(row=0, column=2, padx=0, pady=10)

btn_meal_4 = tk.Button(frame2, text="베이글\n(3500원)", padx="10", pady="10", width="10", command=lambda: meal_add('베이글'))
btn_meal_4.grid(row=0, column=3, padx=0, pady=10)

btn_meal_5 = tk.Button(frame2, text="마카롱\n(2500원)", padx="10", pady="10", width="10", command=lambda: meal_add('마카롱'))
btn_meal_5.grid(row=0, column=4, padx=0, pady=10)

# 음료
btn_drink_1 = tk.Button(frame3, text="에스프레소\n(3000원)", padx="10", pady="10", width="10", command=lambda: drink_add('에스프레소'))
btn_drink_1.grid(row=0, column=0, padx=0, pady=10)

btn_drink_2 = tk.Button(frame3, text="아메리카노\n(3000원)", padx="10", pady="10", width="10", command=lambda: drink_add('아메리카노'))
btn_drink_2.grid(row=0, column=1, padx=0, pady=10)

btn_drink_3 = tk.Button(frame3, text="카페라떼\n(3500원)", padx="10", pady="10", width="10", command=lambda: drink_add('카페라떼'))
btn_drink_3.grid(row=0, column=2, padx=0, pady=10)

btn_drink_4 = tk.Button(frame3, text="카페모카\n(4000원)", padx="10", pady="10", width="10", command=lambda: drink_add('카페모카'))
btn_drink_4.grid(row=0, column=3, padx=0, pady=10)

btn_drink_5 = tk.Button(frame3, text="카푸치노\n(3500원)", padx="10", pady="10", width="10", command=lambda: drink_add('카푸치노'))
btn_drink_5.grid(row=0, column=4, padx=0, pady=10)

# 주문 리스트
text_1 =tk.Text(frame4, height="10")
text_1.pack()

window.mainloop()