# 다시 예비

import tkinter as tk
from tkinter import messagebox
#from openpyxl import load_workbook
from datetime import datetime

price = {'에스프레소': 3000, '아메리카노': 3000, '카페라떼': 3500, '카페모카': 4000, '카푸치노': 3500, '초코케이크': 5000, '치즈케이크': 5000, '타르트':4000, '베이글':3500, '마카롱':2500}

order = []
order2 = {'에스프레소': 0, '아메리카노': 0, '카페라떼': 0, '카페모카': 0, '카푸치노':0, '초코케이크': 0, '치즈케이크': 0, '타르트':0, '베이글':0, '마카롱':0}
sum = 0


def clear():
    global sum, order, order2, textarea, entry1, entry2               # order+order2     ,
    textarea.delete('1.0', tk.END)
    label1['text'] = "금액: 0원"
    sum = 0
    order = []
    order2 = {'에스프레소': 0, '아메리카노': 0, '카페라떼': 0, '카페모카': 0, '카푸치노':0, '초코케이크': 0, '치즈케이크': 0, '타르트':0, '베이글':0, '마카롱':0}
    entry1.delete('0', tk.END)
    entry2.delete('0', tk.END)
    entry1.focus()

def add(item):
    global sum

    if item not in price:
        print("no drink")
    this_price = price.get(item)
    sum += this_price
    order.append(item)
    order2[item] += 1
    textarea.insert(tk.INSERT, item+" ")
    label1['text'] = "금액: " + str(sum) + "원"

def send():
    global order, order2, sum, entry1, entry2
    name = str(entry1.get())
    hp = str(entry2.get())
    print(name, hp)
    print(order)
    print(order2)

    now_dt = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    wb = load_workbook("drink_order.xlsx")
    ws = wb['Sheet1']
    ws.append([now_dt, name, hp, order2['coffee'], order2['latte'], order2['smoothie'], order2['tea'], sum])
    wb.save("drink_order.xlsx")

    clear()


def btn_exit():
    name = str(entry1.get())
    hp = str(entry2.get())

    if name == "":
        tk.messagebox.showerror("확인", "이름을 입력해주세요!")
        entry1.focus()
        return
    if hp == "":
        tk.messagebox.showerror("확인", "휴대폰번호를 입력해주세요!")
        entry2.focus()
        return

    msgbox = tk.messagebox.askquestion('확인', '주문을 마치시겠습니까?')
    if msgbox == 'yes':
        send()


window = tk.Tk()
window.title("머먹조 카페 키오스크 주문")
window.geometry("1000x700")

frame1 = tk.Frame(window)
frame1.pack()

btn_1 = tk.Button(frame1, text="에스프레소", command=lambda: add('에스프레소'), width=10, height=2)
btn_2 = tk.Button(frame1, text="아메리카노", command=lambda: add('아메리카노'), width=10, height=2)
btn_3 = tk.Button(frame1, text="카페라떼", command=lambda: add('카페라떼'), width=10, height=2)
btn_4 = tk.Button(frame1, text="카페모카", command=lambda: add('카페모카'), width=10, height=2)
btn_5 = tk.Button(frame1, text="카푸치노", command=lambda: add('카푸치노'), width=10, height=2)
btn_6 = tk.Button(frame1, text="초코케이크", command=lambda: add('초코케이크'), width=10, height=2)
btn_7 = tk.Button(frame1, text="치즈케이크", command=lambda: add('치즈케이크'), width=10, height=2)
btn_8 = tk.Button(frame1, text="타르트", command=lambda: add('타르트'), width=10, height=2)
btn_9 = tk.Button(frame1, text="베이글", command=lambda: add('베이글'), width=10, height=2)
btn_10 = tk.Button(frame1, text="마카롱", command=lambda: add('마카롱'), width=10, height=2)
btn_11 = tk.Button(frame1, text="주문완료", command=btn_exit, width=10, height=2)


btn_1.grid(row=0, column=0, padx=10, pady=10)
btn_2.grid(row=0, column=1, padx=10, pady=10)
btn_3.grid(row=0, column=2, padx=10, pady=10)
btn_4.grid(row=0, column=3, padx=10, pady=10)
btn_5.grid(row=0, column=4, padx=10, pady=10)
btn_6.grid(row=0, column=5, padx=10, pady=10)
btn_7.grid(row=0, column=6, padx=10, pady=10)
btn_8.grid(row=0, column=7, padx=10, pady=10)
btn_9.grid(row=0, column=8, padx=10, pady=10)
btn_10.grid(row=0, column=9, padx=10, pady=10)
btn_11.grid(row=1, column=0, padx=10, pady=10)

frame2 = tk.Frame(window)
frame2.pack()

frame3 = tk.Frame(window)
frame3.pack()

label2 = tk.Label(frame3, text="이름", width=10, height=2).grid(row=5, column=0)                       # row 참조
label3 = tk.Label(frame3, text="휴대폰번호", width=10, height=2).grid(row=6, column=0)                  # row 참조

entry1 = tk.Entry(frame3)
entry2 = tk.Entry(frame3)
entry1.grid(row=5, column=1)
entry2.grid(row=6, column=1)

label1 = tk.Label(window, text="금액: 0원", width=100, height=2, fg="blue")
label1.pack()

textarea = tk.Text(window)
textarea.pack(padx=10, pady=10)

window.mainloop()