# X 실패
import tkinter as tk
from tkinter import messagebox
#from openpyxl import load_workbook
from datetime import datetime

price = {'에스프레소': 3000, '아메리카노': 3000, '카페라떼': 3500, '카페모카': 4000, '카푸치노': 3500}
price1 = {'초코케이크': 5000, '치즈케이크': 5000, '타르트': 4000, '베이글': 3500, '마카롱': 2500}


order = []
order2 = {'에스프레소': 0, '아메리카노': 0, '카페라떼': 0, '카페모카': 0, '카푸치노':0}
order3 = {'초코케이크': 0, '치즈케이크': 0, '타르트': 0, '베이글': 0, '마카롱': 0} #
sum = 0


def clear():
    global sum, order, order2, order3, textarea, entry1, entry2
    textarea.delete('1.0', tk.END)
    label1['text'] = "금액: 0원"
    sum = 0
    order = []
    order2 = {'에스프레소': 0, '아메리카노': 0, '카페라떼': 0, '카페모카': 0, '카푸치노':0}
    order3 = {'초코케이크': 0, '치즈케이크': 0, '타르트': 0, '베이글': 0, '마카롱': 0}
    entry1.delete('0', tk.END)
    entry2.delete('0', tk.END)
    entry1.focus()
    entry2.focus()  #

def add(item):
    global sum

    if item not in price:
        print("no drink")
    this_price = price.get(item)
    sum += this_price
    order.append(item)
    order2[item] += 1
    order3[item] += 1  # 추가
    textarea.insert(tk.INSERT, item+" ")
    label1['text'] = "금액: " + str(sum) + "원"

def send():
    global order, order2,order3, sum, entry1, entry2
    name = str(entry1.get())
    hp = str(entry2.get())
    print(name, hp)
    print(order)
    print(order2)
    print(order3)    # 추가

    now_dt = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    #wb = load_workbook("drink_order.xlsx")
    ws = wb['Sheet1']
    ws.append([now_dt, name, hp, order2['에스프레소'], order2['아메리카노'], order2['카페라떼'], order2['카푸치노'],order3['초코케이크'], order3['치즈케이크'], order3['타르트'], order3['베이글'], order3['마카롱'],sum]) #
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
window.title("음료 주문")
window.geometry("550x600")

frame1 = tk.Frame(window)
frame1.pack()

frame2 = tk.Frame(window)
frame2.pack()

frame3 = tk.Frame(window) #
frame3.pack() #

btn_1 = tk.Button(frame2, text="에스프레소", command=lambda: add('에스프레소'), width=10, height=2)
btn_2 = tk.Button(frame2, text="아메리카노", command=lambda: add('아메리카노'), width=10, height=2)
btn_3 = tk.Button(frame2, text="카페라떼", command=lambda: add('카페라떼'), width=10, height=2)
btn_4 = tk.Button(frame2, text="카페모카", command=lambda: add('카페모카'), width=10, height=2)
btn_5 = tk.Button(frame2, text="카푸치노", command=lambda: add('카푸치노'), width=10, height=2)
btn_6 = tk.Button(frame3, text="초코케이크", command=lambda: add('초코케이크'), width=10, height=2) #
btn_7 = tk.Button(frame3, text="치즈케이크", command=lambda: add('치즈케이크'), width=10, height=2) #
btn_8 = tk.Button(frame3, text="타르트", command=lambda: add('타르트'), width=10, height=2) #
btn_9 = tk.Button(frame3, text="베이글", command=lambda: add('베이글'), width=10, height=2) #
btn_10 = tk.Button(frame3, text="마카롱", command=lambda: add('마카롱'), width=10, height=2) #
btn_11 = tk.Button(frame3, text="주문완료", command=btn_exit, width=10, height=2) #

btn_1.grid(row=0, column=0, padx=10, pady=10)
btn_2.grid(row=0, column=1, padx=10, pady=10)
btn_3.grid(row=0, column=2, padx=10, pady=10)
btn_4.grid(row=0, column=3, padx=10, pady=10)
btn_5.grid(row=0, column=4, padx=10, pady=10)
btn_6.grid(row=1, column=5, padx=10, pady=10)
btn_7.grid(row=1, column=6, padx=10, pady=10)
btn_8.grid(row=1, column=7, padx=10, pady=10)
btn_9.grid(row=1, column=8, padx=10, pady=10)
btn_10.grid(row=1, column=9, padx=10, pady=10)
btn_11.grid(row=2, column=0, padx=10, pady=10)


frame3 = tk.Frame(window)     #
frame3.pack()                 #

label2 = tk.Label(frame5, text="이름", width=10, height=2).grid(row=3, column=0)     #
label3 = tk.Label(frame5, text="휴대폰번호", width=10, height=2).grid(row=3, column=0)   # frame2

entry1 = tk.Entry(frame2)
entry2 = tk.Entry(frame2)
entry3 = tk.Entry(frame2) #
entry1.grid(row=1, column=2)
entry2.grid(row=1, column=2) #
entry3.grid(row=2, column=2) #


label1 = tk.Label(window, text="금액: 0원", width=100, height=2, fg="blue")
label1.pack()

textarea = tk.Text(window)
textarea.pack(padx=10, pady=10)

window.mainloop()