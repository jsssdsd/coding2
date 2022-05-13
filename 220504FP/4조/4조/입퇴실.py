import os
import tkinter.scrolledtext
from tkinter import *
import tkinter.font
import module

import requests
from tkinter import messagebox
import tkinter.ttk
import time
import bs4
import random
import module as m
import datetime as dt



root4 = Tk()
root4.title("출석 관리")
root4.geometry("400x300")
root4.resizable(True, True)

notebook = tkinter.ttk.Notebook(root4, width=300, height=300)
notebook.pack(expand=True, fill=BOTH)
framei = Frame(root4)
framei.pack(fill=BOTH, expand=True)
notebook.add(framei, text="입/퇴실 체크")

label_framei2 = Frame(framei)
label_framei2.pack(side=TOP)
labeli2 = Label(label_framei2)
labeli2.pack(side=BOTTOM, expand=True)
labeli = Label(label_framei2)
labeli.pack(side=BOTTOM, expand=True)

import datetime as dt

today = dt.datetime.today().strftime("%Y-%m-%d")
present = dt.datetime.today().strftime("%H:%M")
weekdays = ['(일)', '(월)', '(화)', '(수)', '(목)', '(금)', '(토)']
result = dt.datetime.today().strftime("%Y-%m-%d") + weekdays[int(dt.datetime.today().strftime("%w"))]
dd = result[2:]
def i():

    with open('./userlist/' + '최수정7652' + '.txt', 'r', encoding='UTF-8') as user:
        line = user.readlines()
        if dd not in line:
            checkin = open('./userlist/' + '최수정7652' + '.txt', 'a', encoding='UTF-8')
            checkin.writelines(dd + '\t' + present)
            checkin.close()
            labeli.configure(text='입실 시간 : ' + str(present))
        else:
            messagebox.showwarning('경고', '오늘 입실 이력이 있습니다.')



def o():
    from datetime import datetime
    dt = datetime.now()
    a=0
    with open('./userlist/' + '최수정7652' + '.txt', 'r', encoding='UTF-8') as user:
        line = user.readlines()

        if dd in line:
            checkout = open('./userlist/' + '최수정7652' + '.txt', 'a', encoding='UTF-8')
            checkout.writelines('-' + present + '\n')
            checkout.close()
            labeli2.configure(text='퇴실 시간 : ' + str(present))

        elif dd not in line:
            messagebox.showwarning('경고', '이미 퇴실 처리 되었습니다.')


label_framei = LabelFrame(framei)
label_framei.pack()
btn_i = Button(label_framei, text='입실', relief='flat', command=i)
btn_i.pack(side='left', fill='both', padx=5, pady=1)
btn_o = Button(label_framei, text='퇴실', relief='flat', command=o)
btn_o.pack(side='left', fill='both', padx=5, pady=1)




root4.mainloop()