import tkinter as tk
from tkinter import StringVar
import random
import sys
gui = tk.Tk()
money = 1000
var = StringVar()
var.set('开始了')
var1 = StringVar()
var1.set('')
gui.title('赌大小')
gui.geometry('600x200')
def big():
    global money
    gresult = rand()
    #print(gresult)
    if gresult == 'big' :
        #print(11111)
        money = money + 1000
        remain = '你赢了，还剩'+str(money)
        var.set(remain)
    else:
        #print(22222)
        money = money - 500
        remain = '你输了，还剩'+str(money)
        var.set(remain)
        if money <= 0:
            var.set('钱不够了！')
            #sys.exit(3)
            startbtn.pack(padx=10, pady=10)
            info1.pack_forget()
            b.pack_forget()
            s.pack_forget()

def small():
    global money
    gresult = rand()
    if gresult == 'small' :
        money = money + 1000
        remain = '你赢了，还剩' + str(money)
        var.set(remain)
    else:
        money = money - 500
        remain = '你输了，还剩' + str(money)
        var.set(remain)
        if money <= 0:
            var.set('钱不够了！')
            #sys.exit(3)
            startbtn.pack(padx=10, pady=10)
            info1.pack_forget()
            b.pack_forget()
            s.pack_forget()

def dice():
    result = random.randrange(1,7)
    return result

def rand():
    result = dice()
    global gui
    if 0<result<4 :
        much = '本次'+str(result)+'为小'
        var1.set(much)
        info1.pack()
        return 'small'
    else :
        much = '本次'+str(result)+'为大'
        var1.set(much)
        info1.pack()
        return 'big'

def restart():
    #print(333)
    global money
    money = 1000
    var.set('开始了')
    startbtn.pack_forget()
    info.pack()
    b.pack(side="left", padx=10, pady=10, anchor="se")
    s.pack(side="right", padx=10, pady=10, anchor="sw")

info=tk.Label(gui,textvariable=var,width = 30,height = 3 )
info1=tk.Label(gui,textvariable=var1,width = 30,height = 3 )
b=tk.Button(gui,text="大",width =20,height = 2,command=big)
s=tk.Button(gui,text="小",width =20,height = 2,command=small)
startbtn = tk.Button(gui, text="重新开始", width=20, height=2, command=restart)
b.pack(side="left", padx=10, pady=10, anchor="se")
s.pack(side="right", padx=10, pady=10, anchor="sw")
info.pack()
info1.pack()
gui.mainloop()