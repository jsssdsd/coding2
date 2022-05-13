import tkinter as tk
from tkinter import *
import Module_SelectCar as sc
import Module_taxcal as tc
import Module_carinputE as ce
import Module_Bloan as bl
from Module_carinputE import *
from functools import partial
from Module_Bloan import *
import webbrowser

win = Tk()
win.title('3조의 자동차 추천 프로그램')
ICON=PhotoImage(file='./3조/bcon.png')
win.iconphoto(True, ICON)
win.geometry("840x370") #창의 사이즈
win.resizable(False,False) #창의 사이즈 변경 여부 속성 지정\


def callback(url):
    webbrowser.open_new_tab(url)

def close1():
    pro.destroy()
    tc.myc1.clear()

def nextpage1():
    global pro
    pro = Toplevel(win)
    pro.title("자동차추천시스템")  # 창의 타이틀명
    pro.geometry("500x800")  # 창의 사이즈
    framehigh=tk.Frame(pro)
    framehigh.pack()
    frame2 = tk.Frame(framehigh)
    frame2.pack()
    def exit_window_x():
        close1()
    pro.protocol('WM_DELETE_WINDOW', exit_window_x)

    def p1():
        global a
        a = txt1.get()
        lbl1.config(text=txt1.get())

    def p2():
        global b
        b = txt2.get()
        lbl2.config(text=txt2.get())

    def p3():
        global c
        c = txt3.get()
        lbl3.config(text=txt3.get())

    def p4():
        global d
        d = txt4.get()
        lbl4.config(text=txt4.get())

    def close():
        pro.destroy()

    def final():
        global frame3
        try:
            frame3
            frame3.pack_forget()
            frame3 = tk.Frame(framehigh)
            frame3.pack()
            ResultViewlabel_ViewLabel = tk.Label(frame3)
            ResultViewlabel_ViewLabel.grid(row=4, column=1)
            try:
                CARlist = sc.RecommendCar(txt1.get(), int(txt2.get()), int(txt3.get()), int(txt4.get()))
            except ValueError:
                ResultViewlabel_ViewLabel.config(text="숫자가 아닙니다. 다시 입력해주세요.")
                txt1.delete(0, "end")
                txt2.delete(0, "end")
                txt3.delete(0, "end")
                txt4.delete(0, "end")
            if sc.wealthrangex < 2400:
                ResultViewlabel_ViewLabel.config(text="그 재력으로 뭘산다구요? 뚜벅이는 뚜벅이답게 행동하세요.")
            elif sc.wealthrangex > 13400:
                ResultViewlabel_ViewLabel.config(text="그 정도 재력이면 아무거나 사도 되니 대신 저나 좀 사주세요.")
            else:
                ResultViewlabel_ViewLabel.config(text="<추천 차량>", bg="orange")
                try:
                    for i in range(len(CARlist)):
                        labelnum = tk.Label(frame3, text="%d." % (i + 1))
                        if len(CARlist) > 12:
                            if i > 12:
                                labelnum.grid(row=7 + (i - 13), column=2, sticky="w")
                            else:
                                labelnum.grid(row=7 + i, column=0, sticky="w")
                        else:
                            labelnum.grid(row=7 + i, column=0, sticky="w")
                        globals()["btn_{}".format(i)] = tk.Button(frame3, text=CARlist[i],command=partial(resultpage, CARlist[i]))
                        if len(CARlist) > 12:
                            if i > 12:
                                globals()["btn_{}".format(i)].grid(row=7 + (i - 13), column=3, sticky="w", padx=10, pady=10)
                            else:
                                globals()["btn_{}".format(i)].grid(row=7 + i, column=1, sticky="w", padx=10, pady=10)
                        else:
                            globals()["btn_{}".format(i)].grid(row=7 + i, column=1, sticky="w", padx=10, pady=10)
                    print("추천나의카", myc1)
                except UnboundLocalError:
                    ResultViewlabel_ViewLabel.config(text="숫자가 아닙니다. 다시 입력해주세요.")
                    txt1.delete(0, "end")
                    txt2.delete(0, "end")
                    txt3.delete(0, "end")
                    txt4.delete(0, "end")

            def resetresult():
                txt1.delete(0, END)
                txt2.delete(0, END)
                txt3.delete(0, END)
                txt4.delete(0, END)
                frame3.destroy()

            print("추천나의카", myc1)
            btn1 = tk.Button(frame3, text="다시하기", command=resetresult)
            btn1.grid(row=4, column=2, sticky="w", padx=10, pady=10)
        except NameError:
            frame3 = tk.Frame(framehigh)
            frame3.pack()
            ResultViewlabel_ViewLabel = tk.Label(frame3)
            ResultViewlabel_ViewLabel.grid(row=4, column=1)
            try:
                CARlist = sc.RecommendCar(txt1.get(), int(txt2.get()), int(txt3.get()), int(txt4.get()))
            except ValueError:
                frame3.pack_forget()
                frame3 = tk.Frame(framehigh)
                frame3.pack()
                ResultViewlabel_ViewLabel = tk.Label(frame3)
                ResultViewlabel_ViewLabel.grid(row=4, column=1)
                ResultViewlabel_ViewLabel.config(text="숫자가 아닙니다. 다시 입력해주세요.")
                txt1.delete(0, "end")
                txt2.delete(0, "end")
                txt3.delete(0, "end")
                txt4.delete(0, "end")
            if sc.wealthrangex < 2400:
                ResultViewlabel_ViewLabel.config(text="그 재력으로 뭘산다구요? 뚜벅이는 뚜벅이답게 행동하세요.")
            elif sc.wealthrangex > 13400:
                ResultViewlabel_ViewLabel.config(text="그 정도 재력이면 아무거나 사도 되니 대신 저나 좀 사주세요.")
            else:
                ResultViewlabel_ViewLabel.config(text="<추천 차량>",bg="orange")
                try:
                    for i in range(len(CARlist)):
                        labelnum = tk.Label(frame3, text="%d." % (i + 1))
                        if len(CARlist) > 12:
                            if i > 12:
                                labelnum.grid(row=7 + (i - 13), column=2, sticky="w")
                            else:
                                labelnum.grid(row=7 + i, column=0, sticky="w")
                        else:
                            labelnum.grid(row=7 + i, column=0, sticky="w")
                        globals()["btn_{}".format(i)] = tk.Button(frame3, text=CARlist[i],
                                                                  command=partial(resultpage, CARlist[i]))
                        if len(CARlist) > 12:
                            if i > 12:
                                globals()["btn_{}".format(i)].grid(row=7 + (i - 13), column=3, sticky="w", padx=10,
                                                                   pady=10)
                            else:
                                globals()["btn_{}".format(i)].grid(row=7 + i, column=1, sticky="w", padx=10, pady=10)
                        else:
                            globals()["btn_{}".format(i)].grid(row=7 + i, column=1, sticky="w", padx=10, pady=10)
                except UnboundLocalError:
                    ResultViewlabel_ViewLabel.config(text="숫자가 아닙니다. 다시 입력해주세요.")
                    txt1.delete(0, "end")
                    txt2.delete(0, "end")
                    txt3.delete(0, "end")
                    txt4.delete(0, "end")

            def resetresult():
                txt1.delete(0, END)
                txt2.delete(0, END)
                txt3.delete(0, END)
                txt4.delete(0, END)
                txt1.icursor(0)
                frame3.destroy()
            btn1 = tk.Button(frame3, text="다시하기", command=resetresult)
            btn1.grid(row=4, column=2, sticky="w", padx=10, pady=10)

    def resultpage(x1):
        global pro2
        global myc1
        global listx
        print("추천나의카", myc1)
        # int(myc1[1][2]=0
        # tc.myc1.clear()
        try:
            print("추천나의카", myc1)
            pro2.destroy()
            # listx.clear()
            pro2 = Toplevel(pro)
            pro2.title(x1)
            CARlist = sc.RecommendCar(txt1.get(), int(txt2.get()), int(txt3.get()), int(txt4.get()))
            pro2.geometry("900x300")  # 창의 사이즈
            pro2.resizable(False,False)
            frameup = tk.Frame(pro2)
            frameup.pack(side=TOP)
            framedown = tk.Frame(pro2)
            framedown.pack(side=TOP)
            framedown2 = tk.Frame(pro2)
            framedown2.pack(side=TOP)
            print("추천나의카", myc1)
            def exit_window_x():
                pro2.destroy()
            pro2.protocol('WM_DELETE_WINDOW', exit_window_x)
            class CarInfo:
                def picture(self):
                    listpic = []
                    listpicx = []
                    for w in range(len(CARlist)):
                        for z in sc.cleandatareturn2():
                            for y in CARlist:
                                if y == z[0]:
                                    listpic.append(z)
                    for m in listpic:
                        if m[0] == x1:
                            global picture
                            picture = tk.PhotoImage(file="%s" % m[6], master=pro2)
                    label_pic = tk.Label(frameup, image=picture, bg="green")
                    label_pic.pack()


                def info(self):
                    listx = []
                    for w in range(len(CARlist)):
                        for z in sc.cleandatareturn2():
                            for y in CARlist:
                                if y == z[0]:
                                    listx.append(z)
                    for i in listx:
                        if i[0] == x1:
                            label_info0 = tk.Label(frameup, text="차랑명:%s" % i[0])
                            label_info1 = tk.Label(frameup, text="배기량:%s" % i[1])
                            label_info2 = tk.Label(frameup, text="연비:%s" % i[2])
                            label_info3 = tk.Label(frameup, text="가격:%s만원" % i[3])
                            label_info4 = tk.Label(frameup, text="연료:%s" % i[4])
                            label_info5 = tk.Label(frameup, text="차량유형:%s" % i[5])
                    label_info0.pack()
                    label_info5.pack()
                    label_info3.pack()
                    label_info4.pack()
                    label_info1.pack()
                    label_info2.pack()

            print("추천나의카", myc1)
            james = CarInfo()
            james.picture()
            james.info()
            print("추천나의카", myc1)

            def loancal():
                global myc1
                global CarIdex
                global mycarex
                global stringTemp
                global listc
                global listm
                myc1.clear()  #추천차량선택할때마다 초기화
                myc1.append(x1)
                myc1.append(CarIdex[x1])
                print("추천나의카", myc1)

                def loaninp3():  # 할부 금리 입력값
                    global c
                    c = loantxt3.get()
                    loanbl3.config(text=loantxt3.get())

                def loaninp4():  # 원금캐시백 입력값
                    global d
                    d = loantxt4.get()
                    loanbl4.config(text=loantxt4.get())

                loancal = Toplevel(pro2)
                loancal.title("자동차 대출금 계산기")
                loancal.geometry("600x770")  # 창의 사이즈
                loancal.resizable(True, True)
                # frameLex = tk.Frame(loancal, bd=2, bg='green')
                # frameLex.pack(side='bottom')

                frameLex = tk.Frame(loancal, bd=2, bg='green')
                frameLex.grid(row=5, column=0)

                def closel():
                    loancal.destroy()
                    tc.myc1.clear()
                bt1 = tk.Button(loancal, text="대출창닫기", command=closel)
                bt1.grid(row=8, column=0)



                def exit_window_x():
                    closel()
                loancal.protocol('WM_DELETE_WINDOW', exit_window_x)
                import tkinter.ttk as ttk  # tkinter.ttk를 ttk로 줄여서 쓰겠다.

                co1 = [3, 6, 9, 12, 18, 24, 30, 36, 48, 60, 72, 84, 96, 108, 120, "직접입력"]  # 콤보 박스에 나타낼 항목 리스트
                combobox1 = ttk.Combobox(loancal)  # root라는 창에 콤보박스 생성
                combobox1.config(height=5)  # 높이 설정
                combobox1.config(values=co1)  # 나타낼 항목 리스트(a) 설정
                combobox1.config(state="read & write")  # 콤보 박스에 사용자가 직접 입력 불가
                combobox1.set(co1[5])  # 맨 처음 나타낼 값 설정
                combobox1.grid(row=1, column=3)  # 콤보 박스 배치
                loanmonthT = Label(loancal, text="할부기간(월):")
                loanmonthT.grid(row=1, column=2)
                loanmonthT = Label(loancal, text="개월")
                loanmonthT.grid(row=1, column=4)

                def paint1():  # 할부기간
                    print(combobox1.get())
                print(paint1())

                loanbl1 = Label(loancal, text="할부 원금(단위:만원):")
                loanbl1.grid(row=1, column=0)
                loanbl11 = Label(loancal, text="%d" % int(myc1[1][2]))
                loanbl11.grid(row=1, column=1)

                loanbl3 = Label(loancal, text="할부 금리(year/%)")
                loanbl3.grid(row=3, column=0)
                loantxt3 = Entry(loancal)
                loantxt3.grid(row=3, column=1)
                loantxt3.bind("<Return>", loaninp3)

                loanbl4 = Label(loancal, text="원금 캐시백 (만원)")
                loanbl4.grid(row=4, column=0)
                loantxt4 = Entry(loancal)
                loantxt4.grid(row=4, column=1)
                loantxt4.bind("<Return>", loaninp4)

                lastloanexc = tk.Label(frameLex)
                lastloanexc.grid(row=2, column=0)

                def loanFC():
                    try:
                        # frameLex.destroy()
                        global a
                        global c
                        global d
                        global loancal
                        print(combobox1.get())
                        a1 = combobox1.get()
                        lFC = Toplevel(pro2)
                        lFC.title("최종대출금출력")
                        lFC.geometry("500x600")  # 창의 사이즈
                        lFC.resizable(False, False)  # 창의 사이즈 변경 여부 속성 지정

                        def closeLFC():
                            lFC.destroy()
                        btn1 = tk.Button(lFC, text="결과닫기", command=closeLFC)
                        btn1.pack(side='bottom')
                        framelc = tk.Frame(lFC, bd=2, bg='green')
                        framelc.pack(side='top')
                        framelc2 = tk.Frame(lFC, bd=4, bg='blue')
                        framelc2.pack(side='bottom')

                        # 1a= 할부원금 ,c3=할부 금리 , d4=원금 캐시백

                        label_info0 = tk.Label(framelc, text="할부 개월: %s" % a1)
                        label_info1 = tk.Label(framelc, text="할부 금리(year/%%): %s" % loantxt3.get())
                        # label_info2 = tk.Label(framelc, text="할부 원금(단위:만원): %s" % loantxt1.get())  i[3]

                        label_info2 = tk.Label(framelc, text="할부 원금(단위:만원): %s" % int(myc1[1][2]))
                        # label_info4 = tk.Label(framelc, text="이자 합계:%s" % i[4])
                        label_info5 = tk.Label(framelc, text="원금 캐시백(-): %s" % loantxt4.get())
                        label_infoL = tk.Label(framelc2, text="월 할부금(단위:원): %s " % loanMonthSM(a1, 0, loantxt3.get(),int(myc1[1][2]), 0,
                                                                                               loantxt4.get(), 0, 0))
                        # label_info6 = tk.Label(framelc, text="사은품(-):%s" % i[6])
                        # label_info7 = tk.Label(framelc2, text="실 납부이자:%s" % i[6])
                        # label_info8 = tk.Label(framelc2, text="실질 금리:%s" % i[6])
                        # label_info9 = tk.Label(framelc, text="원금 캐시백(-): %s" % loantxt4.get())
                        label_info0.pack()
                        label_info1.pack()
                        label_info2.pack()
                        # label_info4.pack()
                        label_info5.pack()
                        # label_info6.pack()
                        # label_info7.pack()
                        # label_info8.pack()
                        # label_info9.pack()

                        label_infoL.pack()
                        lFC.mainloop()
                        loancal.mainloop()
                    except ValueError:
                        if loantxt3 != None or combobox1 != None or loantxt4 != None:
                            lastloanexc.config(text="숫자가 아닙니다.다시 입력해주세요.")
                            closeLFC()
                            loantxt3.delete(0, "end")
                            loantxt4.delete(0, "end")
                            # combobox1.config(text="숫자를 입력해 주세요.")
                            combobox1.delete(0, "end")
                        else:
                            pass

                    # ex TypeError:
                    #     labinsu.config(text="차를 구매할 수 있는 나이가 아닙니다.")
                    #     btnout = tk.Button(Insu, text="나가기", command=outinsu)
                    #     btnout.grid(row=4, column=1)

                btnloanCcal = tk.Button(loancal, text="계산하기(원리금균등상환기준)", command=loanFC)
                btnloanCcal.grid(row=7, column=3)
                loancal.mainloop()
                pro.mainloop()

            def outinsu():
                Insu.destroy()

            def insurance():
                global Insu

                def i1():
                    global a
                    a = insutxt1.get()
                    insulbl1.config(text=insutxt1.get())

                def final_insu():
                    try:
                        labinsu.config(text="보험료(1년기준): %d원" % InsuranceCal(insutxt1.get()))
                        btnout = tk.Button(Insu, text="나가기", command=outinsu)
                        btnout.grid(row=4, column=1)
                    except ValueError:
                        labinsu.config(text="숫자를 입력해 주세요.")
                        insutxt1.delete(0, "end")
                    except TypeError:
                        labinsu.config(text="차를 구매할 수 있는 나이가 아닙니다.")
                        btnout = tk.Button(Insu, text="나가기", command=outinsu)
                        btnout.grid(row=4, column=1)

                def InsuranceCal(age):
                    global listc
                    global listm
                    listc = []
                    listm = []
                    for i in sc.list_3:
                        listc.append(i[0])
                        listm.append(i[3])
                    inputcarsmoney = listm[listc.index(x1)]
                    Insurance = round((float(inputcarsmoney) * 0.03) * 10000)
                    if 24 <= int(age) < 26:
                        resul_insu = round(Insurance + (float(Insurance * 0.3)))
                        return resul_insu
                    elif 24 > int(age) >= 19:
                        resul_insu = round(Insurance + (float(Insurance * 0.8)))
                        return resul_insu
                    elif 19 > int(age):
                        return "미성년자"
                    else:
                        return Insurance

                Insu = Toplevel(pro2)
                Insu.title("보험료 계산_%s" % x1)
                Insu.geometry("500x120")  # 창의 사이즈
                Insu.resizable(False, False)  # 창의 사이즈 변경 여부 속성 지정
                insulbl1 = Label(Insu, text="만 나이")
                insulbl1.grid(row=0, column=0)
                insutxt1 = Entry(Insu)
                insutxt1.grid(row=0, column=1)
                insutxt1.bind("<Return>", i1)
                btninsu = tk.Button(Insu, text="계산하기", command=final_insu)
                btninsu.grid(row=1, column=1)
                labinsu = tk.Label(Insu)
                labinsu.grid(row=2, column=1, sticky="w")
                smlb1 = Label(Insu, text="<할증료 부과 기준>")
                smlb1.grid(row=0, column=2)
                smlb2 = Label(Insu, text="만 24세 ~ 만 26세 : 할증률 30% 부과")
                smlb2.grid(row=1, column=2)
                smlb3 = Label(Insu, text="만 24세 미만 : 할증률 80% 부과")
                smlb3.grid(row=2, column=2)
                Insu.mainloop()
                pro.mainloop()

            def outtax():
                Tax.destroy()

            def tax():
                global Tax

                def final_tax():
                    if answer1.get() == 0:
                        labtax2.config(text="")
                        labtax1.config(text="자동차세(1년기준): %s원" % (texcal(answer1.get())))

                    elif answer1.get() == 1:
                        labtax1.config(text="")
                        labtax2.config(text="자동차세(1년기준): %s원" % (texcal(answer1.get())))

                def texcal(ty):
                    global myc1
                    global CarIdex
                    global mycarex
                    global stringTemp
                    tc.alonecarlist()
                    myc1.clear()
                    if x1 in CarIdex:
                        myc1.append(x1)
                        myc1.append(CarIdex[x1])
                        if ty == 0:
                            if int(myc1[1][0]) <= 1000:
                                mycarex = int(myc1[1][0]) * 18
                                return mycarex
                            elif 1000 < int(myc1[1][0]) <= 1600:
                                mycarex = int(myc1[1][0]) * 18
                                return mycarex
                            elif 1600 < int(myc1[1][0]) <= 2000:
                                mycarex = int(myc1[1][0]) * 19
                                return mycarex
                            elif 2000 < int(myc1[1][0]) <= 2500:
                                mycarex = int(myc1[1][0]) * 19
                                return mycarex
                            elif int(myc1[1][0]) >= 2500:
                                mycarex = int(myc1[1][0]) * 24
                                return mycarex
                        elif ty == 1:
                            if int(myc1[1][0]) <= 1000:
                                mycarex = int(myc1[1][0]) * 80
                                return mycarex
                            elif 1000 < int(myc1[1][0]) <= 1600:
                                mycarex = int(myc1[1][0]) * 140
                                return mycarex
                            elif 1600 < int(myc1[1][0]) <= 2000:
                                mycarex = int(myc1[1][0]) * 200
                                return mycarex
                            ################################
                            elif 2000 < int(myc1[1][0]) <= 2500:
                                mycarex = int(myc1[1][0]) * 260
                                return mycarex
                            elif 2500 <= int(myc1[1][0]):
                                mycarex = int(myc1[1][0]) * 320
                                return mycarex
                        else:
                            return "잘못입력함"

                def retry():
                    labtax1.config(text="")
                    labtax2.config(text="")
                    tc.myc1.clear()

                Tax = Toplevel(pro2)
                Tax.title("자동차세 계산_%s" % x1)
                Tax.geometry("500x140")  # 창의 사이즈
                Tax.resizable(False, False)  # 창의 사이즈 변경 여부 속성 지정
                answer1 = tk.IntVar()
                taxtxt2 = tk.Radiobutton(Tax, text="영업용", variable=answer1, value=0)
                taxtxt2.grid(row=1, column=1, sticky="w")
                taxtxt3 = tk.Radiobutton(Tax, text="비영업용", variable=answer1, value=1)
                taxtxt3.grid(row=2, column=1, sticky="w")
                btntax = tk.Button(Tax, text="계산하기", command=final_tax)
                btntax.grid(row=3, column=1)
                btntax2 = tk.Button(Tax, text="다시하기", command=retry)
                btntax2.grid(row=4, column=1)
                btntax3 = tk.Button(Tax, text="나가기", command=outtax)
                btntax3.grid(row=5, column=1)
                labtax1 = tk.Label(Tax)
                labtax1.grid(row=1, column=3, sticky="w")
                labtax2 = tk.Label(Tax)
                labtax2.grid(row=2, column=3, sticky="w")
                Tax.mainloop()
                pro.mainloop()

            btn1 = tk.Button(framedown, text="자동차 대출금 계산", command=loancal)
            btn1.pack(side='left')
            btn2 = tk.Button(framedown, text="보험료 계산", command=insurance)
            btn2.pack(side='left')
            btn3 = tk.Button(framedown, text="자동차세 계산", command=tax)
            btn3.pack(side='left')
            btn4 = tk.Button(framedown, text="뒤로가기", command=close1)
            btn4.pack(side='left')
            Blank = tk.Label(framedown2, text="")
            Blank.pack(side='top')
            link = tk.Label(framedown2, text='이미지 출처 : 카비(http://www.carby.co.kr/)', font=('Helveticabold', 8),
                            fg="blue", cursor="hand2")
            link.pack(side='bottom')
            link.bind("<Button-1>", lambda e:
            callback('http://www.carby.co.kr/car/brands/'))
        except NameError:
            pro2 = Toplevel(pro)
            pro2.title(x1)
            CARlist = sc.RecommendCar(txt1.get(), int(txt2.get()), int(txt3.get()), int(txt4.get()))
            pro2.geometry("900x300")  # 창의 사이즈
            pro2.resizable(False,False)
            frameup = tk.Frame(pro2)
            frameup.pack(side=TOP)
            framedown = tk.Frame(pro2)
            framedown.pack(side=TOP)
            framedown2 = tk.Frame(pro2)
            framedown2.pack(side=TOP)
            def exit_window_x():
                pro2.destroy()
                tc.myc1.clear()
            pro2.protocol('WM_DELETE_WINDOW', exit_window_x)
            class CarInfo:
                def picture(self):
                    listpic = []
                    listpicx = []
                    for w in range(len(CARlist)):
                        for z in sc.cleandatareturn2():
                            for y in CARlist:
                                if y == z[0]:
                                    listpic.append(z)
                    for m in listpic:
                        if m[0] == x1:
                            global picture
                            picture = tk.PhotoImage(file="%s" % m[6], master=pro2)
                    label_pic = tk.Label(frameup, image=picture, bg="green")
                    label_pic.pack()

                def info(self):
                    listx = []
                    for w in range(len(CARlist)):
                        for z in sc.cleandatareturn2():
                            for y in CARlist:
                                if y == z[0]:
                                    listx.append(z)
                    for i in listx:
                        if i[0] == x1:
                            label_info0 = tk.Label(frameup, text="차랑명:%s" % i[0])
                            label_info1 = tk.Label(frameup, text="배기량:%s" % i[1])
                            label_info2 = tk.Label(frameup, text="연비:%s" % i[2])
                            label_info3 = tk.Label(frameup, text="가격:%s만원" % i[3])
                            label_info4 = tk.Label(frameup, text="연료:%s" % i[4])
                            label_info5 = tk.Label(frameup, text="차량유형:%s" % i[5])
                    label_info0.pack()
                    label_info5.pack()
                    label_info3.pack()
                    label_info4.pack()
                    label_info1.pack()
                    label_info2.pack()

            james = CarInfo()
            james.picture()
            james.info()

            def loancal():
                global myc1
                global CarIdex
                global mycarex
                global stringTemp
                global listc
                global listm
                myc1.append(x1)
                myc1.append(CarIdex[x1])

                def loaninp3():  # 할부 금리 입력값
                    global c
                    c = loantxt3.get()
                    loanbl3.config(text=loantxt3.get())

                def loaninp4():  # 원금캐시백 입력값
                    global d
                    d = loantxt4.get()
                    loanbl4.config(text=loantxt4.get())

                loancal = Toplevel(pro2)
                loancal.title("자동차 대출금 계산기")
                loancal.geometry("600x770")  # 창의 사이즈
                loancal.resizable(True, True)
                # frameLex = tk.Frame(loancal, bd=2, bg='green')
                # frameLex.pack(side='bottom')

                frameLex = tk.Frame(loancal, bd=2, bg='green')
                frameLex.grid(row=5, column=0)
                def closel():
                    loancal.destroy()
                    tc.myc1.clear()
                def exit_window_x():
                    closel()
                loancal.protocol('WM_DELETE_WINDOW', exit_window_x)
                bt1 = tk.Button(loancal, text="대출창닫기", command=closel)
                bt1.grid(row=8, column=0)


                import tkinter.ttk as ttk  # tkinter.ttk를 ttk로 줄여서 쓰겠다.

                co1 = [3, 6, 9, 12, 18, 24, 30, 36, 48, 60, 72, 84, 96, 108, 120, "직접입력"]  # 콤보 박스에 나타낼 항목 리스트
                combobox1 = ttk.Combobox(loancal)  # root라는 창에 콤보박스 생성
                combobox1.config(height=5)  # 높이 설정
                combobox1.config(values=co1)  # 나타낼 항목 리스트(a) 설정
                combobox1.config(state="read & write")  # 콤보 박스에 사용자가 직접 입력 불가
                combobox1.set(co1[5])  # 맨 처음 나타낼 값 설정
                combobox1.grid(row=1, column=3)  # 콤보 박스 배치
                loanmonthT = Label(loancal, text="할부기간(월):")
                loanmonthT.grid(row=1, column=2)
                loanmonthT = Label(loancal, text="개월")
                loanmonthT.grid(row=1, column=4)

                def paint1():  # 할부기간
                    print(combobox1.get())

                print(paint1())

                loanbl1 = Label(loancal, text="할부 원금(단위:만원):")
                loanbl1.grid(row=1, column=0)
                loanbl11 = Label(loancal, text="%d" % int(myc1[1][2]))
                loanbl11.grid(row=1, column=1)

                loanbl3 = Label(loancal, text="할부 금리(year/%)")
                loanbl3.grid(row=3, column=0)
                loantxt3 = Entry(loancal)
                loantxt3.grid(row=3, column=1)
                loantxt3.bind("<Return>", loaninp3)

                loanbl4 = Label(loancal, text="원금 캐시백 (만원)")
                loanbl4.grid(row=4, column=0)
                loantxt4 = Entry(loancal)
                loantxt4.grid(row=4, column=1)
                loantxt4.bind("<Return>", loaninp4)

                lastloanexc = tk.Label(frameLex)
                lastloanexc.grid(row=2, column=0)

                def loanFC():
                    try:
                        # frameLex.destroy()
                        global a
                        global c
                        global d
                        global loancal
                        print(combobox1.get())
                        a1 = combobox1.get()
                        lFC = Toplevel(pro2)
                        lFC.title("최종대출금출력")
                        lFC.geometry("500x600")  # 창의 사이즈
                        lFC.resizable(False, False)  # 창의 사이즈 변경 여부 속성 지정

                        def closeLFC():
                            lFC.destroy()

                        btn1 = tk.Button(lFC, text="결과닫기", command=closeLFC)
                        btn1.pack(side='bottom')
                        framelc = tk.Frame(lFC, bd=2, bg='green')
                        framelc.pack(side='top')
                        framelc2 = tk.Frame(lFC, bd=4, bg='blue')
                        framelc2.pack(side='bottom')

                        # 1a= 할부원금 ,c3=할부 금리 , d4=원금 캐시백

                        label_info0 = tk.Label(framelc, text="할부 개월: %s" % a1)
                        label_info1 = tk.Label(framelc, text="할부 금리(year/%%): %s" % loantxt3.get())
                        # label_info2 = tk.Label(framelc, text="할부 원금(단위:만원): %s" % loantxt1.get())  i[3]

                        label_info2 = tk.Label(framelc, text="할부 원금(단위:만원): %s" % int(myc1[1][2]))
                        # label_info4 = tk.Label(framelc, text="이자 합계:%s" % i[4])
                        label_info5 = tk.Label(framelc, text="원금 캐시백(-): %s" % loantxt4.get())
                        label_infoL = tk.Label(framelc2, text="월 할부금(단위:원): %s " % loanMonthSM(a1, 0, loantxt3.get(),
                                                                                               int(myc1[1][2]), 0,
                                                                                               loantxt4.get(), 0, 0))
                        # label_info6 = tk.Label(framelc, text="사은품(-):%s" % i[6])
                        # label_info7 = tk.Label(framelc2, text="실 납부이자:%s" % i[6])
                        # label_info8 = tk.Label(framelc2, text="실질 금리:%s" % i[6])
                        # label_info9 = tk.Label(framelc, text="원금 캐시백(-): %s" % loantxt4.get())
                        label_info0.pack()
                        label_info1.pack()
                        label_info2.pack()
                        # label_info4.pack()
                        label_info5.pack()
                        # label_info6.pack()
                        # label_info7.pack()
                        # label_info8.pack()
                        # label_info9.pack()

                        label_infoL.pack()
                        lFC.mainloop()
                        loancal.mainloop()
                    except ValueError:
                        if loantxt3 != None or combobox1 != None or loantxt4 != None:
                            lastloanexc.config(text="숫자가 아닙니다.다시 입력해주세요.")
                            closeLFC()
                            loantxt3.delete(0, "end")
                            loantxt4.delete(0, "end")
                            # combobox1.config(text="숫자를 입력해 주세요.")
                            combobox1.delete(0, "end")
                        else:
                            pass

                    # ex TypeError:
                    #     labinsu.config(text="차를 구매할 수 있는 나이가 아닙니다.")
                    #     btnout = tk.Button(Insu, text="나가기", command=outinsu)
                    #     btnout.grid(row=4, column=1)

                btnloanCcal = tk.Button(loancal, text="계산하기(원리금균등상환기준)", command=loanFC)
                btnloanCcal.grid(row=7, column=3)
                loancal.mainloop()
                pro.mainloop()

            def outinsu():
                Insu.destroy()

            def insurance():
                global Insu

                def i1():
                    global a
                    a = insutxt1.get()
                    insulbl1.config(text=insutxt1.get())

                def final_insu():
                    try:
                        labinsu.config(text="보험료(1년기준): %d원" % InsuranceCal(insutxt1.get()))
                        btnout = tk.Button(Insu, text="나가기", command=outinsu)
                        btnout.grid(row=4, column=1)
                    except ValueError:
                        labinsu.config(text="숫자를 입력해 주세요.")
                        insutxt1.delete(0, "end")
                    except TypeError:
                        labinsu.config(text="차를 구매할 수 있는 나이가 아닙니다.")
                        btnout = tk.Button(Insu, text="나가기", command=outinsu)
                        btnout.grid(row=4, column=1)

                def InsuranceCal(age):
                    global listc
                    global listm
                    listc = []
                    listm = []
                    for i in sc.list_3:
                        listc.append(i[0])
                        listm.append(i[3])
                    inputcarsmoney = listm[listc.index(x1)]
                    Insurance = round((float(inputcarsmoney) * 0.03) * 10000)
                    if 24 <= int(age) < 26:
                        resul_insu = round(Insurance + (float(Insurance * 0.3)))
                        return resul_insu
                    elif 24 > int(age) >= 19:
                        resul_insu = round(Insurance + (float(Insurance * 0.8)))
                        return resul_insu
                    elif 19 > int(age):
                        return "미성년자"
                    else:
                        return Insurance

                Insu = Toplevel(pro2)
                Insu.title("보험료 계산_%s" % x1)
                Insu.geometry("500x120")  # 창의 사이즈
                Insu.resizable(False, False)  # 창의 사이즈 변경 여부 속성 지정
                insulbl1 = Label(Insu, text="만 나이")
                insulbl1.grid(row=0, column=0)
                insutxt1 = Entry(Insu)
                insutxt1.grid(row=0, column=1)
                insutxt1.bind("<Return>", i1)
                btninsu = tk.Button(Insu, text="계산하기", command=final_insu)
                btninsu.grid(row=1, column=1)
                labinsu = tk.Label(Insu)
                labinsu.grid(row=2, column=1, sticky="w")
                smlb1 = Label(Insu, text="<할증료 부과 기준>")
                smlb1.grid(row=0, column=2)
                smlb2 = Label(Insu, text="만 24세 ~ 만 26세 : 할증률 30% 부과")
                smlb2.grid(row=1, column=2)
                smlb3 = Label(Insu, text="만 24세 미만 : 할증률 80% 부과")
                smlb3.grid(row=2, column=2)
                Insu.mainloop()
                pro.mainloop()

            def outtax():
                Tax.destroy()

            def tax():
                global Tax

                def final_tax():
                    if answer1.get() == 0:
                        labtax2.config(text="")
                        labtax1.config(text="자동차세(1년기준): %s원" % (texcal(answer1.get())))

                    elif answer1.get() == 1:
                        labtax1.config(text="")
                        labtax2.config(text="자동차세(1년기준): %s원" % (texcal(answer1.get())))

                def texcal(ty):
                    global myc1
                    global CarIdex
                    global mycarex
                    global stringTemp
                    tc.alonecarlist()
                    if x1 in CarIdex:
                        myc1.append(x1)
                        myc1.append(CarIdex[x1])
                        if ty == 0:
                            if int(myc1[1][0]) <= 1000:
                                mycarex = int(myc1[1][0]) * 18
                                return mycarex
                            elif int(myc1[1][0]) <= 1600:
                                mycarex = int(myc1[1][0]) * 18
                                return mycarex
                            elif int(myc1[1][0]) <= 2000:
                                mycarex = int(myc1[1][0]) * 19
                                return mycarex
                            elif int(myc1[1][0]) <= 2500:
                                mycarex = int(myc1[1][0]) * 19
                                return mycarex
                            elif int(myc1[1][0]) >= 2500:
                                mycarex = int(myc1[1][0]) * 24
                                return mycarex
                        elif ty == 1:
                            if int(myc1[1][0]) <= 1000:
                                mycarex = int(myc1[1][0]) * 80
                                return mycarex
                            elif int(myc1[1][0]) <= 1600:
                                mycarex = int(myc1[1][0]) * 140
                                return mycarex
                            elif int(myc1[1][0]) >= 1600:
                                mycarex = int(myc1[1][0]) * 200
                                return mycarex
                        else:
                            return "잘못입력함"

                def retry():
                    labtax1.config(text="")
                    labtax2.config(text="")
                    tc.myc1.clear()

                Tax = Toplevel(pro2)
                Tax.title("자동차세 계산_%s" % x1)
                Tax.geometry("500x140")  # 창의 사이즈
                Tax.resizable(False, False)  # 창의 사이즈 변경 여부 속성 지정
                answer1 = tk.IntVar()
                taxtxt2 = tk.Radiobutton(Tax, text="영업용", variable=answer1, value=0)
                taxtxt2.grid(row=1, column=1, sticky="w")
                taxtxt3 = tk.Radiobutton(Tax, text="비영업용", variable=answer1, value=1)
                taxtxt3.grid(row=2, column=1, sticky="w")
                # taxtxt2.bind("<Return>", t2)
                btntax = tk.Button(Tax, text="계산하기", command=final_tax)
                btntax.grid(row=3, column=1)
                btntax2 = tk.Button(Tax, text="다시하기", command=retry)
                btntax2.grid(row=4, column=1)
                btntax3 = tk.Button(Tax, text="나가기", command=outtax)
                btntax3.grid(row=5, column=1)
                labtax1 = tk.Label(Tax)
                labtax1.grid(row=1, column=3, sticky="w")
                labtax2 = tk.Label(Tax)
                labtax2.grid(row=2, column=3, sticky="w")
                Tax.mainloop()
                pro.mainloop()

            btn1 = tk.Button(framedown, text="자동차 대출금 계산", command=loancal)
            btn1.pack(side='left')
            btn2 = tk.Button(framedown, text="보험료 계산", command=insurance)
            btn2.pack(side='left')
            btn3 = tk.Button(framedown, text="자동차세 계산", command=tax)
            btn3.pack(side='left')
            btn4 = tk.Button(framedown, text="뒤로가기", command=close1)
            btn4.pack(side='left')
            Blank=tk.Label(framedown2, text="")
            Blank.pack(side='top')
            link = tk.Label(framedown2, text='이미지 출처 : 카비(http://www.carby.co.kr/)', font=('Helveticabold', 8),
                            fg="blue", cursor="hand2")
            link.pack(side='bottom')
            link.bind("<Button-1>", lambda e:
            callback('http://www.carby.co.kr/car/brands/'))

    lbl1 = Label(frame2, text="이름")

    txt1 = Entry(frame2)

    txt1.bind("<Return>", p1)
    lbl2 = Label(frame2, text="재산(단위:만원)")
    lbl2.grid(row=1, column=0)
    txt2 = Entry(frame2)
    txt2.grid(row=1, column=1)
    txt2.bind("<Return>", p2)
    lbl3 = Label(frame2, text="월급(단위:만원)")
    lbl3.grid(row=2, column=0)
    txt3 = Entry(frame2)
    txt3.grid(row=2, column=1)
    txt3.bind("<Return>", p3)
    lbl4 = Label(frame2, text="빚(단위:만원)")
    lbl4.grid(row=3, column=0)
    txt4 = Entry(frame2)
    txt4.grid(row=3, column=1)
    txt4.bind("<Return>", p4)
    btn = Button(frame2, text="OK", width=15, command=final)
    btn.grid(row=4, column=1)
    lb5 = tk.Label(pro)
    lb5.pack()
    win.mainloop()

def close2():
    pro.destroy()

def nextpage2():  #  여기에 내차 견적 만들기!
    pro = Tk()
    pro.title("내차 견적 조회")  # 창의 타이틀명
    pro.geometry("600x550")  # 창의 사이즈
    pro.resizable(False,False)

    frame2 = tk.Frame(pro)
    frame2.grid(row=3, column=1)
    frame3 = tk.Frame(pro)
    frame3.grid(row=5, column=1)
    frame4 = tk.Frame(pro, bd=4, bg='blue')
    frame4.grid(row=0, column=4)


    def CarCompany1():

        import tkinter.ttk
        global comboboxC
        global valuescar

        valuescar = ["기아","렉서스","르노코리아","마세라티","메르세데스-벤츠","미니","볼보","BMW","쉐보레","쌍용","아우디","재규어","제네시스","지프","캐딜락","토요타","포드","포르쉐","폭스바겐","현대","혼다"]
        comboboxC = tkinter.ttk.Combobox(frame2, height=10, values=valuescar)
        comboboxC.grid(row=0, column=1)
        comboboxC.config(state="readonly")
        def pCar(x):
            if comboboxC.get() in valuescar:
                global combobox
                values = [mycarname(comboboxC.get())[i] for i in range(len(mycarname(comboboxC.get())))]
                combobox = tkinter.ttk.Combobox(frame2, height=10)
                combobox.grid(row=1, column=1)
                combobox.config(state="readonly", values=values)
                def qCar(x):
                    if combobox.get() in values:
                        btnd = Button(frame2, text="데이터적용", width=15, command=final)
                        btnd.grid(row=6, column=1)
                combobox.bind("<<ComboboxSelected>>",qCar)
                combobox.set(comboboxC.get())

        comboboxC.bind("<<ComboboxSelected>>",pCar)
        comboboxC.set("회사명")

        def mycarname(x):
            open("자동차 목록.txt", 'r', encoding='UTF-8')
            global list_1
            global list_2
            global list_3
            global list_4
            list_1 = []
            list_2 = []
            list_3 = []
            list_4 = []
            list_5 = []
            for i in open("자동차 목록.txt", 'r', encoding='UTF-8').readlines():
                if "차량명" in i:
                    continue
                else:
                    list_1.append(i)
            for i in list_1:
                temp = i.replace('\n', '')
                list_2.append(temp)
            for i in list_2:
                list_3.append(i.split('\t'))
            for i in list_3:
                list_4.append(i[0])
            for i in list_4:
                if comboboxC.get() in i:
                    list_5.append(i)
            for i in range(len(list_5)):
                return list_5
    def close2():
        pro.destroy()

    def final():
        global a
        taxcalres()
        if len(escar)==0:
            global top
            global eslist
            global x1
            esw1 = Toplevel(pro)
            esw1.title("견적 출력")
            esw1.geometry("300x300")  # 창의 사이즈
            esw1.resizable(True, True)  # 창의 사이즈 변경 여부 속성 지정
            framegj = tk.Frame(esw1, bd=2, bg='green')
            framegj.pack(side='top')
            frame3 = tk.Frame(esw1, bd=1, bg='blue')
            frame3.pack(side='top')
            frame0 = tk.Frame(esw1)
            frame0.pack(side='top')
            link = tk.Label(esw1, text='이미지 출처 : 카비(http://www.carby.co.kr/)', font=('Helveticabold', 8),
                            fg="blue", cursor="hand2")
            link.pack(side='bottom')
            link.bind("<Button-1>", lambda e:
            callback('http://www.carby.co.kr/car/brands/'))
            try:
                a =ce.taxcal(combobox.get(), int(txt5.get()))
                for m in ce.cleandatacarlist():
                    if m[0] == combobox.get():
                        global picture
                        picture = tk.PhotoImage(file="%s" % m[6], master=esw1)
                label_info0 = tk.Label(frame0, text="차랑명:%s" % escar[0])
                label_info1 = tk.Label(frame0, text="배기량:%s" % escar[1][0])
                label_info2 = tk.Label(frame0, text="연비:%s" % escar[1][1])
                label_info3 = tk.Label(frame0, text="가격(단위:만):%s 만원" % int(escar[1][2]))
                label_info4 = tk.Label(frame0, text="연료:%s" % escar[1][3])
                label_info5 = tk.Label(frame0, text="차량유형:%s" % escar[1][4])
                label_info0.pack()
                label_info1.pack()
                label_info2.pack()
                label_info3.pack()
                label_info4.pack()
                label_info5.pack()
                pictureresult = tk.Label(framegj, image=picture)
                pictureresult.pack()
            except ValueError:
                lb5.config(text="숫자를 입력해주세요.")
                txt5.delete(0,"end")
                esw1.withdraw()

            def closematch():
                for widget in frame0.winfo_children():
                    widget.destroy()
                frame0.destroy()
                frame0.pack_forget()
                esw1.destroy()
                taxcalres()
            btn4 = tk.Button(esw1, text="견적창 닫기", command=closematch)
            btn4.pack()
            ResultViewlabel_ViewLabel = tk.Label(frame3, text="<견적값>")
            ResultViewlabel_ViewLabel.grid(row=0, column=1, sticky="w")
            esw1.mainloop()
            taxcalres()
        else:
            taxcalres()

    lbl1 = Label(frame2, text="회사 선택")  # 틀만들기
    lbl1.grid(row=0, column=0)
    lbl1 = Label(frame2, text="차종 선택")  # 틀만들기
    lbl1.grid(row=1, column=0)
    CarCompany1()
    lbl5 = Label(frame2, text="사용일 수",width=15)
    lbl5.grid(row=4, column=0)
    txt5 = Entry(frame2,width=20)
    txt5.grid(row=4, column=1)
    btnces = Button(frame2, text="닫기", width=15, command=close2)
    btnces.bind("<Return>", final)
    btnces.grid(row=7, column=1)
    lb5 = tk.Label(frame2)
    lb5.grid(row=5, column=1, sticky="w")
    ResultViewlabel_ViewLabel = tk.Label(frame3)
    ResultViewlabel_ViewLabel.grid(row=6, column=2, sticky="w")

    pro.mainloop()

def close3():
    test.destroy()

def nextpage3():
    global test
    test=Toplevel(win)
    test.title("운전 성향 검사")
    test.geometry("300x280")
    test.resizable(False,False)

    def result():
        testnext = Toplevel(test)
        testnext.title("운전 성향 테스트 결과")
        def recom_car(x):
            import random as rd
            open("자동차 목록.txt", 'r', encoding='UTF-8')
            global list_1
            global list_2
            global list_3
            global list_4
            list_1 = []
            list_2 = []
            list_3 = []
            list_4 = []
            list_5 = []
            for i in open("자동차 목록.txt", 'r', encoding='UTF-8').readlines():
                if "차량명" in i:
                    continue
                else:
                    list_1.append(i)
            for i in list_1:
                temp = i.replace('\n', '')
                list_2.append(temp)
            for i in list_2:
                list_3.append(i.split('\t'))
            for i in list_3:
                if x in i:
                    list_4.append(i[0])
                    list_5.append(i[6])
            return list_4[0]
        def recom_car2(x):
            import random as rd
            open("자동차 목록.txt", 'r', encoding='UTF-8')
            global list_1
            global list_2
            global list_3
            global list_4
            list_1 = []
            list_2 = []
            list_3 = []
            list_4 = []
            list_5 = []
            for i in open("자동차 목록.txt", 'r', encoding='UTF-8').readlines():
                if "차량명" in i:
                    continue
                else:
                    list_1.append(i)
            for i in list_1:
                temp = i.replace('\n', '')
                list_2.append(temp)
            for i in list_2:
                list_3.append(i.split('\t'))
            for i in list_3:
                if x in i:
                    list_4.append(i[0])
                    list_5.append(i[6])
            return list_5[0]

        lbone = tk.Label(testnext, font=("굴림", 30, "bold"), bg="yellow")
        lbone.pack(side=TOP)
        lbblank = tk.Label(testnext)
        lbblank.pack(side=TOP)
        testframe = tk.Frame(testnext, bd=2, bg='green')
        testframe.pack(side=TOP)
        lbtwo = tk.Label(testnext, font=("굴림", 10, "bold"))
        lbtwo.pack(side=TOP)
        lbthree = tk.Label(testnext, font=("굴림", 10, "bold"))
        lbthree.pack(side=TOP)
        lbfour = tk.Label(testnext, font=("굴림", 10, "bold"))
        lbfour.pack(side=TOP)
        lbfive = tk.Label(testnext, font=("굴림", 12), wraplength=500)
        lbfive.pack(side=TOP, padx=10, pady=10)
        link = tk.Label(testnext, text='이미지 출처 : 카비(http://www.carby.co.kr/)', font=('Helveticabold', 8),
                     fg="blue", cursor="hand2")
        link.pack(side='bottom')
        link.bind("<Button-1>", lambda e:
        callback('http://www.carby.co.kr/car/brands/'))
        score = answer1.get() + answer2.get() + answer3.get() + answer4.get() + answer5.get() + answer6.get() + answer7.get() + answer8.get() + answer9.get() + answer10.get()
        if score == 0:
            lbone.config(text="따듯한 오지라퍼")
            lbblank.config(text="")
            testpic = tk.PhotoImage(file="%s" % recom_car2("경형 해치백"), master=testnext)
            lbtestpic = tk.Label(testframe, image=testpic)
            lbtestpic.pack()
            lbtwo.config(text="어울리는 차 : %s" % recom_car("경형 해치백"))
            lbthree.config(text="어울리는 옵션 : 비상등, 방향지시등")
            lbfour.config(text="어울리는 도로 : 한적한 해안도로")
            lbfive.config(
                text="누가봐도 너무 착한 당신! 억지로 끼어드려는 차량까지 왠만하면 다 양보해주는 편이네요. 하지만 양보했는데 상대차량이 고마움의 표시도 없이 숭~지나가면 속상해 합니다. 난폭운전을 하는 운전자를 만나도 싸움 나기 싫어 피하는 당신, 그대신 "
                     " 돌려 스마트국민제보로 신고하는 편입니다. 내가 당했을 때보다 남이 당했을 때 더 분한 당신! 오지랖이 넓다는 소리도 듣지만 선의의 도움을 주는 착한 사람이군요!")
        elif score == 1:
            lbone.config(text="관대하고 친절한 낭만러")
            lbblank.config(text="")
            testpic = tk.PhotoImage(file="%s" % recom_car2("소형 해치백"), master=testnext)
            lbtestpic = tk.Label(testframe, image=testpic)
            lbtestpic.pack()
            lbtwo.config(text="어울리는 차 : %s" % recom_car("소형 해치백"))
            lbthree.config(text="어울리는 옵션 : 귀여운 클락션")
            lbfour.config(text="어울리는 도로 : 서행하는 길")
            lbfive.config(
                text="좋은 사람이라는 소리를 자주 듣는 당신~ 운전하면서 화나는 상황도 그러려니 넘어가요. 남에 대한 포용력이 높기 때문이에요. 내가 아는 빠른 길이 있어도 동승자가 다른 길을 안다고 하면 의아해도 따라가주는 성격! 하지만 개인주의적인 성향이 강해서 내 물건을 막 만지는 걸 특히나 싫어해요. 비오는날 눈오는날 햇살이 좋은 날 모두 감성을 즐길 줄 아는 낭만쟁이!")
        elif score == 2:
            lbone.config(text="운전을 하는 이순간, 나는 바람과 하나야~!")
            lbblank.config(text="")
            testpic = tk.PhotoImage(file="%s" % recom_car2("중형 세단"), master=testnext)
            lbtestpic = tk.Label(testframe, image=testpic)
            lbtestpic.pack()
            lbtwo.config(text="어울리는 차 : %s" % recom_car("중형 세단"))
            lbthree.config(text="어울리는 옵션 : 파노라마 썬루프")
            lbfour.config(text="어울리는 도로 : 바닷바람이 느껴지는 해안도로")
            lbfive.config(
                text="누가봐도 자유분방한 당신! 틀에 박힌 것을 싫어하죠. 그래서 그런지 답답한 사무실보단 바깥에서 일하는게 잘 어울리는 사람! 사람들과 이야기하는 걸 좋아해서 어떤 차를 살까 고민할 때도 최대한 많은 사람들에게 동네방네소문내고 의견을 물어보는 편, 그만큼 귀도 얇아서 살려고 하는 차가 매번 바뀌어요. 하지만 이것저것 골치아프게 생각하는게 싫어서 차를 고를 땐 매번 내가 처음 생각했던 그 차를 살 확률이 높네요!")
        elif score == 3:
            lbone.config(text="흥이 난다, 흥이나~! 내 차안 월드스타!")
            lbblank.config(text="")
            testpic = tk.PhotoImage(file="%s" % recom_car2("준대형 트럭"), master=testnext)
            lbtestpic = tk.Label(testframe, image=testpic)
            lbtestpic.pack()
            lbtwo.config(text="어울리는 차 : %s" % recom_car("준대형 트럭"))
            lbthree.config(text="어울리는 옵션 : 서라운드 스피커, 블루투스 마이크")
            lbfour.config(text="어울리는 도로 : 적당히 막히는 고속도로")
            lbfive.config(
                text="평소 흥이 많다는 소리를 많이 듣는 당신, 가만히 있어도 '무슨 좋은 일 있어요?, 기분 좋아보여요~'라고 자주 듣는 편이죠. 그닥 친하지 않은 사람이 차를 태워달라고 해도 거절하지 못합니다. 모두 잘 지내는게 좋다고 생각하기 때문에 비호감만 아니면 왠만하면 태워주는 편! 하지만 친절을 베풀고 생색내는편이네요~")
        elif score == 4:
            lbone.config(text="따듯한 오지라퍼")
            lbblank.config(text="")
            testpic = tk.PhotoImage(file="%s" % recom_car2("경형 해치백"), master=testnext)
            lbtestpic = tk.Label(testframe, image=testpic)
            lbtestpic.pack()
            lbtwo.config(text="어울리는 차 : %s" % recom_car("경형 해치백"))
            lbthree.config(text="어울리는 옵션 : 비상등, 방향지시등")
            lbfour.config(text="어울리는 도로 : 한적한 해안도로")
            lbfive.config(
                text="누가봐도 너무 착한 당신! 억지로 끼어드려는 차량까지 왠만하면 다 양보해주는 편이네요. 하지만 양보했는데 상대차량이 고마움의 표시도 없이 숭~지나가면 속상해 합니다. 난폭운전을 하는 운전자를 만나도 싸움 나기 싫어 피하는 당신, 그대신 블랙박스를 돌려 스마트국민제보로 신고하는 편입니다. 내가 당했을 때보다 남이 당했을 때 더 분한 당신! 오지랖이 넓다는 소리도 듣지만 선의의 도움을 주는 착한 사람이군요!")
        elif score == 5:
            lbone.config(text="관대하고 친절한 낭만러")
            lbblank.config(text="")
            testpic = tk.PhotoImage(file="%s" % recom_car2("소형 해치백"), master=testnext)
            lbtestpic = tk.Label(testframe, image=testpic)
            lbtestpic.pack()
            lbtwo.config(text="어울리는 차 : %s" % recom_car("소형 해치백"))
            lbthree.config(text="어울리는 옵션 : 귀여운 클락션")
            lbfour.config(text="어울리는 도로 : 서행하는 길")
            lbfive.config(
                text="좋은 사람이라는 소리를 자주 듣는 당신~ 운전하면서 화나는 상황도 그러려니 넘어가요. 남에 대한 포용력이 높기 때문이에요. 내가 아는 빠른 길이 있어도 동승자가 다른 길을 안다고 하면 의아해도 따라가주는 성격! 하지만 개인주의적인 성향이 강해서 내 물건을 막 만지는 걸 특히나 싫어해요. 비오는날 눈오는날 햇살이 좋은 날 모두 감성을 즐길 줄 아는 낭만쟁이!")
        elif score == 6:
            lbone.config(text="흥이 난다, 흥이나~! 내 차안 월드스타!")
            lbblank.config(text="")
            testpic = tk.PhotoImage(file="%s" % recom_car2("준대형 트럭"), master=testnext)
            lbtestpic = tk.Label(testframe, image=testpic)
            lbtestpic.pack()
            lbtwo.config(text="어울리는 차 : %s" % recom_car("준대형 트럭"))
            lbthree.config(text="어울리는 옵션 : 서라운드 스피커, 블루투스 마이크")
            lbfour.config(text="어울리는 도로 : 적당히 막히는 고속도로")
            lbfive.config(
                text="평소 흥이 많다는 소리를 많이 듣는 당신, 가만히 있어도 '무슨 좋은 일 있어요?, 기분 좋아보여요~'라고 자주 듣는 편이죠. 그닥 친하지 않은 사람이 차를 태워달라고 해도 거절하지 못합니다. 모두 잘 지내는게 좋다고 생각하기 때문에 비호감만 아니면 왠만하면 태워주는 편! 하지만 친절을 베풀고 생색내는편이네요~")
        elif score == 7:
            lbone.config(text="신차 나오면 제일 먼저 찾아보는 얼리카답터")
            lbblank.config(text="")
            testpic = tk.PhotoImage(file="%s" % recom_car2("대형 세단"), master=testnext)
            lbtestpic = tk.Label(testframe, image=testpic)
            lbtestpic.pack()
            lbtwo.config(text="어울리는 차 : %s" % recom_car("대형 세단"))
            lbthree.config(text="어울리는 옵션 : 비상등, 방향지시등")
            lbfour.config(text="어울리는 도로 : 방금 깔린 아스팔트 위")
            lbfive.config(
                text="신차가 나오면 시승기를 찾아보는게 제일 재밌는 당신! 스포츠 게임을 좋아하기 때문에 운전도 나름대로 재미를 느끼네요. 새로운 것에 대한 욕구가 강하기 때문에 어디 재밌는 곳이 생겼다고 하면 꼭 찾아가고 싶어하는 당신. 경쟁심이 있어서 운전을 잘하고 못하고를 떠나서 내 주변에 있는 '누구'보단 잘하고 싶어해요.")
        elif score == 8:
            lbone.config(text="내 차는 내가 관리한다. 잘 관리된 차의 오너")
            lbblank.config(text="")
            testpic = tk.PhotoImage(file="%s" % recom_car2("중형 세단"), master=testnext)
            lbtestpic = tk.Label(testframe, image=testpic)
            lbtestpic.pack()
            lbtwo.config(text="어울리는 차 : %s" % recom_car("중형 세단"))
            lbthree.config(text="어울리는 옵션 : 세차도구")
            lbfour.config(text="어울리는 도로 : 도시의 바쁨이 느껴지는 수도권 한복판")
            lbfive.config(
                text="운전에 큰 흥미없다. 운전할 시간에 스케줄 확인하거나 휴식을 취하는게 더 '효율적'일 것이라고 생각하는 편! 하지만 한번 관리를 시작하면 계획적이고 규칙적인 스타일이라 내 차의 물건은 꼭 내가 아는 그 자리에 있어야 직성이 풀리는 성격. 엔진오일은 물론 와이퍼, 타이어, 브레이크 패드 등등.. 내 차 소모품 주기를 철저히 챙겨요. 도시의 바쁜 일상을 나름 적응하며 즐기지만, 차가 조금이라도 막하는 걸 싫어해요.")
        elif score == 9:
            lbone.config(text="신차 나오면 제일 먼저 찾아보는 얼리카답터")
            lbblank.config(text="")
            testpic = tk.PhotoImage(file="%s" % recom_car2("스포츠카 컨버터블"), master=testnext)
            lbtestpic = tk.Label(testframe, image=testpic)
            lbtestpic.pack()
            lbtwo.config(text="어울리는 차 : %s" % recom_car("스포츠카 컨버터블"))
            lbthree.config(text="어울리는 옵션 : 팔콘 도어")
            lbfour.config(text="어울리는 도로 : 방금 깔린 아스팔트 위")
            lbfive.config(
                text="신차가 나오면 시승기를 찾아보는게 제일 재밌는 당신! 스포츠 게임을 좋아하기 때문에 운전도 나름대로 재미를 느끼네요. 새로운 것에 대한 욕구가 강하기 때문에 어디 재밌는 곳이 생겼다고 하면 꼭 찾아가고 싶어하는 당신. 경쟁심이 있어서 운전을 잘하고 못하고를 떠나서 내 주변에 있는 '누구'보단 잘하고 싶어해요.")
        elif score == 10:
            lbone.config(text="나만의 세계 마이웨이")
            lbblank.config(text="")
            testpic = tk.PhotoImage(file="%s" % recom_car2("준중형 해치백"), master=testnext)
            lbtestpic = tk.Label(testframe, image=testpic)
            lbtestpic.pack()
            lbtwo.config(text="어울리는 차 : %s" % recom_car("준중형 해치백"))
            lbthree.config(text="어울리는 옵션 : 나만 아는 음악")
            lbfour.config(text="어울리는 도로 : 방금 깔린 아스팔트 위")
            lbfive.config(
                text="지금 무슨 차를 탔던 간에 사람들이 추천한 차보다 자신이 원했던 차를 샀을 유형. 다른 사람의 기준에 맞추기보단 나만의 기준이 확실해요. 관대하고 너그러운 마음씨를 가지고 있어서 동승자가 내 차에 타서 차를 더럽히거나 이것저것 만져서 거슬려도 크게 뭐라고 하지 않아요. 하지만 차 밖에 있는 얌체같은 운전자들에겐 혼잣말로 궁시렁 대는 타입.")
        testnext.mainloop()
    def retry():
        answer1.get() == 0
        answer2.get() == 0
        answer3.get() == 0
        answer4.get() == 0
        answer5.get() == 0
        answer6.get() == 0
        answer7.get() == 0
        answer8.get() == 0
        answer9.get() == 0
        answer10.get() == 0
        btn0.config(text="다음", command=nxstep)
        lb4.config(text="질문 1. 내 차의 청결상태는?")
        rad1.config(text="누가봐도 깔끔하게 항상 정돈되어 있다.", variable=answer1, value=0)
        rad2.config(text="어제 먹다 남은 음료수 캔도 그대로 남아있다.", variable=answer1, value=1)
        rad1.select()
        rad2.deselect()

    lb1 = tk.Label(test, text="운전 성향 테스트", bg="yellow")
    lb1.grid(row=0, column=0)
    lb2 = tk.Label(test, text="다음 질문의 두가지 선택사항 중 하나를 선택해 주세요.")
    lb2.grid(row=1, column=0)
    lb3 = tk.Label(test)
    lb3.grid(row=2, column=0)
    lb4 = tk.Label(test, text="질문 1. 내 차의 청결상태는?")
    lb4.grid(row=3, column=0, sticky="w")

    answer1 = tk.IntVar()
    answer2 = tk.IntVar()
    answer3 = tk.IntVar()
    answer4 = tk.IntVar()
    answer5 = tk.IntVar()
    answer6 = tk.IntVar()
    answer7 = tk.IntVar()
    answer8 = tk.IntVar()
    answer9 = tk.IntVar()
    answer10 = tk.IntVar()

    rad1 = tk.Radiobutton(test, text="누가봐도 깔끔하게 항상 정돈되어 있다.", variable=answer1, value=0)
    rad1.grid(row=4, column=0, sticky="w")
    rad2 = tk.Radiobutton(test, text="어제 먹다 남은 음료수 캔도 그대로 남아있다.", variable=answer1, value=1)
    rad2.grid(row=5, column=0, sticky="w")

    def nxstep():
        if lb4.cget("text") == "질문 1. 내 차의 청결상태는?":
            lb4.config(text="질문 2. 차를 타다 미세한 문콕을 발견한 나는")
            rad1.config(text="찾는게 더 번거롭다. 그냥 넘어간다.", variable=answer2, value=0)
            rad2.config(text="블랙박스를 돌려 어떻게든 범인을 찾아낸다.", variable=answer2, value=1)
            rad1.select()
            rad2.deselect()
            btn1.grid(row=34, column=0, sticky="w", padx=10, pady=5)
        elif lb4.cget("text") == "질문 2. 차를 타다 미세한 문콕을 발견한 나는":
            lb4.config(text="질문 3. 나는 차에서 노래를")
            rad1.config(text="그냥 허전해서 듣는다.", variable=answer3, value=0)
            rad2.config(text="노래방보다 더 신나게 부른다.", variable=answer3, value=1)
            rad1.select()
            rad2.deselect()
            btn1.grid(row=34, column=0, sticky="w", padx=10, pady=5)
        elif lb4.cget("text") == "질문 3. 나는 차에서 노래를":
            lb4.config(text="질문 4. 힘겹게 끼어들기하려는 차량이 있다면?")
            rad1.config(text="초보인가? 불쌍해서 넣어준다.", variable=answer4, value=0)
            rad2.config(text="상습범이 분명해! 절대 안 넣어준다.", variable=answer4, value=1)
            rad1.select()
            rad2.deselect()
            btn1.grid(row=34, column=0, sticky="w", padx=10, pady=5)
        elif lb4.cget("text") == "질문 4. 힘겹게 끼어들기하려는 차량이 있다면?":
            lb4.config(text="질문 5. 내비게이션이 알려주는 길을")
            rad1.config(text="거의 다 따라서 간다.", variable=answer5, value=0)
            rad2.config(text="내가 더 빠르다고 생각하는 길을 간다.", variable=answer5, value=1)
            rad1.select()
            rad2.deselect()
            btn1.grid(row=34, column=0, sticky="w", padx=10, pady=5)
        elif lb4.cget("text") == "질문 5. 내비게이션이 알려주는 길을":
            lb4.config(text="질문 6. 나는 조수석에 타면")
            rad1.config(text="군말없이 조용히 있는다.", variable=answer6, value=0)
            rad2.config(text="인간 내비게이션이 되어 운전자를 도와준다.", variable=answer6, value=1)
            rad1.select()
            rad2.deselect()
            btn1.grid(row=34, column=0, sticky="w", padx=10, pady=5)
        elif lb4.cget("text") == "질문 6. 나는 조수석에 타면":
            lb4.config(text="질문 7. 내 차에 있는 기능을")
            rad1.config(text="쓰는 것만 쓴다.", variable=answer7, value=0)
            rad2.config(text="한번씩 다 써보려고 한다.", variable=answer7, value=1)
            rad1.select()
            rad2.deselect()
            btn1.grid(row=34, column=0, sticky="w", padx=10, pady=5)
        elif lb4.cget("text") == "질문 7. 내 차에 있는 기능을":
            lb4.config(text="질문 8. 나는 약속시간을")
            rad1.config(text="교통체증까지 미리 계산해서 지킨다.", variable=answer8, value=0)
            rad2.config(text="5분 이상 늦는 편이다.", variable=answer8, value=1)
            rad1.select()
            rad2.deselect()
            btn1.grid(row=34, column=0, sticky="w", padx=10, pady=5)
        elif lb4.cget("text") == "질문 8. 나는 약속시간을":
            lb4.config(text="질문 9. 내가 생각하는 내 운전실력은")
            rad1.config(text="잘하진 않는다. 조심히 한다.", variable=answer9, value=0)
            rad2.config(text="운전경력에 비해 꽤나 잘한다.", variable=answer9, value=1)
            rad1.select()
            rad2.deselect()
            btn1.grid(row=34, column=0, sticky="w", padx=10, pady=5)
        elif lb4.cget("text") == "질문 9. 내가 생각하는 내 운전실력은":
            lb4.config(text="질문 10. 지인이 사고가 났다면 내가 할 말은")
            rad1.config(text="어디 다치신데는 없으셨어요?", variable=answer10, value=0)
            rad2.config(text="보험은 드셨어요?", variable=answer10, value=1)
            rad1.select()
            rad2.deselect()
            btn1.grid(row=34, column=0, sticky="w", padx=10, pady=5)
        elif lb4.cget("text") == "질문 10. 지인이 사고가 났다면 내가 할 말은":
            btn0.config(text="완료", command=result)
            btn1.grid(row=34, column=0, sticky="w", padx=10, pady=5)

    def bfstep():
        if lb4.cget("text") == "질문 2. 차를 타다 미세한 문콕을 발견한 나는":
            lb4.config(text="질문 1. 내 차의 청결상태는?")
            rad1.config(text="누가봐도 깔끔하게 항상 정돈되어 있다.", variable=answer1, value=0)
            rad2.config(text="어제 먹다 남은 음료수 캔도 그대로 남아있다.", variable=answer1, value=1)
            btn1.grid_forget()
            btn0.config(text="다음", command=nxstep)
        elif lb4.cget("text") == "질문 3. 나는 차에서 노래를":
            lb4.config(text="질문 2. 차를 타다 미세한 문콕을 발견한 나는")
            rad1.config(text="찾는게 더 번거롭다. 그냥 넘어간다.", variable=answer2, value=0)
            rad2.config(text="블랙박스를 돌려 어떻게든 범인을 찾아낸다.", variable=answer2, value=1)
            btn0.config(text="다음", command=nxstep)
        elif lb4.cget("text") == "질문 4. 힘겹게 끼어들기하려는 차량이 있다면?":
            lb4.config(text="질문 3. 나는 차에서 노래를")
            rad1.config(text="그냥 허전해서 듣는다.", variable=answer3, value=0)
            rad2.config(text="노래방보다 더 신나게 부른다.", variable=answer3, value=1)
            btn0.config(text="다음", command=nxstep)
        elif lb4.cget("text") == "질문 5. 내비게이션이 알려주는 길을":
            lb4.config(text="질문 4. 힘겹게 끼어들기하려는 차량이 있다면?")
            rad1.config(text="초보인가? 불쌍해서 넣어준다.", variable=answer4, value=0)
            rad2.config(text="상습범이 분명해! 절대 안 넣어준다.", variable=answer4, value=1)
            btn0.config(text="다음", command=nxstep)
        elif lb4.cget("text") == "질문 6. 나는 조수석에 타면":
            lb4.config(text="질문 5. 내비게이션이 알려주는 길을")
            rad1.config(text="거의 다 따라서 간다.", variable=answer5, value=0)
            rad2.config(text="내가 더 빠르다고 생각하는 길을 간다.", variable=answer5, value=1)
            btn0.config(text="다음", command=nxstep)
        elif lb4.cget("text") == "질문 7. 내 차에 있는 기능을":
            lb4.config(text="질문 6. 나는 조수석에 타면")
            rad1.config(text="군말없이 조용히 있는다.", variable=answer6, value=0)
            rad2.config(text="인간 내비게이션이 되어 운전자를 도와준다.", variable=answer6, value=1)
            btn0.config(text="다음", command=nxstep)
        elif lb4.cget("text") == "질문 8. 나는 약속시간을":
            lb4.config(text="질문 7. 내 차에 있는 기능을")
            rad1.config(text="쓰는 것만 쓴다.", variable=answer7, value=0)
            rad2.config(text="한번씩 다 써보려고 한다.", variable=answer7, value=1)
            btn0.config(text="다음", command=nxstep)
        elif lb4.cget("text") == "질문 9. 내가 생각하는 내 운전실력은":
            lb4.config(text="질문 8. 나는 약속시간을")
            rad1.config(text="교통체증까지 미리 계산해서 지킨다.", variable=answer8, value=0)
            rad2.config(text="5분 이상 늦는 편이다.", variable=answer8, value=1)
            btn0.config(text="다음", command=nxstep)
        elif lb4.cget("text") == "질문 10. 지인이 사고가 났다면 내가 할 말은":
            lb4.config(text="질문 9. 내가 생각하는 내 운전실력은")
            rad1.config(text="잘하진 않는다. 조심히 한다.", variable=answer9, value=0)
            rad2.config(text="운전경력에 비해 꽤나 잘한다.", variable=answer9, value=1)
            btn0.config(text="다음", command=nxstep)

    btn0 = tk.Button(test, text="다음", command=nxstep)
    btn0.grid(row=33, column=0, sticky="w", padx=10, pady=5)
    btn1 = tk.Button(test, text="뒤로가기", command=bfstep)
    btn2 = tk.Button(test, text="다시하기", command=retry)
    btn2.grid(row=35, column=0, sticky="w", padx=10, pady=5)
    btn3 = tk.Button(test, text="나가기", command=close3)
    btn3.grid(row=36, column=0, sticky="w", padx=10, pady=5)
    test.mainloop()
    win.mainloop()

def close4():
    w0.destroy()

def nextpage4():
    global w0
    w0 = Toplevel(win)
    w0.title('나만의 차 만들기')
    w0.geometry("1080x960")
    w0.resizable(False, False)
    frameone = tk.Frame(w0)
    frameone.pack()
    frametwo = tk.Frame(w0)
    frametwo.pack()

    def SportCar():
        w = Toplevel(w0)
        w.title("나만의 차 만들기_스포츠카")
        w.geometry("800x800+200+200")
        photowheel1 = tk.PhotoImage(file="./3조/911/1번휠.png")
        photowheel2 = tk.PhotoImage(file="./3조/911/2번휠.png")
        photowheel3 = tk.PhotoImage(file="./3조/911/3번휠.png")
        photoyellow = tk.PhotoImage(file="./3조/911/노.png")
        photored = tk.PhotoImage(file="./3조/911/빨.png")
        photoblack = tk.PhotoImage(file="./3조/911/검.png")
        photowhite = tk.PhotoImage(file="./3조/911/흰.png")
        photobasic = tk.PhotoImage(file="./3조/911/흰3.png")
        label0 = tk.Label(w, text="원하는 옵션을 선택해보세요!", bg="orange")
        label0.pack()
        label1 = tk.Label(w, image=photobasic)
        label1.pack()
        link = Label(w, text='이미지 출처 : 포르쉐 코리아(https://www.porsche.com/korea/ko/)', font=('Helveticabold', 8), fg="blue", cursor="hand2")
        link.pack(side='bottom')
        link.bind("<Button-1>", lambda e:
        callback('https://cc.porsche.com/icc/ccCall.do?rt=1651542378&screen=1920x1080&userID=PAKKE&lang=ke&PARAM=parameter_internet_ke&ORDERTYPE=992110&CNR=C39&MODELYEAR=2022&hookURL=https%3a%2f%2fwww.porsche.com%2fkorea%2fko%2fmodelstart%2fall%2f'))
        frame_2 = tk.Frame(w)
        frame_2.pack(side='bottom')
        frame_1 = tk.Frame(w)
        frame_1.pack(side='left')
        frame_3 = tk.Frame(w)
        frame_3.pack(side='right')

        def yellow():
            global btnwheel1
            global btnwheel2
            global btnwheel3
            btnwheel1 = tk.Button(frame_3, image=photowheel1, command=change_yellow1)
            btnwheel1.grid(row=0, column=1)
            btnwheel2 = tk.Button(frame_3, image=photowheel2, command=change_yellow2)
            btnwheel2.grid(row=0, column=2)
            btnwheel3 = tk.Button(frame_3, image=photowheel3, command=change_yellow3)
            btnwheel3.grid(row=0, column=3)
            label3 = tk.Label(frame_3, text="휠 선택")
            label3.grid(row=0, column=0)
            change_yellow1()
            change_yellow2()
            change_yellow3()

        def change_yellow1():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/911/노1.png")
            label1.config(image=photo1)

        def change_yellow2():
            global photo2
            photo2 = tk.PhotoImage(file="./3조/911/노2.png")
            label1.config(image=photo2)

        def change_yellow3():
            global photo3
            photo3 = tk.PhotoImage(file="./3조/911/노3.png")
            label1.config(image=photo3)

        def red():
            global btnwheel1
            global btnwheel2
            global btnwheel3
            btnwheel1 = tk.Button(frame_3, image=photowheel1, command=change_red1)
            btnwheel1.grid(row=0, column=1)
            btnwheel2 = tk.Button(frame_3, image=photowheel2, command=change_red2)
            btnwheel2.grid(row=0, column=2)
            btnwheel3 = tk.Button(frame_3, image=photowheel3, command=change_red3)
            btnwheel3.grid(row=0, column=3)
            label3 = tk.Label(frame_3, text="휠 선택")
            label3.grid(row=0, column=0)
            change_red1()
            change_red2()
            change_red3()

        def change_red1():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/911/빨1.png")
            label1.config(image=photo1)

        def change_red2():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/911/빨2.png")
            label1.config(image=photo1)

        def change_red3():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/911/빨3.png")
            label1.config(image=photo1)

        def black():
            global btnwheel1
            global btnwheel2
            global btnwheel3
            btnwheel1 = tk.Button(frame_3, image=photowheel1, command=change_black1)
            btnwheel1.grid(row=0, column=1)
            btnwheel2 = tk.Button(frame_3, image=photowheel2, command=change_black2)
            btnwheel2.grid(row=0, column=2)
            btnwheel3 = tk.Button(frame_3, image=photowheel3, command=change_black3)
            btnwheel3.grid(row=0, column=3)
            label3 = tk.Label(frame_3, text="휠 선택")
            label3.grid(row=0, column=0)
            change_black1()
            change_black2()
            change_black3()

        def change_black1():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/911/검1.png")
            label1.config(image=photo1)

        def change_black2():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/911/검2.png")
            label1.config(image=photo1)

        def change_black3():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/911/검3.png")
            label1.config(image=photo1)

        def white():
            global btnwheel1
            global btnwheel2
            global btnwheel3
            btnwheel1 = tk.Button(frame_3, image=photowheel1, command=change_white1)
            btnwheel1.grid(row=0, column=1)
            btnwheel2 = tk.Button(frame_3, image=photowheel2, command=change_white2)
            btnwheel2.grid(row=0, column=2)
            btnwheel3 = tk.Button(frame_3, image=photowheel3, command=change_white3)
            btnwheel3.grid(row=0, column=3)
            label3 = tk.Label(frame_3, text="휠 선택")
            label3.grid(row=0, column=0)
            change_white1()
            change_white2()
            change_white3()

        def change_white1():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/911/흰1.png")
            label1.config(image=photo1)

        def change_white2():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/911/흰2.png")
            label1.config(image=photo1)

        def change_white3():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/911/흰3.png")
            label1.config(image=photo1)

        label2 = tk.Label(frame_1, text="색상 선택")
        label2.grid(row=0, column=0)
        btnyellow = tk.Button(frame_1, image=photoyellow, command=yellow)
        btnyellow.grid(row=0, column=1)
        btnred = tk.Button(frame_1, image=photored, command=red)
        btnred.grid(row=0, column=2)
        btnblack = tk.Button(frame_1, image=photoblack, command=black)
        btnblack.grid(row=0, column=3)
        btnwhite = tk.Button(frame_1, image=photowhite, command=white)
        btnwhite.grid(row=0, column=4)

        def Deiconify():
            w2.deiconify()

        def destroyW2():
            w2.withdraw()
            btninmycar.destroy()
            btninsideinput = tk.Button(frame_2, text="적용화면 보기", command=Deiconify)
            btninsideinput.grid(row=0, column=0)

        def nextstep():
            global w2
            global btnwheel1
            global btnwheel2
            global btnwheel3
            global labelb
            global btnfin
            global framea
            w2 = Toplevel(w)
            w2.title("차량 내부 선택")
            w2.geometry("800x800+200+200")
            photoblackbeige = tk.PhotoImage(file="./3조/911/검베.png")
            photowine = tk.PhotoImage(file="./3조/911/와인.png")
            photoblackwhite = tk.PhotoImage(file="./3조/911/검흰.png")
            photobasicinside = tk.PhotoImage(file="./3조/911/검흰적용.png")
            labela = tk.Label(w2, text="원하는 내부옵션을 선택해보세요!", bg="orange")
            labela.pack()
            labelb = tk.Label(w2, image=photobasicinside)
            labelb.pack()
            link = Label(w2, text='이미지 출처 : 포르쉐 코리아(https://www.porsche.com/korea/ko/)', font=('Helveticabold', 8),
                         fg="blue", cursor="hand2")
            link.pack(side='bottom')
            link.bind("<Button-1>", lambda e:
            callback(
                'https://cc.porsche.com/icc/ccCall.do?rt=1651542378&screen=1920x1080&userID=PAKKE&lang=ke&PARAM=parameter_internet_ke&ORDERTYPE=992110&CNR=C39&MODELYEAR=2022&hookURL=https%3a%2f%2fwww.porsche.com%2fkorea%2fko%2fmodelstart%2fall%2f'))
            framea = tk.Frame(w2)
            framea.pack(side='bottom')
            frameb = tk.Frame(w2)
            frameb.pack(side='left')

            def change_blackbeige():
                global photo2
                photo2 = tk.PhotoImage(file="./3조/911/검베적용.png")
                labelb.config(image=photo2)

            def change_wine():
                global photo2
                photo2 = tk.PhotoImage(file="./3조/911/와인적용.png")
                labelb.config(image=photo2)

            def change_blackwhite():
                global photo2
                photo2 = tk.PhotoImage(file="./3조/911/검흰적용.png")
                labelb.config(image=photo2)

            labelc = tk.Label(frameb, text="색상 선택")
            labelc.grid(row=0, column=0)

            btnwheel1 = tk.Button(frameb, image=photoblackbeige, command=change_blackbeige)
            btnwheel1.grid(row=0, column=1)
            btnwheel2 = tk.Button(frameb, image=photowine, command=change_wine)
            btnwheel2.grid(row=0, column=2)
            btnwheel3 = tk.Button(frameb, image=photoblackwhite, command=change_blackwhite)
            btnwheel3.grid(row=0, column=3)

            btnfin = tk.Button(framea, text="적용하기", command=destroyW2)
            btnfin.grid(row=0, column=0)
            w0.mainloop()

        def destroyW():
            w.destroy()

        def finishmakingcar():
            label4 = tk.Label(frame_2, text="멋진 차가 만들어졌어요!")
            label4.grid(row=2, column=0)
            btnout = tk.Button(frame_2, text="나가기", command=destroyW)
            btnout.grid(row=3, column=0)

        btninmycar = tk.Button(frame_2, text="차량 내부 선택", command=nextstep)
        btninmycar.grid(row=0, column=0)
        btnfinish = tk.Button(frame_2, text="완료", command=finishmakingcar)
        btnfinish.grid(row=1, column=0)

        w0.mainloop()

    def Sedan():
        w = Toplevel(w0)
        w.title("나만의 차 만들기_세단")
        w.geometry("1000x900")
        photowheel1 = tk.PhotoImage(file="./3조/panamera/휠1.png")
        photowheel2 = tk.PhotoImage(file="./3조/panamera/휠2.png")
        photowheel3 = tk.PhotoImage(file="./3조/panamera/휠3.png")
        photoyellow = tk.PhotoImage(file="./3조/panamera/파.png")
        photored = tk.PhotoImage(file="./3조/panamera/빨.png")
        photoblack = tk.PhotoImage(file="./3조/panamera/검.png")
        photowhite = tk.PhotoImage(file="./3조/panamera/흰.png")
        photobasic = tk.PhotoImage(file="./3조/panamera/흰3.png")
        label0 = tk.Label(w, text="원하는 옵션을 선택해보세요!", bg="orange")
        label0.pack()
        label1 = tk.Label(w, image=photobasic)
        label1.pack()
        link = Label(w, text='이미지 출처 : 포르쉐 코리아(https://www.porsche.com/korea/ko/)', font=('Helveticabold', 8),
                     fg="blue", cursor="hand2")
        link.pack(side='bottom')
        link.bind("<Button-1>", lambda e:
        callback('https://cc.porsche.com/icc/ccCall.do?rt=1651542744&screen=1920x1080&userID=PAKKE&lang=ke&PARAM=parameter_internet_ke&ORDERTYPE=97ABI1&CNR=C39&MODELYEAR=2023&hookURL=https%3a%2f%2fwww.porsche.com%2fkorea%2fko%2fmodelstart%2fall%2f'))
        frame_2 = tk.Frame(w)
        frame_2.pack(side='bottom')
        frame_1 = tk.Frame(w)
        frame_1.pack(side='left')
        frame_3 = tk.Frame(w)
        frame_3.pack(side='right')

        def yellow():
            global btnwheel1
            global btnwheel2
            global btnwheel3
            btnwheel1 = tk.Button(frame_3, image=photowheel1, command=change_yellow1)
            btnwheel1.grid(row=0, column=1)
            btnwheel2 = tk.Button(frame_3, image=photowheel2, command=change_yellow2)
            btnwheel2.grid(row=0, column=2)
            btnwheel3 = tk.Button(frame_3, image=photowheel3, command=change_yellow3)
            btnwheel3.grid(row=0, column=3)
            label3 = tk.Label(frame_3, text="휠 선택")
            label3.grid(row=0, column=0)
            change_yellow1()
            change_yellow2()
            change_yellow3()

        def change_yellow1():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/panamera/파1.png")
            label1.config(image=photo1)

        def change_yellow2():
            global photo2
            photo2 = tk.PhotoImage(file="./3조/panamera/파2.png")
            label1.config(image=photo2)

        def change_yellow3():
            global photo3
            photo3 = tk.PhotoImage(file="./3조/panamera/파3.png")
            label1.config(image=photo3)

        def red():
            global btnwheel1
            global btnwheel2
            global btnwheel3
            btnwheel1 = tk.Button(frame_3, image=photowheel1, command=change_red1)
            btnwheel1.grid(row=0, column=1)
            btnwheel2 = tk.Button(frame_3, image=photowheel2, command=change_red2)
            btnwheel2.grid(row=0, column=2)
            btnwheel3 = tk.Button(frame_3, image=photowheel3, command=change_red3)
            btnwheel3.grid(row=0, column=3)
            label3 = tk.Label(frame_3, text="휠 선택")
            label3.grid(row=0, column=0)
            change_red1()
            change_red2()
            change_red3()

        def change_red1():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/panamera/빨1.png")
            label1.config(image=photo1)

        def change_red2():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/panamera/빨2.png")
            label1.config(image=photo1)

        def change_red3():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/panamera/빨3.png")
            label1.config(image=photo1)

        def black():
            global btnwheel1
            global btnwheel2
            global btnwheel3
            btnwheel1 = tk.Button(frame_3, image=photowheel1, command=change_black1)
            btnwheel1.grid(row=0, column=1)
            btnwheel2 = tk.Button(frame_3, image=photowheel2, command=change_black2)
            btnwheel2.grid(row=0, column=2)
            btnwheel3 = tk.Button(frame_3, image=photowheel3, command=change_black3)
            btnwheel3.grid(row=0, column=3)
            label3 = tk.Label(frame_3, text="휠 선택")
            label3.grid(row=0, column=0)
            change_black1()
            change_black2()
            change_black3()

        def change_black1():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/panamera/검1.png")
            label1.config(image=photo1)

        def change_black2():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/panamera/검2.png")
            label1.config(image=photo1)

        def change_black3():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/panamera/검3.png")
            label1.config(image=photo1)

        def white():
            global btnwheel1
            global btnwheel2
            global btnwheel3
            btnwheel1 = tk.Button(frame_3, image=photowheel1, command=change_white1)
            btnwheel1.grid(row=0, column=1)
            btnwheel2 = tk.Button(frame_3, image=photowheel2, command=change_white2)
            btnwheel2.grid(row=0, column=2)
            btnwheel3 = tk.Button(frame_3, image=photowheel3, command=change_white3)
            btnwheel3.grid(row=0, column=3)
            label3 = tk.Label(frame_3, text="휠 선택")
            label3.grid(row=0, column=0)
            change_white1()
            change_white2()
            change_white3()

        def change_white1():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/panamera/흰1.png")
            label1.config(image=photo1)

        def change_white2():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/panamera/흰2.png")
            label1.config(image=photo1)

        def change_white3():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/panamera/흰3.png")
            label1.config(image=photo1)

        label2 = tk.Label(frame_1, text="색상 선택")
        label2.grid(row=0, column=0)
        btnyellow = tk.Button(frame_1, image=photoyellow, command=yellow)
        btnyellow.grid(row=0, column=1)
        btnred = tk.Button(frame_1, image=photored, command=red)
        btnred.grid(row=0, column=2)
        btnblack = tk.Button(frame_1, image=photoblack, command=black)
        btnblack.grid(row=0, column=3)
        btnwhite = tk.Button(frame_1, image=photowhite, command=white)
        btnwhite.grid(row=0, column=4)

        def Deiconify():
            w2.deiconify()

        def destroyW2():
            w2.withdraw()
            btninmycar.destroy()
            btninsideinput = tk.Button(frame_2, text="적용화면 보기", command=Deiconify)
            btninsideinput.grid(row=0, column=0)

        def nextstep():
            global w2
            global btnwheel1
            global btnwheel2
            global btnwheel3
            global labelb
            w2 = Toplevel(w)
            w2.title("차량 내부 선택")
            w2.geometry("800x800+200+200")
            photoblackbeige = tk.PhotoImage(file="./3조/panamera/검빨.png")
            photowine = tk.PhotoImage(file="./3조/panamera/보베.png")
            photoblackwhite = tk.PhotoImage(file="./3조/panamera/검검.png")
            photobasicinside = tk.PhotoImage(file="./3조/panamera/검적용.png")
            labela = tk.Label(w2, text="원하는 내부옵션을 선택해보세요!", bg="orange")
            labela.pack()
            labelb = tk.Label(w2, image=photobasicinside)
            labelb.pack()
            link = Label(w2, text='이미지 출처 : 포르쉐 코리아(https://www.porsche.com/korea/ko/)', font=('Helveticabold', 8),
                         fg="blue", cursor="hand2")
            link.pack(side='bottom')
            link.bind("<Button-1>", lambda e:
            callback(
                'https://cc.porsche.com/icc/ccCall.do?rt=1651542744&screen=1920x1080&userID=PAKKE&lang=ke&PARAM=parameter_internet_ke&ORDERTYPE=97ABI1&CNR=C39&MODELYEAR=2023&hookURL=https%3a%2f%2fwww.porsche.com%2fkorea%2fko%2fmodelstart%2fall%2f'))
            framea = tk.Frame(w2)
            framea.pack(side='bottom')
            frameb = tk.Frame(w2)
            frameb.pack(side='left')

            def change_blackbeige():
                global photo2
                photo2 = tk.PhotoImage(file="./3조/panamera/검빨적용.png")
                labelb.config(image=photo2)

            def change_wine():
                global photo2
                photo2 = tk.PhotoImage(file="./3조/panamera/보베적용.png")
                labelb.config(image=photo2)

            def change_blackwhite():
                global photo2
                photo2 = tk.PhotoImage(file="./3조/panamera/검적용.png")
                labelb.config(image=photo2)

            labelc = tk.Label(frameb, text="색상 선택")
            labelc.grid(row=0, column=0)

            btnwheel1 = tk.Button(frameb, image=photoblackbeige, command=change_blackbeige)
            btnwheel1.grid(row=0, column=1)
            btnwheel2 = tk.Button(frameb, image=photowine, command=change_wine)
            btnwheel2.grid(row=0, column=2)
            btnwheel3 = tk.Button(frameb, image=photoblackwhite, command=change_blackwhite)
            btnwheel3.grid(row=0, column=3)

            btnfin = tk.Button(framea, text="적용하기", command=destroyW2)
            btnfin.grid(row=0, column=0)
            w0.mainloop()

        def destroyW():
            w.destroy()

        def finishmakingcar():
            label4 = tk.Label(frame_2, text="멋진 차가 만들어졌어요!")
            label4.grid(row=2, column=0)
            btnout = tk.Button(frame_2, text="나가기", command=destroyW)
            btnout.grid(row=3, column=0)

        btninmycar = tk.Button(frame_2, text="차량 내부 선택", command=nextstep)
        btninmycar.grid(row=0, column=0)
        btnfinish = tk.Button(frame_2, text="완료", command=finishmakingcar)
        btnfinish.grid(row=1, column=0)

        w0.mainloop()

    def SUV():
        w = Toplevel(w0)
        w.title("나만의 차 만들기_SUV")
        w.geometry("1000x900")
        photowheel1 = tk.PhotoImage(file="./3조/Cayenne/휠1.png")
        photowheel2 = tk.PhotoImage(file="./3조/Cayenne/휠2.png")
        photowheel3 = tk.PhotoImage(file="./3조/Cayenne/휠3.png")
        photoyellow = tk.PhotoImage(file="./3조/Cayenne/파.png")
        photored = tk.PhotoImage(file="./3조/Cayenne/빨.png")
        photoblack = tk.PhotoImage(file="./3조/Cayenne/검.png")
        photowhite = tk.PhotoImage(file="./3조/Cayenne/흰.png")
        photobasic = tk.PhotoImage(file="./3조/Cayenne/흰3.png")
        label0 = tk.Label(w, text="원하는 옵션을 선택해보세요!", bg="orange")
        label0.pack()
        label1 = tk.Label(w, image=photobasic)
        label1.pack()
        link = Label(w, text='이미지 출처 : 포르쉐 코리아(https://www.porsche.com/korea/ko/)', font=('Helveticabold', 8),
                     fg="blue", cursor="hand2")
        link.pack(side='bottom')
        link.bind("<Button-1>", lambda e:
        callback(
            'https://cc.porsche.com/icc/ccCall.do?rt=1651542908&screen=1920x1080&userID=PAKKE&lang=ke&PARAM=parameter_internet_ke&ORDERTYPE=9YAAA1&CNR=C39&MODELYEAR=2023&hookURL=https%3a%2f%2fwww.porsche.com%2fkorea%2fko%2fmodelstart%2fall%2f'))
        frame_2 = tk.Frame(w)
        frame_2.pack(side='bottom')
        frame_1 = tk.Frame(w)
        frame_1.pack(side='left')
        frame_3 = tk.Frame(w)
        frame_3.pack(side='right')

        def yellow():
            global btnwheel1
            global btnwheel2
            global btnwheel3
            btnwheel1 = tk.Button(frame_3, image=photowheel1, command=change_yellow1)
            btnwheel1.grid(row=0, column=1)
            btnwheel2 = tk.Button(frame_3, image=photowheel2, command=change_yellow2)
            btnwheel2.grid(row=0, column=2)
            btnwheel3 = tk.Button(frame_3, image=photowheel3, command=change_yellow3)
            btnwheel3.grid(row=0, column=3)
            label3 = tk.Label(frame_3, text="휠 선택")
            label3.grid(row=0, column=0)
            change_yellow1()
            change_yellow2()
            change_yellow3()

        def change_yellow1():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/Cayenne/파1.png")
            label1.config(image=photo1)

        def change_yellow2():
            global photo2
            photo2 = tk.PhotoImage(file="./3조/Cayenne/파2.png")
            label1.config(image=photo2)

        def change_yellow3():
            global photo3
            photo3 = tk.PhotoImage(file="./3조/Cayenne/파3.png")
            label1.config(image=photo3)

        def red():
            global btnwheel1
            global btnwheel2
            global btnwheel3
            btnwheel1 = tk.Button(frame_3, image=photowheel1, command=change_red1)
            btnwheel1.grid(row=0, column=1)
            btnwheel2 = tk.Button(frame_3, image=photowheel2, command=change_red2)
            btnwheel2.grid(row=0, column=2)
            btnwheel3 = tk.Button(frame_3, image=photowheel3, command=change_red3)
            btnwheel3.grid(row=0, column=3)
            label3 = tk.Label(frame_3, text="휠 선택")
            label3.grid(row=0, column=0)
            change_red1()
            change_red2()
            change_red3()

        def change_red1():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/Cayenne/빨1.png")
            label1.config(image=photo1)

        def change_red2():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/Cayenne/빨2.png")
            label1.config(image=photo1)

        def change_red3():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/Cayenne/빨3.png")
            label1.config(image=photo1)

        def black():
            global btnwheel1
            global btnwheel2
            global btnwheel3
            btnwheel1 = tk.Button(frame_3, image=photowheel1, command=change_black1)
            btnwheel1.grid(row=0, column=1)
            btnwheel2 = tk.Button(frame_3, image=photowheel2, command=change_black2)
            btnwheel2.grid(row=0, column=2)
            btnwheel3 = tk.Button(frame_3, image=photowheel3, command=change_black3)
            btnwheel3.grid(row=0, column=3)
            label3 = tk.Label(frame_3, text="휠 선택")
            label3.grid(row=0, column=0)
            change_black1()
            change_black2()
            change_black3()

        def change_black1():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/Cayenne/검1.png")
            label1.config(image=photo1)

        def change_black2():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/Cayenne/검2.png")
            label1.config(image=photo1)

        def change_black3():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/Cayenne/검3.png")
            label1.config(image=photo1)

        def white():
            global btnwheel1
            global btnwheel2
            global btnwheel3
            btnwheel1 = tk.Button(frame_3, image=photowheel1, command=change_white1)
            btnwheel1.grid(row=0, column=1)
            btnwheel2 = tk.Button(frame_3, image=photowheel2, command=change_white2)
            btnwheel2.grid(row=0, column=2)
            btnwheel3 = tk.Button(frame_3, image=photowheel3, command=change_white3)
            btnwheel3.grid(row=0, column=3)
            label3 = tk.Label(frame_3, text="휠 선택")
            label3.grid(row=0, column=0)
            change_white1()
            change_white2()
            change_white3()

        def change_white1():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/Cayenne/흰1.png")
            label1.config(image=photo1)

        def change_white2():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/Cayenne/흰2.png")
            label1.config(image=photo1)

        def change_white3():
            global photo1
            photo1 = tk.PhotoImage(file="./3조/Cayenne/흰3.png")
            label1.config(image=photo1)

        label2 = tk.Label(frame_1, text="색상 선택")
        label2.grid(row=0, column=0)
        btnyellow = tk.Button(frame_1, image=photoyellow, command=yellow)
        btnyellow.grid(row=0, column=1)
        btnred = tk.Button(frame_1, image=photored, command=red)
        btnred.grid(row=0, column=2)
        btnblack = tk.Button(frame_1, image=photoblack, command=black)
        btnblack.grid(row=0, column=3)
        btnwhite = tk.Button(frame_1, image=photowhite, command=white)
        btnwhite.grid(row=0, column=4)


        def Deiconify():
            w2.deiconify()
        def destroyW2():
            w2.withdraw()
            btninmycar.destroy()
            btninsideinput = tk.Button(frame_2, text="적용화면 보기", command=Deiconify)
            btninsideinput.grid(row=0, column=0)
        def nextstep():
            global w2
            global btnwheel1
            global btnwheel2
            global btnwheel3
            global labelb
            w2 = Toplevel(w)
            w2.title("차량 내부 선택")
            w2.geometry("800x800+200+200")
            #w2.deiconify()
            photoblackbeige = tk.PhotoImage(file="./3조/Cayenne/네흰.png")
            photowine = tk.PhotoImage(file="./3조/Cayenne/검빨.png")
            photoblackwhite = tk.PhotoImage(file="./3조/Cayenne/검베.png")
            photobasicinside = tk.PhotoImage(file="./3조/Cayenne/검베적용.png")
            labela = tk.Label(w2, text="원하는 내부옵션을 선택해보세요!", bg="orange")
            labela.pack()
            labelb = tk.Label(w2, image=photobasicinside)
            labelb.pack()
            link = Label(w2, text='이미지 출처 : 포르쉐 코리아(https://www.porsche.com/korea/ko/)', font=('Helveticabold', 8),
                         fg="blue", cursor="hand2")
            link.pack(side='bottom')
            link.bind("<Button-1>", lambda e:
            callback(
                'https://cc.porsche.com/icc/ccCall.do?rt=1651542908&screen=1920x1080&userID=PAKKE&lang=ke&PARAM=parameter_internet_ke&ORDERTYPE=9YAAA1&CNR=C39&MODELYEAR=2023&hookURL=https%3a%2f%2fwww.porsche.com%2fkorea%2fko%2fmodelstart%2fall%2f'))
            framea = tk.Frame(w2)
            framea.pack(side='bottom')
            frameb = tk.Frame(w2)
            frameb.pack(side='left')

            def change_blackbeige():
                global photo2
                photo2 = tk.PhotoImage(file="./3조/Cayenne/네흰적용.png")
                labelb.config(image=photo2)

            def change_wine():
                global photo2
                photo2 = tk.PhotoImage(file="./3조/Cayenne/검빨적용.png")
                labelb.config(image=photo2)

            def change_blackwhite():
                global photo2
                photo2 = tk.PhotoImage(file="./3조/Cayenne/검베적용.png")
                labelb.config(image=photo2)

            labelc = tk.Label(frameb, text="색상 선택")
            labelc.grid(row=0, column=0)

            btnwheel1 = tk.Button(frameb, image=photoblackbeige, command=change_blackbeige)
            btnwheel1.grid(row=0, column=1)
            btnwheel2 = tk.Button(frameb, image=photowine, command=change_wine)
            btnwheel2.grid(row=0, column=2)
            btnwheel3 = tk.Button(frameb, image=photoblackwhite, command=change_blackwhite)
            btnwheel3.grid(row=0, column=3)

            btnfin = tk.Button(framea, text="적용하기", command=destroyW2)
            btnfin.grid(row=0, column=0)
            w0.mainloop()


        def destroyW():
            w.destroy()

        def finishmakingcar():
            label4 = tk.Label(frame_2, text="멋진 차가 만들어졌어요!")
            label4.grid(row=2, column=0)
            btnout = tk.Button(frame_2, text="나가기", command=destroyW)
            btnout.grid(row=3, column=0)

        btninmycar = tk.Button(frame_2, text="차량 내부 선택", command=nextstep)
        btninmycar.grid(row=0, column=0)
        btnfinish = tk.Button(frame_2, text="완료", command=finishmakingcar)
        btnfinish.grid(row=1, column=0)
        w0.mainloop()

    photomain = tk.PhotoImage(file="./3조/911/배경화면.png")
    labelmain = tk.Label(frameone, image=photomain)
    labelmain.grid(row=0, column=0)
    labeltext = tk.Label(frameone, text="__decorating my car__", font=("Courier", 36, "italic"), bg="tan")
    labeltext.grid(row=0, column=0)
    btn1 = tk.Button(frametwo, width=29, height=10, text="Sport Car", font=("Courier", 15, "bold"), fg="black",
                     bg="slategray", command=SportCar)
    btn1.grid(row=3, column=3)
    btn2 = tk.Button(frametwo, width=29, height=10, text="Sedan", font=("Courier", 15, "bold"), fg="black", bg="wheat",
                     command=Sedan)
    btn2.grid(row=3, column=4)
    btn3 = tk.Button(frametwo, width=29, height=10, text="SUV", font=("Courier", 15, "bold"), fg="black",
                     bg="rosybrown", command=SUV)
    btn3.grid(row=3, column=5)
    w0.mainloop()

btn1=tk.Button(win,width=25,height=10,text="차량 추천",font=("bold",10,"bold"),fg="midnightblue",bg="lightblue",command=nextpage1)
btn1.grid(row=3, column=3)
btn2=tk.Button(win,width=25,height=10,text="내차 견적",font=("bold",10,"bold"),fg="darkslategrey",bg="mediumaquamarine", command=nextpage2)
btn2.grid(row=3, column=4)
btn3=tk.Button(win,width=25,height=10,text="운전성향 테스트",font=("bold",10,"bold"),fg="white",bg="cadetblue",command=nextpage3)
btn3.grid(row=3, column=5)
btn4=tk.Button(win,width=25,height=10,text="나만의 차 만들기",font=("bold",10,"bold"),fg="indigo",bg="thistle",command=nextpage4)
btn4.grid(row=3, column=6)

win.mainloop()