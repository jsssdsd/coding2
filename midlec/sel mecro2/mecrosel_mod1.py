
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
