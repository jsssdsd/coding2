
import tkinter as tk
from tkinter import *
from functools import partial
import webbrowser
from PIL import Image, ImageTk
from itertools import count, cycle
from  selenium import webdriver
import time as t
# 시작모듈

# x= webdriver.Chrome("chromedriver.exe")

# def start(mode,url):
#
#     if mode=="시작":
#         x.get(url)
#     if mode =="시간":
#         t.sleep(a)
# /mecrosel/molecule.png
win = Tk()
win.title('3조 매크로')
ICON=PhotoImage(file="molecule.png")
win.iconphoto(True, ICON)
win.geometry("640x478") #창의 사이즈
win.resizable(False,False) #창의 사이즈 변경 여부 속성 지정\
framefirst=Frame(win)
framefirst.pack()
framesecond=Frame(win)
framesecond.pack()

w1 = Label(win, text="좌표입력")
w1.pack()
insutxt1 = Entry(win)
insutxt1.pack()
# btninsu = tk.Button(win, text="계산하기", command=final_insu)
# btninsu.grid(row=1, column=1)
# labinsu = tk.Label(win)
# labinsu.grid(row=2, column=1, sticky="w")
# smlb1 = Label(win, text="<할증료 부과 기준>")
# smlb1.grid(row=0, column=2)
# smlb2 = Label(win, text="만 24세 ~ 만 26세 : 할증률 30% 부과")
# smlb2.grid(row=1, column=2)
# smlb3 = Label(win, text="만 24세 미만 : 할증률 80% 부과")
# smlb3.grid(row=2, column=2)
win.mainloop()
#
# def callback(url):
#     webbrowser.open_new_tab(url)
#
# def close1():
#     pro.destroy()
#
# def nextpage1():
#     global pro
#     pro = Toplevel(win)
#     pro.title("메크로2")  # 창의 타이틀명
#     pro.geometry("500x800")  # 창의 사이즈
#     framehigh=tk.Frame(pro)
#     framehigh.pack()
#     frame2 = tk.Frame(framehigh)
#     frame2.pack()
#     def exit_window_x():
#         close1()
#     pro.protocol('WM_DELETE_WINDOW', exit_window_x)
#
# btn1 = tk.Button(framefirst, width=25, height=10, text="차량 추천", font=("bold", 10, "bold"), fg="midnightblue",
#                  bg="lightblue", command=nextpage1)

# btn1.grid(row=3, column=3)
# btn2 = tk.Button(framefirst, width=25, height=10, text="내차 견적", font=("bold", 10, "bold"), fg="darkslategrey",
#                  bg="mediumaquamarine", command=nextpage2)
# btn2.grid(row=3, column=4)
# btn3 = tk.Button(framefirst, width=25, height=10, text="운전성향 테스트", font=("bold", 10, "bold"), fg="white",
#                  bg="cadetblue", command=nextpage3)
# btn3.grid(row=3, column=5)
# btn4 = tk.Button(framefirst, width=25, height=10, text="나만의 차 만들기", font=("bold", 10, "bold"), fg="indigo",
#                  bg="thistle", command=nextpage4)
# btn4.grid(row=3, column=6)

    # def p1():
    #     global a
    #     a = txt1.get()
    #     lbl1.config(text=txt1.get())
    #
    # def p2():
    #     global b
    #     b = txt2.get()
    #     lbl2.config(text=txt2.get())
    #
    # def p3():
    #     global c
    #     c = txt3.get()
    #     lbl3.config(text=txt3.get())
    #
    # def p4():
    #     global d
    #     d = txt4.get()
    #     lbl4.config(text=txt4.get())
    #
    # def close():
    #     pro.destroy()