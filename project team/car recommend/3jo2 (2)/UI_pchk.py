import tkinter as tk
from tkinter import *
import Module_SelectCar as sc
import Module_InsuranceCalculator as ic
import Module_taxcal as tc
import Module_carinputE as ce
from Module_carinputE import *
pro = Tk()
pro.title("자동차견적시스템") #창의 타이틀명
pro.geometry("1400x800") #창의 사이즈
 #창의 사이즈 변경 여부 속성 지정
frame2=tk.Frame(pro)
frame2.grid(row=3,column=1)
frame3 = tk.Frame(pro, bd=4, bg='green')
frame3.grid(row=5,column=1)
frame4 = tk.Frame(pro, bd=4, bg='blue')
frame4.grid(row=0,column=4)
def p1():  #이름
    global a
    a=txt1.get()
    lbl1.config(text=txt1.get())
# def p2(): #배기량
#     global b
#     b=txt2.get()
#     lbl2.config(text=txt2.get())
# def p3(): #연비
#     global c
#     c=txt3.get()
#     lbl3.config(text=txt3.get())
# def p4(): #구매가격
#     global d
#     d=txt4.get()
#     lbl4.config(text=txt4.get())
def p5():  # 사용연식.(단위:일)
    global e
    e=txt5.get()
    lbl5.config(text=txt5.get())
def close():
    pro.destroy()
def final():
    ResultViewlabel_ViewLabel.config(text=ce.taxcal(txt1.get(), int(txt5.get())))

    def matchingp():
        global top
        esw1 = Toplevel(pro)
        esw1.title("견적 출력")
        esw1.geometry("1200x800")  # 창의 사이즈
        esw1.resizable(False, False)  # 창의 사이즈 변경 여부 속성 지정
        frame2 = tk.Frame(esw1, bd=4, bg='green')
        frame2.grid(row=0, column=1)

        frame3 = tk.Frame(esw1, bd=1, bg='blue')
        frame3.grid(row=0, column=2)

        btn4 = tk.Button(esw1, text="모두닫기", command=close)
        btn4.grid(row=10, column=1, sticky="w", padx=10)

        ResultViewlabel_ViewLabel = tk.Label(frame3, text="<결과> %s" % ce.taxcal(txt1.get(), int(txt5.get())))
        ResultViewlabel_ViewLabel.grid(row=0, column=1, sticky="w")

        def p1():  # 이름
            global a
            a = txta1.get()
            lbl1.config(text=txt1.get())

        lbl1 = Label(frame2, text="내 차량명")  #
        lbl1.grid(row=0, column=0)
        txta1 = Entry(frame3)
        txta1.grid(row=0, column=0)
        esw1.mainloop()

    btn1 = tk.Button(pro, text="견적출력", command=matchingp())  #pro창안에 또 세부넣는 키워드.
    btn1.grid(row=1, column=0, sticky="w", padx=10, pady=10)


lbl1 = Label(frame2, text="차량명") #틀만들기
lbl1.grid(row=0, column=0)
txt1 = Entry(frame2)
txt1.grid(row=0, column=1)

lbl5 = Label(frame2, text="사용한 연도 단위(:일)")
lbl5.grid(row=4, column=0)
txt5 = Entry(frame2)
txt5.grid(row=4, column=1)
# txt5.bind("<Return>",p4)

btn = Button(frame2, text="OK", width=15,command=final)
btn.grid(row=5, column=1)
lb5 = tk.Label(pro)
lb5.grid(row=5, column=1, sticky="w")
ResultViewlabel_ViewLabel = tk.Label(frame3, text ="<결과>")
ResultViewlabel_ViewLabel.grid(row=6, column=2, sticky="w")
ResultViewlabel_ViewLabel = tk.Label(frame4, text =ce.cleandata(n1), wraplength=500)
ResultViewlabel_ViewLabel.grid(row=6, column=0, sticky="w")

pro.mainloop()

