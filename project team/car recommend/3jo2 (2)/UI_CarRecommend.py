import tkinter as tk
from tkinter import *
import Module_SelectCar as sc
import Module_InsuranceCalculator as ic
import Module_taxcal as tc
pro = Tk()
pro.title("자동차추천시스템") #창의 타이틀명
pro.geometry("1000x800") #창의 사이즈
 #창의 사이즈 변경 여부 속성 지정
frame2=tk.Frame(pro)
frame2.grid(row=1,column=1)
frame3 = tk.Frame(pro, bd=2, bg='green')
frame3.grid(row=11,column=1)
def p1():
    global a
    a=txt1.get()
    lbl1.config(text=txt1.get())
def p2():
    global b
    b=txt2.get()
    lbl2.config(text=txt2.get())
def p3():
    global c
    c=txt3.get()
    lbl3.config(text=txt3.get())
def p4():
    global d
    d=txt4.get()
    lbl4.config(text=txt4.get())
def close():
    pro.destroy()
def final():
    ResultViewlabel_ViewLabel.config(text=sc.RecommendCar(txt1.get(), int(txt2.get()), int(txt3.get()), int(txt4.get())))

    def store():
        global top
        searstore = Toplevel(pro)
        searstore.title("자동차 매장 찾기")
        bt1 = tk.Button(searstore, text="클릭", command=close)
        bt1.pack()
        pro.mainloop()
    def insurance():
        def i1():
            global a
            a = insutxt1.get()
            insulbl1.config(text=insutxt1.get())
        def i2():
            global b
            b = insutxt2.get()
            insulbl2.config(text=insutxt2.get())
        def final_insu():
            labinsu.config(text="보험료: %s원" % ic.InsuranceCal(insutxt1.get(),insutxt2.get()))
        Insu=Toplevel(pro)
        Insu.title("보험료 계산")
        Insu.geometry("600x600")  # 창의 사이즈
        Insu.resizable(False, False)  # 창의 사이즈 변경 여부 속성 지정
        insulbl1 = Label(Insu, text="만 나이")
        insulbl1.grid(row=0, column=0)
        insutxt1 = Entry(Insu)
        insutxt1.grid(row=0, column=1)
        insutxt1.bind("<Return>", i1)
        insulbl2 = Label(Insu, text="차량명")
        insulbl2.grid(row=1, column=0)
        insutxt2 = Entry(Insu)
        insutxt2.grid(row=1, column=1)
        insutxt2.bind("<Return>", i2)
        btninsu = tk.Button(Insu, text="계산하기", command=final_insu)
        btninsu.grid(row=2, column=1)
        labinsu = tk.Label(Insu)
        labinsu.grid(row=5, column=1, sticky="w")
        Insu.mainloop()
        pro.mainloop()
    def tax():
        def t1():
            global a
            a = taxtxt1.get()
            taxlbl1.config(text=taxtxt1.get())

        def final_tax():
            if answer1.get()==0:
                labtax.config(text="자동차세: %s원" % (tc.texcal(taxtxt1.get(), answer1.get())))

            elif answer1.get()==1:
                labtax.config(text="자동차세: %s원" % (tc.texcal(taxtxt1.get(), answer1.get())))

            print(answer1.get())

        def retry():
            labtax.config(text="")
            tc.myc1.clear()

        Tax = Toplevel(pro)
        Tax.title("자동차세 계산")
        Tax.geometry("600x600")  # 창의 사이즈
        Tax.resizable(False, False)  # 창의 사이즈 변경 여부 속성 지정
        taxlbl1 = Label(Tax, text="차량명")
        taxlbl1.grid(row=0, column=0)
        taxtxt1 = Entry(Tax)
        taxtxt1.grid(row=0, column=1)
        taxtxt1.bind("<Return>", t1)
        answer1 = tk.IntVar()
        taxtxt2 = tk.Radiobutton(Tax, text="영업용", variable=answer1, value=0)
        taxtxt2.grid(row=1, column=1, sticky="w")
        taxtxt3 = tk.Radiobutton(Tax, text="비영업용", variable=answer1, value=1)
        taxtxt3.grid(row=2, column=1, sticky="w")
        #taxtxt2.bind("<Return>", t2)
        btntax = tk.Button(Tax, text="계산하기", command=final_tax)
        btntax.grid(row=3, column=1)
        btntax2 = tk.Button(Tax, text="다시하기", command=retry)
        btntax2.grid(row=3, column=2)
        labtax = tk.Label(Tax)
        labtax.grid(row=5, column=1, sticky="w")
        Tax.mainloop()
        pro.mainloop()

    btn1 = tk.Button(pro, text="자동차 매장 찾기", command=store)
    btn1.grid(row=7, column=1, sticky="w", padx=10, pady=10)
    btn2 = tk.Button(pro, text="보험료 계산", command=insurance)
    btn2.grid(row=8, column=1, sticky="w", padx=10)
    btn3 = tk.Button(pro, text="자동차세 계산", command=tax)
    btn3.grid(row=9, column=1, sticky="w", padx=10, pady=10)
    btn4 = tk.Button(pro, text="처음으로", command=close)
    btn4.grid(row=10, column=1, sticky="w", padx=10)


lbl1 = Label(frame2, text="이름")
lbl1.grid(row=0, column=0)
txt1 = Entry(frame2)
txt1.grid(row=0, column=1)
txt1.bind("<Return>",p1)
lbl2 = Label(frame2, text="재산(단위:만원)")
lbl2.grid(row=1, column=0)
txt2 = Entry(frame2)
txt2.grid(row=1, column=1)
txt2.bind("<Return>",p2)
lbl3 = Label(frame2, text="월급(단위:만원)")
lbl3.grid(row=2, column=0)
txt3 = Entry(frame2)
txt3.grid(row=2, column=1)
txt3.bind("<Return>",p3)
lbl4 = Label(frame2, text="빚(단위:만원)")
lbl4.grid(row=3, column=0)
txt4 = Entry(frame2)
txt4.grid(row=3, column=1)
txt4.bind("<Return>",p4)
btn = Button(frame2, text="OK", width=15,command=final)
btn.grid(row=4, column=1)
lb5 = tk.Label(pro)
lb5.grid(row=5, column=1, sticky="w")

ResultViewlabel_ViewLabel = tk.Label(frame3, text ="<결과>")
ResultViewlabel_ViewLabel.grid(row=6, column=1, sticky="w")

pro.mainloop()

