import tkinter as tk

price_dessert = {'초코케이크': 5000, '치즈케이크': 5000, '타르트': 4000, '베이글': 3500, '마카롱': 2500}
price_drink = {'에스프레소': 3000, '아메리카노': 3000, '카페라떼': 3500, '카페모카': 4000, '카푸치노': 3500}
price_sat = {'아아,치케':7200, '아아,에이글':5900, '아아,마카롱': 5000, '아아2,치즈케이크':9900, '아아2잔,에이글':8600, '아아2잔,마카롱':7700}


order_dessert = {}
order_drink = {}
order_sat = {}

total_price = 0

def show_dessert():
    btn_dessert.configure(bg="yellow")
    btn_drink.configure(bg="white")
    frame4.pack_forget()
    frame3.pack_forget()
    frame2.pack(fill="both", expand=True)
    frame4.pack(fill="both", expand=True)

def show_drink():
    btn_dessert.configure(bg="white")
    btn_drink.configure(bg="yellow")
    frame4.pack_forget()
    frame2.pack_forget()
    frame3.pack(fill="both", expand=True)
    frame4.pack(fill="both", expand=True)

def show_sat():
    btn_sat.configure(bg="white")
    btn_drink.configure(bg="white")
    frame4.pack_forget()
    frame3.pack_forget()
    frame2.pack(fill="both", expand=True)
    frame4.pack(fill="both", expand=True)

def sat_add(m):
    global price_sat, order_sat, total_price
    if m not in price_sat:
        print("입력한 메뉴가 존재하지 않습니다.")
        # text_1['text'] = "입력한 메뉴가 존재하지 않습니다."
        this_price = price_sat.get(m)
        total_price += this_price

        if m in order_sat:
            order_sat[m] = order_sat.get(m) + 1
        else:
            order_sat[m] = 1
        print_order()
        print_price()

def dessert_add(m):
    global price_dessert, order_dessert, total_price
    if m not in price_dessert:
        print("입력한 메뉴가 존재하지 않습니다.")
        # text_1['text'] = "입력한 메뉴가 존재하지 않습니다."
        this_price = price_dessert.get(m)
        total_price += this_price

        if m in order_dessert:
            order_dessert[m] = order_dessert.get(m) + 1
        else:
            order_dessert[m] = 1
        print_order()
        print_price()

def drink_add(m):
    global price_dessert, order_dessert, total_price
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
    global order_dessert, order_drink, order_sat

    tmp = ""
    for i in order_dessert:
        tmp = tmp + i + " X " + str(order_dessert.get(i)) + "\n"
    for i in order_drink:
        tmp = tmp + i + " X " + str(order_drink.get(i)) + "\n"
    for i in order_sat:
        tmp = tmp + i + " X " + str(order_sat.get(i)) + "\n"

    text_1.delete('1.0', tk.END)
    text_1.insert(tk.INSERT, tmp)

def order_end():
    global total_price, order_dessert, order_drink, order_sat
    total_price = 0
    del order_dessert
    del order_drink
    del order_sat

    order_dessert = {}
    order_drink = {}
    order_sat = {}
    print_price()
    print_order()
    show_dessert()

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

btn_dessert = tk.Button(frame1, text="디저트", padx="10", pady="10", bg="yellow", command=show_dessert)
btn_dessert.grid(row=0, column=0, padx=10, pady=10)

btn_drink = tk.Button(frame1, text="음료", padx="10", pady="10", bg="white", command=show_drink)
btn_drink.grid(row=0, column=1, padx=10, pady=10)

btn_sat = tk.Button(frame1, text="세트메뉴", padx="10", pady="10", bg="blue", command=show_sat)
btn_sat.grid(row=0, column=2, padx=10, pady=10)

btn_end = tk.Button(frame1, text="주문종료", padx="10", command=order_end)
btn_end.grid(row=0, column=3, padx=10, pady=10)

label_price = tk.Label(frame1, text="0 원", width="20", padx=10, pady="10", fg="blue", font='Arial 15')
label_price.grid(row=0, column="4", padx="10", pady="10")

# 디저트
btn_dessert_1 = tk.Button(frame2, text="초코케이크\n(5000원)", padx="10", pady="10", width="10", command=lambda: dessert_add("초코케이크"))
btn_dessert_1.grid(row=0, column=0, padx=0, pady=10)

btn_dessert_2 = tk.Button(frame2, text="치즈케이크\n(5000원)", padx="10", pady="10", width="10", command=lambda: dessert_add('치즈케이크'))
btn_dessert_2.grid(row=0, column=1, padx=0, pady=10)

btn_dessert_3 = tk.Button(frame2, text="타르트\n(4000원)", padx="10", pady="10", width="10", command=lambda: dessert_add('타르트'))
btn_dessert_3.grid(row=0, column=2, padx=0, pady=10)

btn_dessert_4 = tk.Button(frame2, text="베이글\n(3500원)", padx="10", pady="10", width="10", command=lambda: dessert_add('베이글'))
btn_dessert_4.grid(row=0, column=3, padx=0, pady=10)

btn_dessert_5 = tk.Button(frame2, text="마카롱\n(2500원)", padx="10", pady="10", width="10", command=lambda: dessert_add('마카롱'))
btn_dessert_5.grid(row=0, column=4, padx=0, pady=10)

# 음료
btn_drink_1 = tk.Button(frame3, text="에스프레소\n(3000원)", padx="10", pady="10", width="10", command=lambda: drink_add('에스프레소'))
btn_drink_1.grid(row=0, column=0, padx=0, pady=10)

btn_drink_2 = tk.Button(frame3, text="아메리카노\n(3500원)", padx="10", pady="10", width="10", command=lambda: drink_add('아메리카노'))
btn_drink_2.grid(row=0, column=1, padx=0, pady=10)

btn_drink_3 = tk.Button(frame3, text="카페라떼\n(4000원)", padx="10", pady="10", width="10", command=lambda: drink_add('카페라떼'))
btn_drink_3.grid(row=0, column=2, padx=0, pady=10)

btn_drink_4 = tk.Button(frame3, text="카페모카\n(4500원)", padx="10", pady="10", width="10", command=lambda: drink_add('카페모카'))
btn_drink_4.grid(row=0, column=3, padx=0, pady=10)

btn_drink_5 = tk.Button(frame3, text="카푸치노\n(5000원)", padx="10", pady="10", width="10", command=lambda: drink_add('카푸치노'))
btn_drink_5.grid(row=0, column=4, padx=0, pady=10)

# 세트
btn_sat_1 = tk.Button(frame4, text="아아,치즈케이크\n(7200원)", padx="10", pady="10", width="10", command=lambda: sat_add('아아,치즈케이크'))
btn_sat_1.grid(row=0, column=0, padx=0, pady=10)

btn_sat_2 = tk.Button(frame4, text="아아,베이글\n(5900원)", padx="10", pady="10", width="10", command=lambda: sat_add('아아,베이글'))
btn_sat_2.grid(row=0, column=1, padx=0, pady=10)

btn_sat_3 = tk.Button(frame4, text="아아,마카롱\n(5000원)", padx="10", pady="10", width="10", command=lambda: sat_add('아아,마카롱'))
btn_sat_3.grid(row=0, column=2, padx=0, pady=10)

btn_sat_4 = tk.Button(frame4, text="아아2,치즈케이크\n(9900원)", padx="10", pady="10", width="10", command=lambda: sat_add('아아2,치즈케이크'))
btn_sat_4.grid(row=0, column=3, padx=0, pady=10)

btn_sat_5 = tk.Button(frame4, text="아아2,에이글\n(8600원)", padx="10", pady="10", width="10", command=lambda: sat_add('아아2,에이글'))
btn_sat_5.grid(row=0, column=4, padx=0, pady=10)

btn_sat_6 = tk.Button(frame4, text="아아2,마카롱\n(7700원)", padx="10", pady="10", width="10", command=lambda: sat_add('아아2,마카롱'))
btn_sat_6.grid(row=0, column=5, padx=0, pady=10)


# 주문 리스트
text_1 =tk.Text(frame4, height="10")
text_1.pack()

window.mainloop()