import tkinter
win= tkinter.Tk()

menuBtn = tkinter.Menubutton(win, text='Menubutton')
menuBtn.pack()


menu = tkinter.Menu(menuBtn, tearoff=0)
menu.add_command(label='menu1')
menu.add_command(label='menu2')
menu.add_command(label='menu3')





menuBtn['menu']=menu



win.mainloop()