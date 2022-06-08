import tkinter as tk
import tkinter.ttk
from tkinter import messagebox


import IMP_SH as SH
import IMP_GY as GY

Passward_ch=['o']

def Login() :
    def Login_ch() :

        Passward=Login_ent1.get()

        import os.path
        path = ("Passward.txt")

        if os.path.isfile(path):
            file = open("Passward.txt.", "r", encoding="UTF-8")
            x=file.readlines()
            file.close()
            if Passward in x :
                Passward_ch=tk.messagebox.showinfo('알림', "로그인 성공")
                if Passward_ch :
                    Login.destroy()
                    a='o'
                    Login_res.append(a)
                else :
                    pass

            else :
                tk.messagebox.showerror('알림',"비밀번호가 맞지 않습니다.")

        else:
            PW="0000"
            file = open("Passward.txt.", "w", encoding="UTF-8")
            file.write(PW)
            file.close()

            Login_ch()

    def Login_ch_A(event):
        Login_ch()

    def Login_ch_B():
        Login_ch()

    global Passward_ch

    Login_res=[]

    Login = tk.Tk()
    Login.title("IMP_Login")
    Login.geometry("350x200")
    Login.resizable(False, False)

    tk.Label(Login, text="비밀번호 입력").place(x=130,y=40)
    Login_ent1=tk.Entry(Login, show='*')
    Login_ent1.place(x=103, y=70)
    Login_ent1.bind('<Return>',Login_ch_A)

    Login_btn1=tk.Button(Login, command=Login_ch_B, width=10, height=3, text="입력")
    Login_btn1.place(x=140, y=110)

    Login.mainloop()

    return Login_res

def Main() :

    def Manager_Login() :
        def Manager_Login_ch() :
            def Manager() :
                def center_up() :
                    m_f2.tkraise()
                def centerm_up() :
                    m_f2_1.tkraise()
                def centerc_up() :
                    m_f2_2.tkraise()

                def category_up() :
                    m_f3.tkraise()
                def categorym_up():
                    m_f3_1.tkraise()
                def categoryc_up():
                    m_f3_2.tkraise()

                def IMP_up():
                    m_f4.tkraise()
                def IMPpc_up():
                    m_f4_1.tkraise()
                def IMPmc_up():
                    m_f4_2.tkraise()

                def center_Make() :
                    def center_Make_A():
                        import os.path
                        path="0_CCN.txt"
                        if os.path.isfile(path):
                            x=SH.U_strTodic('0_CCN')
                            x[code]=[name]
                            a=SH.U_dicTostr(x)
                            file = open("0_CCN.txt", "w", encoding="UTF8")
                            file.write(str(a))
                            file.close()

                            GY.U_CI_file(code, name, adress, Vmax, Smax)
                            GY.U_IM_file(code)

                        else:
                            x={"코드명": ["지역명"]}
                            a=SH.U_dicTostr(x)
                            file=open("0_CCN.txt", "w", encoding="UTF-8")
                            file.write(str(a))
                            file.close()

                            center_Make_A()

                    name=m_f2_1ent1.get()
                    code=m_f2_1ent2.get()
                    adress=m_f2_1ent3.get()
                    Vmax=m_f2_1ent4.get()
                    Smax=m_f2_1ent5.get()
                    AA=[name, code, adress, Vmax, Smax]
                    if "" in AA:
                        tk.messagebox.showerror('에러', "공백이 존재합니다.")
                        manager.tkraise()
                    else:
                        tk.messagebox.showinfo('알림', "센터정보를 생성합니다.")
                        center_Make_A()
                        manager.tkraise()

                def center_c() :
                    name=m_f2_2ent1.get()
                    code=m_f2_2ent2.get()
                    adress=m_f2_2ent3.get()
                    Vmax=m_f2_2ent4.get()
                    Smax=m_f2_2ent5.get()

                    AA = [name, code, adress, Vmax, Smax]
                    if "" in AA:
                        tk.messagebox.showerror('에러', "공백이 존재합니다.")
                        manager.tkraise()

                    else:
                        import os.path
                        path = ("%sINFO_F.txt" % code)
                        if os.path.isfile(path):
                            a = SH.U_strTodic("%sINFO_F" % code)
                            del a[code]

                            a[code] = [name, adress, Vmax, Smax]
                            xx = SH.U_dicTostr(a)

                            file = open("%sINFO_F.txt" % code, "w", encoding="UTF8")
                            file.write(xx)
                            file.close()

                            tk.messagebox.showinfo('알림', "센터정보를 변경합니다.")
                            manager.tkraise()
                        else:
                            tk.messagebox.showerror('알림', '해당 코드명은 존재 하지 않습니다.')
                            manager.tkraise()

                def center_d() :

                    code=m_f2_2ent7.get()

                    if code == "":
                        tk.messagebox.showerror('에러', "코드명을 입력해주세요.")
                        manager.tkraise()

                    else:
                        import os.path
                        path = ('0_CCN.txt')
                        if os.path.isfile(path):
                            x = SH.U_strTodic('0_CCN')
                            del x[code]

                            xx = SH.U_dicTostr(x)
                            file = open("0_CCN.txt", "w", encoding="UTF-8")
                            file.write(xx)
                            file.close()

                            import os
                            os.remove("%sIMIP.txt" % code)
                            os.remove("%sIMOP.txt" % code)
                            os.remove("%sINFO_F.txt" % code)

                            tk.messagebox.showinfo('알림', "센터정보 삭제를 완료하였습니다.")
                            manager.tkraise()
                        else:
                            tk.messagebox.showerror('알림', '해당 코드명은 존재 하지 않습니다.')
                            manager.tkraise()

                def cate_make():
                    x={}

                    catemcode=m_f3_1ent1.get()
                    ma1=m_f3_1ent2.get()
                    ma2=m_f3_1ent3.get()
                    ma3=m_f3_1ent4.get()
                    ma4=m_f3_1ent5.get()
                    ma5=m_f3_1ent6.get()
                    ma6=m_f3_1ent7.get()
                    malla=[ma1, ma2, ma3, ma4, ma5, ma6]
                    mcatelist=[]

                    for i in malla:
                        if i == "":
                            del i
                        else:
                            mcatelist.append(i)

                    if catemcode != "" and malla.count("") != len(malla):
                        import os.path
                        path = "0_Category.txt"
                        if os.path.isfile(path):
                            x = SH.U_strTodic('0_Category')
                            x[catemcode] = mcatelist
                            xx = SH.U_dicTostr(x)
                            file = open("0_Category.txt", "w", encoding="UTF-8")
                            file.write(xx)
                            file.close()
                            pass
                        else:
                            x["카테고리명"] = ["카테고리목록"]
                            x[catemcode] = mcatelist
                            xx = SH.U_dicTostr(x)
                            file = open("0_Category.txt", "w", encoding="UTF-8")
                            file.write(xx)
                            file.close()
                        tk.messagebox.showinfo('알림', "카테고리를 생성 하였습니다.")
                        manager.tkraise()

                    else:
                        tk.messagebox.showerror('알림', "입력하신 내용을 확인해주세요.")
                        manager.tkraise()

                def cate_c() :

                    cateccode=m_f3_2ent1.get()
                    ca1=m_f3_2ent2.get()
                    ca2=m_f3_2ent3.get()
                    ca3=m_f3_2ent4.get()
                    ca4=m_f3_2ent5.get()
                    ca5=m_f3_2ent6.get()
                    ca6=m_f3_2ent7.get()
                    calla=[ca1, ca2, ca3, ca4, ca5, ca6]
                    ccatelist=[]

                    for i in calla:
                        if i == "":
                            del i
                        else:
                            ccatelist.append(i)

                    if cateccode == "":
                        tk.messagebox.showerror('알림', "카테고리명은 공백일 수 없습니다.")
                        manager.tkraise()

                    elif cateccode != "" and calla.count("") == len(calla):
                        tk.messagebox.showerror('알림', "카테고리목록이 전부 공백일 수 없습니다.")
                        manager.tkraise()

                    else:
                        import os.path
                        path=('0_Category.txt')
                        if os.path.isfile(path):
                            x = SH.U_strTodic('0_Category')
                            for i in list(x.keys()) :
                                if cateccode == i :
                                    del x[i]
                                else :
                                    pass

                            x[cateccode]=ccatelist

                            xx = SH.U_dicTostr(x)

                            file = open("0_Category.txt", "w", encoding="UTF-8")
                            file.write(str(xx))
                            file.close()

                            tk.messagebox.showinfo('알림', "카테고리 수정을 완료했습니다.")
                            manager.tkraise()
                        else :
                            tk.messagebox.showerror('알림', '해당 카테고리명은 존재 하지 않습니다.')
                            manager.tkraise()

                manager=tk.Tk()
                manager.title("IMP_Manager")
                manager.geometry("800x300")
                manager.resizable(False, False)

                # 센터관리
                m_f2=tk.Frame(manager, relief='groove', bd=2, bg='white')
                m_f2.place(x=130, y=10, width=650, height=280)

                m_f2_btn1=tk.Button(m_f2, text='센터\n생성', command=centerm_up)
                m_f2_btn1.place(x=15, y=45, width=100, height=60)
                m_f2_btn2=tk.Button(m_f2, text='센터\n수정', command=centerc_up)
                m_f2_btn2.place(x=15, y=145, width=100, height=60)
                # 센터관리 - 생성
                m_f2_1=tk.Frame(manager, relief='groove', bd=2)
                m_f2_1.place(x=265, y=20, width=505, height=260)

                m_f2_1la1=tk.Label(m_f2_1, text="지역명 입력 : ")
                m_f2_1la1.place(x=50, y=40)
                m_f2_1ent1=tk.Entry(m_f2_1)
                m_f2_1ent1.place(x=150, y=40)

                m_f2_1la2=tk.Label(m_f2_1, text="코드명 입력 : ")
                m_f2_1la2.place(x=50, y=80)
                m_f2_1ent2=tk.Entry(m_f2_1)
                m_f2_1ent2.place(x=150, y=80)

                m_f2_1la3=tk.Label(m_f2_1, text="주소입력 : ")
                m_f2_1la3.place(x=50, y=120)
                m_f2_1ent3=tk.Entry(m_f2_1)
                m_f2_1ent3.place(x=150, y=120)

                m_f2_1la4=tk.Label(m_f2_1, text="최대적재부피 : ")
                m_f2_1la4.place(x=50, y=160)
                m_f2_1ent4=tk.Entry(m_f2_1)
                m_f2_1ent4.place(x=150, y=160)

                m_f2_1la5=tk.Label(m_f2_1, text="섹터별부피 : ")
                m_f2_1la5.place(x=50, y=200)
                m_f2_1ent5=tk.Entry(m_f2_1)
                m_f2_1ent5.place(x=150, y=200)

                m_f2_1btn1=tk.Button(m_f2_1, width=15, height=11, text="생성", command=center_Make)
                m_f2_1btn1.place(x=350, y=38)

                # 센터관리 - 수정
                m_f2_2=tk.Frame(manager, relief='groove', bd=2)
                m_f2_2.place(x=265, y=20, width=505, height=260)

                m_f2_2la1=tk.Label(m_f2_2, text="지역명 입력 : ")
                m_f2_2la1.place(x=50, y=20)
                m_f2_2ent1=tk.Entry(m_f2_2)
                m_f2_2ent1.place(x=150, y=20)

                m_f2_2la2=tk.Label(m_f2_2, text="코드명 입력 : ")
                m_f2_2la2.place(x=50, y=50)
                m_f2_2ent2=tk.Entry(m_f2_2)
                m_f2_2ent2.place(x=150, y=50)

                m_f2_2la3=tk.Label(m_f2_2, text="주소입력 : ")
                m_f2_2la3.place(x=50, y=80)
                m_f2_2ent3=tk.Entry(m_f2_2)
                m_f2_2ent3.place(x=150, y=80)

                m_f2_2la4=tk.Label(m_f2_2, text="최대적재부피 : ")
                m_f2_2la4.place(x=50, y=110)
                m_f2_2ent4=tk.Entry(m_f2_2)
                m_f2_2ent4.place(x=150, y=110)

                m_f2_2la5=tk.Label(m_f2_2, text="섹터별부피 : ")
                m_f2_2la5.place(x=50, y=140)
                m_f2_2ent5=tk.Entry(m_f2_2)
                m_f2_2ent5.place(x=150, y=140)

                m_f2_2la6 = tk.Label(m_f2_2, text="삭제시에는 센터정보 파일 및\n입/출고 파일또한 삭제됩니다.", fg="red")
                m_f2_2la6.place(x=100, y=170)

                m_f2_2la7=tk.Label(m_f2_2, text="코드명 입력 : ")
                m_f2_2la7.place(x=50, y=220)
                m_f2_2ent7=tk.Entry(m_f2_2)
                m_f2_2ent7.place(x=150, y=220)

                m_f2_2btn1 = tk.Button(m_f2_2, width=12, height=8, text="수정", command=center_c)
                m_f2_2btn1.place(x=350, y=20)

                m_f2_2btn2 = tk.Button(m_f2_2, width=12, height=2, text="삭제", command=center_d)
                m_f2_2btn2.place(x=350, y=210)

                # 카테고리 관리
                m_f3=tk.Frame(manager, relief='groove', bd=2, bg='white')
                m_f3.place(x=130, y=10, width=650, height=280)

                m_f3_btn1=tk.Button(m_f3, text='카테고리\n생성', command=categorym_up)
                m_f3_btn1.place(x=15, y=45, width=100, height=60)
                m_f3_btn2=tk.Button(m_f3, text='카테고리\n수정', command=categoryc_up)
                m_f3_btn2.place(x=15, y=145, width=100, height=60)
                # 카테고리 - 생성
                m_f3_1=tk.Frame(manager, relief='groove', bd=2)
                m_f3_1.place(x=265, y=20, width=505, height=260)

                m_f3_1la1=tk.Label(m_f3_1, text="카테고리 명 : ")
                m_f3_1la1.place(x=50, y=30)
                m_f3_1ent1=tk.Entry(m_f3_1)
                m_f3_1ent1.place(x=160, y=30)

                m_f3_1la2=tk.Label(m_f3_1, text="카테고리 목록 1 : ")
                m_f3_1la2.place(x=50, y=60)
                m_f3_1ent2=tk.Entry(m_f3_1)
                m_f3_1ent2.place(x=160, y=60)

                m_f3_1la3=tk.Label(m_f3_1, text="카테고리 목록 2 : ")
                m_f3_1la3.place(x=50, y=90)
                m_f3_1ent3=tk.Entry(m_f3_1)
                m_f3_1ent3.place(x=160, y=90)

                m_f3_1la4=tk.Label(m_f3_1, text="카테고리 목록 3 : ")
                m_f3_1la4.place(x=50, y=120)
                m_f3_1ent4=tk.Entry(m_f3_1)
                m_f3_1ent4.place(x=160, y=120)

                m_f3_1la5=tk.Label(m_f3_1, text="카테고리 목록 4 : ")
                m_f3_1la5.place(x=50, y=150)
                m_f3_1ent5=tk.Entry(m_f3_1)
                m_f3_1ent5.place(x=160, y=150)

                m_f3_1la6=tk.Label(m_f3_1, text="카테고리 목록 5 : ")
                m_f3_1la6.place(x=50, y=180)
                m_f3_1ent6=tk.Entry(m_f3_1)
                m_f3_1ent6.place(x=160, y=180)

                m_f3_1la7=tk.Label(m_f3_1, text="카테고리 목록 6 : ")
                m_f3_1la7.place(x=50, y=210)
                m_f3_1ent7=tk.Entry(m_f3_1)
                m_f3_1ent7.place(x=160, y=210)

                Ncate_Abtn1=tk.Button(m_f3_1,width=15, height=12, text="생성", command=cate_make)
                Ncate_Abtn1.place(x=350, y=33)

                # 카테고리 - 수정
                m_f3_2=tk.Frame(manager, relief='groove', bd=2)
                m_f3_2.place(x=265, y=20, width=505, height=260)

                m_f3_2la1=tk.Label(m_f3_2, text="카테고리 명 : ")
                m_f3_2la1.place(x=50, y=30)
                m_f3_2ent1=tk.Entry(m_f3_2)
                m_f3_2ent1.place(x=160, y=30)

                m_f3_2la2=tk.Label(m_f3_2, text="카테고리 목록 1 : ")
                m_f3_2la2.place(x=50, y=60)
                m_f3_2ent2=tk.Entry(m_f3_2)
                m_f3_2ent2.place(x=160, y=60)

                m_f3_2la3=tk.Label(m_f3_2, text="카테고리 목록 2 : ")
                m_f3_2la3.place(x=50, y=90)
                m_f3_2ent3=tk.Entry(m_f3_2)
                m_f3_2ent3.place(x=160, y=90)

                m_f3_2la4=tk.Label(m_f3_2, text="카테고리 목록 3 : ")
                m_f3_2la4.place(x=50, y=120)
                m_f3_2ent4=tk.Entry(m_f3_2)
                m_f3_2ent4.place(x=160, y=120)

                m_f3_2la5=tk.Label(m_f3_2, text="카테고리 목록 4 : ")
                m_f3_2la5.place(x=50, y=150)
                m_f3_2ent5=tk.Entry(m_f3_2)
                m_f3_2ent5.place(x=160, y=150)

                m_f3_2la6=tk.Label(m_f3_2, text="카테고리 목록 5 : ")
                m_f3_2la6.place(x=50, y=180)
                m_f3_2ent6=tk.Entry(m_f3_2)
                m_f3_2ent6.place(x=160, y=180)

                m_f3_2la7=tk.Label(m_f3_2, text="카테고리 목록 6 : ")
                m_f3_2la7.place(x=50, y=210)
                m_f3_2ent7=tk.Entry(m_f3_2)
                m_f3_2ent7.place(x=160, y=210)

                m_f3_2btn1=tk.Button(m_f3_2, width=15, height=12, text="수정", command=cate_c)
                m_f3_2btn1.place(x=350, y=33)

                # IMP 관리
                m_f4=tk.Frame(manager, relief='groove', bd=2, bg='white')
                m_f4.place(x=130, y=10, width=650, height=280)

                m_f4_btn1=tk.Button(m_f4, text='프로그램\n PW 변경', command=IMPpc_up)
                m_f4_btn1.place(x=15, y=45, width=100, height=60)
                m_f4_btn2=tk.Button(m_f4, text='관리자\n PW 변경', command=IMPmc_up)
                m_f4_btn2.place(x=15, y=145, width=100, height=60)
                # IMP - 프로그램 비번 수정
                m_f4_1=tk.Frame(manager, relief='groove', bd=2, bg='black')
                m_f4_1.place(x=265, y=20, width=505, height=260)
                # IMP - 관리자 비번 수정
                m_f4_2=tk.Frame(manager, relief='groove', bd=2, bg='silver')
                m_f4_2.place(x=265, y=20, width=505, height=260)

                # 기본 화면
                m_f1=tk.Frame(manager, bd=2)
                m_f1.place(x=0, y=0, width=800, height=300)

                m_f1_btn1=tk.Button(m_f1, text='센터 관리', command=center_up)
                m_f1_btn1.place(x=15, y=40, width=100, height=40)
                m_f1_btn2=tk.Button(m_f1, text='카테고리 관리', command=category_up)
                m_f1_btn2.place(x=15, y=120, width=100, height=40)
                m_f1_btn2=tk.Button(m_f1, text='IMP 관리', command=IMP_up)
                m_f1_btn2.place(x=15, y=200, width=100, height=40)

                manager.mainloop()

            M_Passward = ML_ent1.get()

            import os.path
            path = ("M_Passward.txt")

            if os.path.isfile(path):
                file = open("M_Passward.txt.", "r", encoding="UTF-8")
                x = file.readlines()
                file.close()
                if M_Passward in x:
                    Passward_ch = tk.messagebox.showinfo('알림', "로그인 성공")
                    if Passward_ch:
                        ML.destroy()
                        Manager()
                    else:
                        pass

                else:
                    tk.messagebox.showerror('알림', "비밀번호가 맞지 않습니다.")
                    ML.tkraise()

            else:
                PW = "0001"
                file = open("M_Passward.txt.", "w", encoding="UTF-8")
                file.write(PW)
                file.close()

                Manager_Login_ch()

        def Manager_Login_A(event):
            Manager_Login_ch()

        def Manager_Login_B():
            Manager_Login_ch()

        ML=tk.Tk()
        ML.title("Manager_Login")
        ML.geometry("350x200")
        ML.resizable(False, False)

        tk.Label(ML, text="관리자 비밀번호 입력").place(x=110, y=40)
        ML_ent1 = tk.Entry(ML, show='*')
        ML_ent1.place(x=103, y=70)
        ML_ent1.bind('<Return>', Manager_Login_A)

        ML_btn1=tk.Button(ML, command=Manager_Login_B, width=10, height=3, text="입력")
        ML_btn1.place(x=140, y=110)

        ML.mainloop()

    def Product() :

        def Product_in() :

            Name=p_f1_1ent1.get() #상품명
            Cate=p_f1_1ent2.get() #카테고리(남성패션 등)
            Price=p_f1_1ent3.get() # 가격
            Volume=p_f1_1ent4.get() # 부피
            KG=p_f1_1ent5.get() # 무게
            AA=[Name,Cate,Price,Volume,KG] # 위 리스트

            if "" not in AA :
                import os.path
                path='0_IP_List.txt'
                if os.path.isfile(path) :
                    Namelist=SH.U_strTodic('0_IP_List')
                    if Name not in Namelist :
                        x=SH.catelist()
                        if Cate in x :
                            X=SH.U_strTodic('0_IP_list')
                            X_1=list(X.values())
                            X_2=[]
                            for i in X_1[1:]:
                                X_2.append(i[0])
                            X_3=X_2[-1]
                            X_4=X_3.split("-")
                            X_5=""

                            P_num_A=""
                            for i in range(len(category1)):
                                if Cate in category1[i]:
                                    P_num_A += category2[i]
                                else:
                                    pass

                            if 9999 == int(X_4[3]) :
                                A=int(X_4[1])+1
                                X_5+=P_num_A
                                X_5+="-"
                                X_5+=str(A)
                                X_5+="-"
                                X_5+=X_4[2]
                                X_5+="-"
                                X_5+='1001'

                            else :
                                A=int(X_4[3])+1
                                X_5+=P_num_A
                                X_5+="-"
                                X_5+=X_4[1]
                                X_5+="-"
                                X_5+=X_4[2]
                                X_5+="-"
                                X_5+=str(A)

                            X_6=[X_5,Cate,Price,Volume,KG]
                            X_7={}
                            X_7[Name]=X_6
                            X_8=SH.U_dicTostr(X_7)

                            file = open("0_IP_List.txt", "a", encoding="UTF-8")
                            file.write(X_8)
                            file.close()

                            tk.messagebox.showinfo('알림', '상품등록을 완료하였습니다.')
                            product.tkraise()

                        else :
                            tk.messagebox.showerror('알림', '카테고리가 존재 하지 않음.')
                            product.tkraise()
                    else:
                        tk.messagebox.showerror('알림', '같은상품이 존재함.')
                        product.tkraise()
                else :
                    title={'상품명':['제품번호','카테고리','금액','부피','무게']}
                    P_num_A=""
                    for i in range(len(category1)) :
                        if Cate in category1[i] :
                            P_num_A+=category2[i]
                        else :
                            pass

                    if P_num_A != "" :
                        P_num_B=P_num_A+'-10-IMP-1001'
                        P_num=[P_num_B,Cate,Price,Volume,KG]
                        title[Name]=P_num

                        title_A=SH.U_dicTostr(title)

                        file=open("0_IP_List.txt", "w", encoding="UTF-8")
                        file.write(title_A)
                        file.close()

                        tk.messagebox.showinfo('알림', '상품등록을 완료하였습니다.')
                        product.tkraise()
                    else :
                        tk.messagebox.showerror('알림', '카테고리가 존재하지 않아 생성이 불가능합니다.')
                        product.tkraise()
            else:
                tk.messagebox.showerror('알림','공백이 존재할 수 없습니다.')
                product.tkraise()

            pass

        def Product_ch() :

            Name=p_f1_2ent1.get()  # 상품명
            Cate=p_f1_2ent2.get()  # 카테고리(남성패션 등)
            Price=p_f1_2ent3.get()  # 가격
            Volume=p_f1_2ent4.get()  # 부피
            KG=p_f1_2ent5.get()  # 무게
            AA=[Name, Cate, Price, Volume, KG]  # 위 리스트

            if "" not in AA :
                import os.path
                path='0_IP_List.txt'

                if os.path.isfile(path) :
                    Namelist=SH.U_strTodic('0_IP_List')
                    if Name in Namelist :
                        x=SH.catelist()
                        if Cate in x :
                            P_list=SH.U_strTodic('0_IP_List')
                            P_list[Name]=[P_list[Name][0],Cate,Price,Volume,KG]

                            x=SH.U_dicTostr(P_list)

                            file = open("0_IP_List.txt", "w", encoding="UTF-8")
                            file.write(x)
                            file.close()

                            tk.messagebox.showinfo('알림', '수정을 완료하였습니다.')
                            product.tkraise()

                        else :
                            tk.messagebox.showerror('알림', '카테고리가 존재 하지 않음.')
                            product.tkraise()
                    else:
                        tk.messagebox.showerror('알림', '등록된 상품이 아닙니다.')
                        product.tkraise()
                else :
                    tk.messagebox.showerror('알림', '등록된 상품이 없습니다.')
                    product.tkraise()
            else:
                tk.messagebox.showerror('알림','공백이 존재할 수 없습니다.')
                product.tkraise()

        def pi_up() :
            p_f1_1.tkraise()

        def pc_up() :
            p_f1_2.tkraise()

        product=tk.Tk()
        product.title("IMP_Manager")
        product.geometry("600x300")
        product.resizable(False, False)

        # 상품등록
        p_f1_1=tk.Frame(product, relief='groove', bd=2)
        p_f1_1.place(x=130, y=10, width=455, height=280)

        p_f1_1la0=tk.Label(p_f1_1, text="등록 상품 정보 기입")
        p_f1_1la0.place(x=50, y=20)

        p_f1_1la1=tk.Label(p_f1_1, text="상품명 : ")
        p_f1_1la1.place(x=50, y=60)
        p_f1_1ent1=tk.Entry(p_f1_1)
        p_f1_1ent1.place(x=150, y=60)

        p_f1_1la2=tk.Label(p_f1_1, text="카테고리 : ")
        p_f1_1la2.place(x=50, y=100)
        p_f1_1ent2=tk.Entry(p_f1_1)
        p_f1_1ent2.place(x=150, y=100)

        p_f1_1la3=tk.Label(p_f1_1, text="금액 : ")
        p_f1_1la3.place(x=50, y=140)
        p_f1_1ent3=tk.Entry(p_f1_1)
        p_f1_1ent3.place(x=150, y=140)

        p_f1_1la4=tk.Label(p_f1_1, text="부피 : ")
        p_f1_1la4.place(x=50, y=180)
        p_f1_1ent4=tk.Entry(p_f1_1)
        p_f1_1ent4.place(x=150, y=180)

        p_f1_1la5=tk.Label(p_f1_1, text="무게 : ")
        p_f1_1la5.place(x=50, y=220)
        p_f1_1ent5=tk.Entry(p_f1_1)
        p_f1_1ent5.place(x=150, y=220)

        p_f1_1btn1=tk.Button(p_f1_1, width=12, height=11, text="생성", command=Product_in)
        p_f1_1btn1.place(x=330, y=60)

        # 등록 상품 정보수정
        p_f1_2=tk.Frame(product, relief='groove', bd=2)
        p_f1_2.place(x=130, y=10, width=455, height=280)

        p_f1_2la0=tk.Label(p_f1_2, text="수정할 상품명 기입")
        p_f1_2la0.place(x=50, y=20)

        p_f1_2la1=tk.Label(p_f1_2, text="상품명 : ")
        p_f1_2la1.place(x=50, y=60)
        p_f1_2ent1=tk.Entry(p_f1_2)
        p_f1_2ent1.place(x=150, y=60)

        p_f1_2la2=tk.Label(p_f1_2, text="카테고리 : ")
        p_f1_2la2.place(x=50, y=100)
        p_f1_2ent2=tk.Entry(p_f1_2)
        p_f1_2ent2.place(x=150, y=100)

        p_f1_2la3=tk.Label(p_f1_2, text="금액 : ")
        p_f1_2la3.place(x=50, y=140)
        p_f1_2ent3=tk.Entry(p_f1_2)
        p_f1_2ent3.place(x=150, y=140)

        p_f1_2la4=tk.Label(p_f1_2, text="부피 : ")
        p_f1_2la4.place(x=50, y=180)
        p_f1_2ent4=tk.Entry(p_f1_2)
        p_f1_2ent4.place(x=150, y=180)

        p_f1_2la5=tk.Label(p_f1_2, text="무게 : ")
        p_f1_2la5.place(x=50, y=220)
        p_f1_2ent5=tk.Entry(p_f1_2)
        p_f1_2ent5.place(x=150, y=220)

        p_f1_2btn1=tk.Button(p_f1_2, width=12, height=11, text="수정", command=Product_ch)
        p_f1_2btn1.place(x=330, y=60)

        # 기본 화면
        p_f1=tk.Frame(product, bd=2)
        p_f1.place(x=0, y=0, width=800, height=300)

        p_f1_btn1=tk.Button(p_f1, text='상품 등록', command=pi_up)
        p_f1_btn1.place(x=15, y=35, width=100, height=80)
        p_f1_btn2 = tk.Button(p_f1, text='등록 상품\n정보수정', command=pc_up)
        p_f1_btn2.place(x=15, y=155, width=100, height=80)

    def P_choice(event) :
        def IP() :
            P_num=choice[1]
            Name=choice[0]
            Center=IPOP_Aent3.get()
            Sector=choice[1][0:2]
            Cate=choice[2]
            SD=IPOP_Aent6.get()
            ED=IPOP_Aent7.get()
            IP_D=IPOP_Aent8.get()
            OP_D=IPOP_Aent9.get()
            Price=choice[3]
            Volume=choice[4]
            KG=choice[5]
            Cost=IPOP_Aent13.get()

            P_info=[P_num,Name,Center,Sector,Cate,SD,ED,IP_D,OP_D,Price,Volume,KG,Cost]

            if '' not in P_info :
                last_c = tk.messagebox.askyesno('알림', '입고를 진행하시겠습니까?')
                if last_c :
                    import os.path
                    path=("%sIMIP.txt" %Center)
                    if os.path.isfile(path) :

                        yysd = SD[0:2].isdigit()
                        mmsd = SD[3:5].isdigit()
                        ddsd = SD[6:8].isdigit()

                        yyed = ED[0:2].isdigit()
                        mmed = ED[3:5].isdigit()
                        dded = ED[6:8].isdigit()

                        yyip=IP_D[0:2].isdigit()
                        mmip=IP_D[3:5].isdigit()
                        ddip=IP_D[6:8].isdigit()

                        SD_C = ""
                        ED_C = ""
                        IP_D_C=""
                        OP_D_C=""

                        if SD == '-' :
                            SD_C+=SD
                        elif len(SD) == 8 :
                            if SD[2] == "-" and SD[5] == "-" :
                                if yysd and mmsd and ddsd:
                                    if int(SD[0:2]) <= 99 and int(SD[3:5]) <= 12 and int(SD[6:8]) <= 31:
                                        if int(SD[0:2]) != 0 and int(SD[3:5]) != 0 and int(SD[6:8]) != 0:
                                            SD_C+=SD
                                        else:
                                            tk.messagebox.showerror('알림', '유통기한(S) 월, 일에는 00을 기입할 수 없습니다.')
                                    else:
                                        tk.messagebox.showerror('알림', '유통기한(S)의 년, 월, 일을 정확히 기입해 주세요.')
                                else:
                                    tk.messagebox.showerror('알림', '유통기한(S)에 숫자를 기입해 주세요.')
                            else:
                                tk.messagebox.showerror('알림', '유통기한(S)을 00-00-00 형식으로 입력해주세요.')
                        else:
                            tk.messagebox.showerror('알림', '유통기한(S)을 00-00-00 형식으로 입력해주세요.')


                        if ED == '-' :
                            ED_C+=ED
                        elif len(ED) == 8 :
                            if ED[2] == "-" and ED[5] == "-" :
                                if yyed and mmed and dded:
                                    if int(ED[0:2]) <= 99 and int(ED[3:5]) <= 12 and int(ED[6:8]) <= 31:
                                        if int(ED[0:2]) != 0 and int(ED[3:5]) != 0 and int(ED[6:8]) != 0:
                                            ED_C+=ED
                                        else :
                                            tk.messagebox.showerror('알림', '유통기한(E) 월, 일에는 00을 기입할 수 없습니다.')
                                    else :
                                        tk.messagebox.showerror('알림', '유통기한(E)의 년, 월, 일을 정확히 기입해 주세요.')
                                else:
                                    tk.messagebox.showerror('알림', '유통기한(E)에 숫자를 기입해 주세요.')
                            else :
                                tk.messagebox.showerror('알림', '유통기한(E)을 00-00-00 형식으로 입력해주세요.')
                        else :
                            tk.messagebox.showerror('알림', '유통기한(E)을 00-00-00 형식으로 입력해주세요.')

                        if IP_D == '-' :
                            tk.messagebox.showerror('알림', '입고시 입고일은 반드시 기입해야 합니다.')
                        elif len(IP_D) == 8 :
                            if IP_D[2] == "-" and IP_D[5] == "-" :
                                if yyip and mmip and ddip:
                                    if int(IP_D[0:2]) <= 99 and int(IP_D[3:5]) <= 12 and int(IP_D[6:8]) <= 31:
                                        if int(IP_D[0:2]) != 0 and int(IP_D[3:5]) != 0 and int(IP_D[6:8]) != 0:
                                            IP_D_C+=IP_D
                                        else :
                                            tk.messagebox.showerror('알림', '입고일 월, 일에는 00을 기입할 수 없습니다.')
                                    else :
                                        tk.messagebox.showerror('알림', '입고일의 년, 월, 일을 정확히 기입해 주세요.')
                                else:
                                    tk.messagebox.showerror('알림', '입고일에 숫자를 기입해 주세요.')
                            else :
                                tk.messagebox.showerror('알림', '입고일은 00-00-00 형식으로 입력해주세요.')
                        else :
                            tk.messagebox.showerror('알림', '입고일은 00-00-00 형식으로 입력해주세요.')

                        if OP_D == '-' :
                            OP_D_C+=OP_D
                        else :
                            tk.messagebox.showerror('알림', '입고시에는 출고일을 기입할 수 없습니다.')

                        P_info_A=[P_num, Name, Center, Sector, Cate, SD_C, ED_C, IP_D_C, OP_D_C, Price, Volume, KG]

                        if "" not in P_info_A :
                            for i in range(int(Cost)) :
                                P_code=GY.Pro_code()

                                X={}
                                X[P_code]=P_info_A

                                XX=SH.U_dicTostr(X)

                                file=open('%sIMIP.txt' % Center, "a", encoding="UTF=8")
                                file.write(XX)
                                file.close()

                            tk.messagebox.showinfo('알림', '%s 입고를 완료 하였습니다.' % Name)
                        else :
                            pass
                    else :
                        tk.messagebox.showerror('알림', '해당센터의 입고파일은 존재하지 않습니다.')
                        Home.tkraise()
                else :
                    Home.tkraise()
            else :
                tk.messagebox.showerror('알림', '공백이 존재합니다.')
                Home.tkraise()

        def OP() :

            def Other_CD() :
                try :
                    res_1=OPCC_Listbox.curselection()
                    choice=OPCC_Listbox.get(res_1[0])

                    X_1=SH.U_strTolist('%sIMIP' %choice[0])
                    X_2=X_1[1:]
                    X_2.sort(key=lambda x:x[8])
                    X_3=[]
                    X_4={}

                    for i in X_2 :
                        if Name in i :
                            X_3.append(i)
                        else :
                            pass

                    X_3_1=X_3[:int(Cost)]

                    for i in range(len(X_3_1)) :
                        X_3_1[i][9] = OP_D
                        X_4[X_3_1[i][0]] = X_3_1[i][1:]

                    A_1=SH.U_strTodic('%sIMOP' % Center)

                    for i in X_4 :
                        A_1[i]=X_4[i][0:]

                    A_2=SH.U_dicTostr(A_1)
                    file_A=open('%sIMOP.txt' % Center, "w", encoding="UTF-8")
                    file_A.write(A_2)
                    file_A.close()

                    X_5=SH.U_strTodic('%sIMIP' %choice[0])
                    X_6=list(X_5.keys())

                    for i in X_6 :
                        if i in list(X_4.keys()) :
                            del X_5[i]
                        else :
                            pass

                    X_7=SH.U_dicTostr(X_5)
                    file_B = open('%sIMIP.txt' % choice[0], "w", encoding="UTF-8")
                    file_B.write(X_7)
                    file_B.close()
                except :
                    A=tk.messagebox.askyesno('알림', '타 센터가 데이터가 존재하지 않습니다.\n현재 창을 닫으시겠습니까?')
                    OPCC.tkraise()
                    if A :
                        OPCC.destroy()
                    else :
                        pass


            def BC() :
                Other_CD()

            def DC(event) :
                Other_CD()

            P_num = choice[1]
            Name = choice[0]
            Center = IPOP_Aent3.get()
            Sector = choice[1][0:2]
            Cate = choice[2]
            SD = IPOP_Aent6.get()
            ED = IPOP_Aent7.get()
            IP_D = IPOP_Aent8.get()
            OP_D = IPOP_Aent9.get()
            Price = choice[3]
            Volume = choice[4]
            KG = choice[5]
            Cost = IPOP_Aent13.get()

            P_info = [P_num, Name, Center, Sector, Cate, SD, ED, IP_D, OP_D, Price, Volume, KG, Cost]

            IP_Flist=[]
            Sort_list=[]
            Sort_dic={}

            if '' not in P_info:
                last_c=tk.messagebox.askyesno('알림', '출고를 진행하시겠습니까?')
                if last_c :
                    if Center in Centcode2 :

                        yyop=OP_D[0:2].isdigit()
                        mmop=OP_D[3:5].isdigit()
                        ddop=OP_D[6:8].isdigit()

                        SD_C=""
                        ED_C=""
                        IP_D_C=""
                        OP_D_C=""

                        if SD == '-':
                            SD_C+=SD
                            if ED == '-':
                                ED_C += ED
                                if IP_D == '-':
                                    IP_D_C += OP_D
                                    if OP_D == '-':
                                        tk.messagebox.showerror('알림', '출고시 출고일은 반드시 기입해야 합니다.')
                                    elif len(OP_D) == 8:
                                        if OP_D[2] == "-" and OP_D[5] == "-":
                                            if yyop and mmop and ddop:
                                                if int(OP_D[0:2]) <= 99 and int(OP_D[3:5]) <= 12 and int(
                                                        OP_D[6:8]) <= 31:
                                                    if int(OP_D[0:2]) != 0 and int(OP_D[3:5]) != 0 and int(
                                                            OP_D[6:8]) != 0:
                                                        OP_D_C += OP_D
                                                    else:
                                                        tk.messagebox.showerror('알림', '출고일 월, 일에는 00을 기입할 수 없습니다.')
                                                else:
                                                    tk.messagebox.showerror('알림', '출고일의 년, 월, 일을 정확히 기입해 주세요.')
                                            else:
                                                tk.messagebox.showerror('알림', '출고일에 숫자를 기입해 주세요.')
                                        else:
                                            tk.messagebox.showerror('알림', '출고일은 00-00-00 형식으로 입력해주세요.')
                                    else:
                                        tk.messagebox.showerror('알림', '출고일은 00-00-00 형식으로 입력해주세요.')

                                    X = SH.U_strTolist('%sIMIP' % Center)
                                    for i in X:
                                        if Name == i[2]:
                                            IP_Flist.append(i)

                                    if OP_D_C != "" and len(IP_Flist) >= int(Cost) and int(Cost) > 0:
                                        IP_Flist.sort(key=lambda x: x[8])
                                        for i in range(int(Cost)):
                                            Sort_list.append(IP_Flist[i])
                                        for i in range(len(Sort_list)):
                                            Sort_list[i][9] = OP_D
                                            Sort_dic[Sort_list[i][0]] = Sort_list[i][1:]

                                        X = SH.U_dicTostr(Sort_dic)
                                        file = open("%sIMOP.txt" % Center, 'a', encoding='UTF-8')
                                        file.write(X)
                                        file.close()

                                        Y = SH.U_strTodic('%sIMIP' % Center)

                                        X_1 = SH.U_strTodic('%sIMOP' % Center)
                                        X_2 = list(X_1.keys())[1:]

                                        for i in X_2:
                                            if i in Y:
                                                del Y[i]
                                            else:
                                                del i

                                        Y_1 = SH.U_dicTostr(Y)

                                        filex = open('%sIMIP.txt' % Center, 'w', encoding='UTF-8')
                                        filex.write(Y_1)
                                        file.close()

                                        tk.messagebox.showinfo('알림', '%s의 출고가 완료되었습니다.' % Name)
                                        Home.tkraise()

                                    elif OP_D_C != "" and len(IP_Flist) < int(Cost) and int(Cost) > 0:
                                        F = tk.messagebox.askyesno('알림','현재 센터에 **%s**의 재고수량이 부족합니다.\n타 센터의 **%s** 재고수량을 확인 하시겠습니까?' % (Name, Name))
                                        if F:
                                            Centcode3 = []
                                            IP_Alist = []
                                            IP_Alist_C = []
                                            IP_Adic = {}
                                            IP_Alist_C_F = []

                                            for i in Centcode2:
                                                if i == Center:
                                                    del i
                                                else:
                                                    Centcode3.append(i)

                                            for i in Centcode3:
                                                X = SH.U_strTolist('%sIMIP' % i)
                                                X_1 = X[1:]
                                                for x in X_1:
                                                    IP_Alist.append(x)

                                            for i in IP_Alist:
                                                if i[2] == Name:
                                                    IP_Alist_C.append(i)
                                                else:
                                                    pass

                                            for i in IP_Alist_C:
                                                if i[3] in IP_Adic.keys():
                                                    IP_Adic[i[3]] = [i[2], IP_Adic[i[3]][1] + 1]
                                                else:
                                                    IP_Adic[i[3]] = [i[2], 1]

                                            Klist = list(IP_Adic.keys())
                                            Vlist = list(IP_Adic.values())
                                            N = 0
                                            for i in Klist:
                                                B = []
                                                C = []
                                                B.append(i)
                                                for x in Vlist[N]:
                                                    C.append(x)
                                                N += 1
                                                F = B + C
                                                IP_Alist_C_F.append(F)

                                            OPCC = tk.Tk()
                                            OPCC.title("센터별 %s 재고 현황" % Name)
                                            OPCC.geometry("625x450")
                                            OPCC.resizable(False, False)

                                            OPCC_Listbox = tk.Listbox(OPCC)
                                            OPCC_Listbox.yview()
                                            OPCC_Listbox.place(x=25, y=25, width=400, height=400)

                                            Num = 0
                                            for i in IP_Alist_C_F:
                                                OPCC_Listbox.insert(Num, i)
                                                Num += 1

                                            OPCC_Listbox.bind('<Double-Button-1>', DC)

                                            OPCC_La1 = tk.Label(OPCC, text='데이터를 가져올 센터를\n선택하여 주세요.')
                                            OPCC_La1.place(x=450, y=150)

                                            OPCC_bnt1 = tk.Button(OPCC, text="선택", command=BC)
                                            OPCC_bnt1.place(x=450, y=200, width=145, height=100)

                                            OPCC.mainloop()

                                        else:
                                            pass

                                    elif int(Cost) <= 0:
                                        tk.messagebox.showerror('알림', '0개 이하로는 출고를 할 수 없습니다')
                                        Home.tkraise()

                                    else:
                                        pass
                                else:
                                    tk.messagebox.showerror('알림', '입고시에는 출고일을 기입할 수 없습니다.')
                            else:
                                tk.messagebox.showerror('알림', '출고시에는 유통기한(E)를 기입할 수 없습니다.')
                        else:
                            tk.messagebox.showerror('알림', '출고시에는 유통기한(S)를 기입할 수 없습니다.')
                    else :
                        tk.messagebox.showerror('알림', '%s 센터입고파일은 존재하지 않습니다.' % Center)
                        Home.tkraise()
                else :
                    Home.tkraise()
            else :
                tk.messagebox.showerror('알림', '공백이 존재합니다.')
                Home.tkraise()

        res_1=IPOP_listbox3.curselection()
        choice=IPOP_listbox3.get(res_1[0])

        IPOP_Ala1=tk.Label(IPOP_Page_A, text="물품번호 : ", bg='white')
        IPOP_Ala1.place(x=10, y=30)
        IPOP_ALa1_1=tk.Label(IPOP_Page_A, text='%s' % choice[1])
        IPOP_ALa1_1.place(x=100, y=30, width=120)

        IPOP_Ala2=tk.Label(IPOP_Page_A, text="제품명 : ", bg='white')
        IPOP_Ala2.place(x=10, y=80)
        IPOP_ALa2_1=tk.Label(IPOP_Page_A, text='%s' % choice[0])
        IPOP_ALa2_1.place(x=100, y=80, width=120)

        IPOP_Ala3=tk.Label(IPOP_Page_A, text="센터 : ", bg='white')
        IPOP_Ala3.place(x=10, y=130)
        IPOP_Aent3=tk.Entry(IPOP_Page_A)
        IPOP_Aent3.place(x=100, y=130, width=120)

        IPOP_Ala4=tk.Label(IPOP_Page_A, text="섹터 : ", bg='white')
        IPOP_Ala4.place(x=250, y=130)
        IPOP_ALa4_1=tk.Label(IPOP_Page_A, text='%s' % choice[1][0:2])
        IPOP_ALa4_1.place(x=340, y=130, width=120)

        IPOP_Ala5=tk.Label(IPOP_Page_A, text="카테고리 : ", bg='white')
        IPOP_Ala5.place(x=10, y=180)
        IPOP_ALa5_1=tk.Label(IPOP_Page_A, text='%s' % choice[2])
        IPOP_ALa5_1.place(x=100, y=180, width=120)

        IPOP_Ala6=tk.Label(IPOP_Page_A, text="유통기한(S) : ", bg='white')
        IPOP_Ala6.place(x=10, y=230)
        IPOP_Aent6=tk.Entry(IPOP_Page_A)
        IPOP_Aent6.insert(0, '-')
        IPOP_Aent6.place(x=100, y=230, width=120)

        IPOP_Ala7=tk.Label(IPOP_Page_A, text="유통기한(E) : ", bg='white')
        IPOP_Ala7.place(x=250, y=230)
        IPOP_Aent7=tk.Entry(IPOP_Page_A)
        IPOP_Aent7.insert(0, '-')
        IPOP_Aent7.place(x=340, y=230, width=120)

        IPOP_Ala8=tk.Label(IPOP_Page_A, text="입고일 : ", bg='white')
        IPOP_Ala8.place(x=10, y=280)
        IPOP_Aent8=tk.Entry(IPOP_Page_A)
        IPOP_Aent8.insert(0, '-')
        IPOP_Aent8.place(x=100, y=280, width=120)

        IPOP_Ala9=tk.Label(IPOP_Page_A, text="출고일 : ", bg='white')
        IPOP_Ala9.place(x=250, y=280)
        IPOP_Aent9=tk.Entry(IPOP_Page_A)
        IPOP_Aent9.insert(0, '-')
        IPOP_Aent9.place(x=340, y=280, width=120)

        IPOP_Ala10=tk.Label(IPOP_Page_A, text="금액 : ", bg='white')
        IPOP_Ala10.place(x=10, y=330)
        IPOP_ALa10_1=tk.Label(IPOP_Page_A, text='%s' % choice[3])
        IPOP_ALa10_1.place(x=100, y=330, width=120)

        IPOP_Ala11=tk.Label(IPOP_Page_A, text="부피 : ", bg='white')
        IPOP_Ala11.place(x=250, y=330)
        IPOP_ALa11_1=tk.Label(IPOP_Page_A, text='%s' % choice[4])
        IPOP_ALa11_1.place(x=340, y=330, width=120)

        IPOP_Ala12=tk.Label(IPOP_Page_A, text="무게 : ", bg='white')
        IPOP_Ala12.place(x=10, y=380)
        IPOP_ALa12_1=tk.Label(IPOP_Page_A, text='%s' % choice[5])
        IPOP_ALa12_1.place(x=100, y=380, width=120)

        IPOP_Ala13 = tk.Label(IPOP_Page_A, text="수량 : ", bg='white')
        IPOP_Ala13.place(x=250, y=380)
        IPOP_Aent13 = tk.Entry(IPOP_Page_A)
        IPOP_Aent13.place(x=340, y=380, width=120)

        IPOP_Abtn1=tk.Button(IPOP_Page_A, text="입고", command=IP)
        IPOP_Abtn1.place(x=140, y=440, width=90, height=50)

        IPOP_Abtn2=tk.Button(IPOP_Page_A, text="출고", command=OP)
        IPOP_Abtn2.place(x=280, y=440, width=90, height=50)

    def IP_choice(event):
        def IP_choice_c() :
            pass
        def IP_choice_d() :
            pass

        res_1=IMIP_listbox1.curselection()
        choice=IMIP_listbox1.get(res_1[0])

        IMIP_Ala14=tk.Label(IMIP_Page_A, text="고유코드 : ", bg='white')
        IMIP_Ala14.place(x=10, y=30)
        IMIP_Ala14_1=tk.Label(IMIP_Page_A, text='%s' % choice[0])
        IMIP_Ala14_1.place(x=100, y=30, width=120)

        IMIP_Ala1=tk.Label(IMIP_Page_A, text="물품번호 : ", bg='white')
        IMIP_Ala1.place(x=250, y=30)
        IMIP_ALa1_1=tk.Label(IMIP_Page_A, text='%s' % choice[1])
        IMIP_ALa1_1.place(x=340, y=30, width=120)

        IMIP_Ala2=tk.Label(IMIP_Page_A, text="제품명 : ", bg='white')
        IMIP_Ala2.place(x=10, y=80)
        IMIP_ALa2_1=tk.Label(IMIP_Page_A, text='%s' % choice[2])
        IMIP_ALa2_1.place(x=100, y=80, width=120)

        IMIP_Ala3=tk.Label(IMIP_Page_A, text="센터 : ", bg='white')
        IMIP_Ala3.place(x=10, y=130)
        IMIP_Ala3_1=tk.Label(IMIP_Page_A, text='%s' % choice[3])
        IMIP_Ala3_1.place(x=100, y=130, width=120)
        # IMIP_Aent3=tk.Entry(IMIP_Page_A)
        # IMIP_Aent3.place(x=100, y=130, width=120)

        IMIP_Ala4=tk.Label(IMIP_Page_A, text="섹터 : ", bg='white')
        IMIP_Ala4.place(x=250, y=130)
        IMIP_ALa4_1=tk.Label(IMIP_Page_A, text='%s' % choice[4])
        IMIP_ALa4_1.place(x=340, y=130, width=120)

        IMIP_Ala5=tk.Label(IMIP_Page_A, text="카테고리 : ", bg='white')
        IMIP_Ala5.place(x=10, y=180)
        IMIP_ALa5_1=tk.Label(IMIP_Page_A, text='%s' % choice[5])
        IMIP_ALa5_1.place(x=100, y=180, width=120)

        IMIP_Ala6=tk.Label(IMIP_Page_A, text="유통기한(S) : ", bg='white')
        IMIP_Ala6.place(x=10, y=230)
        IMIP_Ala6_1=tk.Label(IMIP_Page_A, text='%s' % choice[6])
        IMIP_Ala6_1.place(x=100, y=230, width=120)
        # IMIP_Aent6=tk.Entry(IMIP_Page_A)
        # IMIP_Aent6.insert(0, '-')
        # IMIP_Aent6.place(x=100, y=230, width=120)

        IMIP_Ala7=tk.Label(IMIP_Page_A, text="유통기한(E) : ", bg='white')
        IMIP_Ala7.place(x=250, y=230)
        IMIP_Ala7_1=tk.Label(IMIP_Page_A, text='%s' % choice[7])
        IMIP_Ala7_1.place(x=340, y=230, width=120)
        # IMIP_Aent7=tk.Entry(IMIP_Page_A)
        # IMIP_Aent7.insert(0, '-')
        # IMIP_Aent7.place(x=340, y=230, width=120)

        IMIP_Ala8=tk.Label(IMIP_Page_A, text="입고일 : ", bg='white')
        IMIP_Ala8.place(x=10, y=280)
        IMIP_Ala8_1=tk.Label(IMIP_Page_A, text='%s' % choice[8])
        IMIP_Ala8_1.place(x=100, y=280, width=120)
        # IMIP_Aent8=tk.Entry(IMIP_Page_A)
        # IMIP_Aent8.insert(0, '-')
        # IMIP_Aent8.place(x=100, y=280, width=120)

        IMIP_Ala9=tk.Label(IMIP_Page_A, text="출고일 : ", bg='white')
        IMIP_Ala9.place(x=250, y=280)
        IMIP_Ala9_1=tk.Label(IMIP_Page_A, text='%s' % choice[9])
        IMIP_Ala9_1.place(x=340, y=280, width=120)
        # IMIP_Aent9=tk.Entry(IMIP_Page_A)
        # IMIP_Aent9.insert(0, '-')
        # IMIP_Aent9.place(x=340, y=280, width=120)

        IMIP_Ala10=tk.Label(IMIP_Page_A, text="금액 : ", bg='white')
        IMIP_Ala10.place(x=10, y=330)
        IMIP_ALa10_1=tk.Label(IMIP_Page_A, text='%s' % choice[10])
        IMIP_ALa10_1.place(x=100, y=330, width=120)

        IMIP_Ala11=tk.Label(IMIP_Page_A, text="부피 : ", bg='white')
        IMIP_Ala11.place(x=250, y=330)
        IMIP_ALa11_1=tk.Label(IMIP_Page_A, text='%s' % choice[11])
        IMIP_ALa11_1.place(x=340, y=330, width=120)

        IMIP_Ala12=tk.Label(IMIP_Page_A, text="무게 : ", bg='white')
        IMIP_Ala12.place(x=10, y=380)
        IMIP_ALa12_1=tk.Label(IMIP_Page_A, text='%s' % choice[12])
        IMIP_ALa12_1.place(x=100, y=380, width=120)

        # IMIP_Ala13=tk.Label(IMIP_Page_A, text="수량 : ", bg='white')
        # IMIP_Ala13.place(x=250, y=380)
        # IMIP_Aent13=tk.Entry(IMIP_Page_A)
        # IMIP_Aent13.place(x=340, y=380, width=120)

        # IMIP_Abtn1=tk.Button(IPOP_Page_A, text="수정", command=IP_choice_c)
        # IMIP_Abtn1.place(x=140, y=440, width=90, height=50)
        #
        # IMIP_Abtn2=tk.Button(IPOP_Page_A, text="삭제", command=IP_choice_d)
        # IMIP_Abtn2.place(x=280, y=440, width=90, height=50)

    def OP_choice(event):
        def OP_choice_c() :
            pass
        def OP_choice_d() :
            pass

        res_1=IMOP_listbox1.curselection()
        choice=IMOP_listbox1.get(res_1[0])

        IMOP_Ala14=tk.Label(IMOP_Page_A, text="고유코드 : ", bg='white')
        IMOP_Ala14.place(x=10, y=30)
        IMOP_Ala14_1=tk.Label(IMOP_Page_A, text='%s' % choice[0])
        IMOP_Ala14_1.place(x=100, y=30, width=120)

        IMOP_Ala1=tk.Label(IMOP_Page_A, text="물품번호 : ", bg='white')
        IMOP_Ala1.place(x=250, y=30)
        IMOP_ALa1_1=tk.Label(IMOP_Page_A, text='%s' % choice[1])
        IMOP_ALa1_1.place(x=340, y=30, width=120)

        IMOP_Ala2=tk.Label(IMOP_Page_A, text="제품명 : ", bg='white')
        IMOP_Ala2.place(x=10, y=80)
        IMOP_ALa2_1=tk.Label(IMOP_Page_A, text='%s' % choice[2])
        IMOP_ALa2_1.place(x=100, y=80, width=120)

        IMOP_Ala3=tk.Label(IMOP_Page_A, text="센터 : ", bg='white')
        IMOP_Ala3.place(x=10, y=130)
        IMOP_Ala3_1=tk.Label(IMOP_Page_A, text='%s' % choice[3])
        IMOP_Ala3_1.place(x=100, y=130, width=120)
        # IMOP_Aent3=tk.Entry(IMOP_Page_A)
        # IMOP_Aent3.place(x=100, y=130, width=120)

        IMOP_Ala4=tk.Label(IMOP_Page_A, text="섹터 : ", bg='white')
        IMOP_Ala4.place(x=250, y=130)
        IMOP_ALa4_1=tk.Label(IMOP_Page_A, text='%s' % choice[4])
        IMOP_ALa4_1.place(x=340, y=130, width=120)

        IMOP_Ala5=tk.Label(IMOP_Page_A, text="카테고리 : ", bg='white')
        IMOP_Ala5.place(x=10, y=180)
        IMOP_ALa5_1=tk.Label(IMOP_Page_A, text='%s' % choice[5])
        IMOP_ALa5_1.place(x=100, y=180, width=120)

        IMOP_Ala6=tk.Label(IMOP_Page_A, text="유통기한(S) : ", bg='white')
        IMOP_Ala6.place(x=10, y=230)
        IMOP_Ala6_1=tk.Label(IMOP_Page_A, text='%s' % choice[6])
        IMOP_Ala6_1.place(x=100, y=230, width=120)
        # IMOP_Aent6=tk.Entry(IMOP_Page_A)
        # IMOP_Aent6.insert(0, '-')
        # IMOP_Aent6.place(x=100, y=230, width=120)

        IMOP_Ala7=tk.Label(IMOP_Page_A, text="유통기한(E) : ", bg='white')
        IMOP_Ala7.place(x=250, y=230)
        IMOP_Ala7_1=tk.Label(IMOP_Page_A, text='%s' % choice[7])
        IMOP_Ala7_1.place(x=340, y=230, width=120)
        # IMOP_Aent7=tk.Entry(IMOP_Page_A)
        # IMOP_Aent7.insert(0, '-')
        # IMOP_Aent7.place(x=340, y=230, width=120)

        IMOP_Ala8=tk.Label(IMOP_Page_A, text="입고일 : ", bg='white')
        IMOP_Ala8.place(x=10, y=280)
        IMOP_Ala8_1=tk.Label(IMOP_Page_A, text='%s' % choice[8])
        IMOP_Ala8_1.place(x=100, y=280, width=120)
        # IMOP_Aent8=tk.Entry(IMOP_Page_A)
        # IMOP_Aent8.insert(0, '-')
        # IMOP_Aent8.place(x=100, y=280, width=120)

        IMOP_Ala9=tk.Label(IMOP_Page_A, text="출고일 : ", bg='white')
        IMOP_Ala9.place(x=250, y=280)
        IMOP_Ala9_1=tk.Label(IMOP_Page_A, text='%s' % choice[9])
        IMOP_Ala9_1.place(x=340, y=280, width=120)
        # IMOP_Aent9=tk.Entry(IMOP_Page_A)
        # IMOP_Aent9.insert(0, '-')
        # IMOP_Aent9.place(x=340, y=280, width=120)

        IMOP_Ala10=tk.Label(IMOP_Page_A, text="금액 : ", bg='white')
        IMOP_Ala10.place(x=10, y=330)
        IMOP_ALa10_1=tk.Label(IMOP_Page_A, text='%s' % choice[10])
        IMOP_ALa10_1.place(x=100, y=330, width=120)

        IMOP_Ala11=tk.Label(IMOP_Page_A, text="부피 : ", bg='white')
        IMOP_Ala11.place(x=250, y=330)
        IMOP_ALa11_1=tk.Label(IMOP_Page_A, text='%s' % choice[11])
        IMOP_ALa11_1.place(x=340, y=330, width=120)

        IMOP_Ala12=tk.Label(IMOP_Page_A, text="무게 : ", bg='white')
        IMOP_Ala12.place(x=10, y=380)
        IMOP_ALa12_1=tk.Label(IMOP_Page_A, text='%s' % choice[12])
        IMOP_ALa12_1.place(x=100, y=380, width=120)

        # IMOP_Ala13=tk.Label(IMOP_Page_A, text="수량 : ", bg='white')
        # IMOP_Ala13.place(x=250, y=380)
        # IMOP_Aent13=tk.Entry(IMOP_Page_A)
        # IMOP_Aent13.place(x=340, y=380, width=120)

        # IMOP_Abtn1=tk.Button(IMOP_Page_A, text="수정", command=IP_choice_c)
        # IMOP_Abtn1.place(x=140, y=440, width=90, height=50)
        #
        # IMOP_Abtn2=tk.Button(IMOP_Page_A, text="삭제", command=IP_choice_d)
        # IMOP_Abtn2.place(x=280, y=440, width=90, height=50)

    def ShowIPlist() :

        C_center_1=IMIP_cb1.get()
        C_center_2=C_center_1[0:2]

        C_cate=IMIP_cb2.get()

        AA=[C_center_2,C_cate]

        x=Centcode2 # 센터코드명 문자열 리스트
        y=category2 # 카테고리명 문자열 리스트

        if "" not in AA :
            if C_center_2 == '전체' and C_cate == '전체':
                IMIP_listbox1.delete(0,999999999)
                AA_1=[]
                Num=0

                for i in Centcode2 :
                    X_1=SH.U_strTolist('%sIMIP' % i)
                    X_2=X_1[1:]
                    for x in X_2 :
                        AA_1.append(x)

                for i in AA_1 :
                    IMIP_listbox1.insert(Num, i)
                    Num+=1

            elif C_center_2 == '전체' and C_cate != '전체' :
                IMIP_listbox1.delete(0,999999999)
                AA_1=[]
                AA_2=[]
                Num=0

                for i in Centcode2 :
                    X_1=SH.U_strTolist('%sIMIP' % i)
                    X_2=X_1[1:]
                    for x in X_2 :
                        AA_1.append(x)

                for i in AA_1 :
                    if C_cate in i :
                        AA_2.append(i)
                    else :
                        pass

                for i in AA_2 :
                    IMIP_listbox1.insert(Num, i)
                    Num+=1

            elif C_center_2 != '전체' and C_cate == '전체' :
                IMIP_listbox1.delete(0,999999999)
                AA_1=[]
                Num=0

                X_1=SH.U_strTolist('%sIMIP' %C_center_2)
                X_2=X_1[1:]
                for i in X_2 :
                    AA_1.append(i)

                for i in AA_1 :
                    IMIP_listbox1.insert(Num, i)
                    Num+=1

            elif C_center_2 != '전체' and C_cate != '전체' :
                IMIP_listbox1.delete(0,999999999)
                AA_1=[]
                AA_2=[]
                Num = 0

                X_1 = SH.U_strTolist('%sIMIP' % C_center_2)
                X_2 = X_1[1:]
                for i in X_2:
                    AA_1.append(i)

                for i in AA_1 :
                    if C_cate in i :
                        AA_2.append(i)
                    else :
                        pass

                for i in AA_2:
                    IMIP_listbox1.insert(Num, i)
                    Num+=1

            else:
                pass
        else :
            tk.messagebox.showerror('알림', '센터와 카테고리를 모두 선택하여 주세요.')
            Home.tkraise()

    def ShowIPlist_c():

        CB_C=IMIP_cb3.get()
        FC=IMIP_ent1.get()
        Be_C=IMIP_listbox1.get(0,999999999)

        Af_C=[]
        Num=0

        if CB_C != "" and FC != "" :
            IMIP_listbox1.delete(0, 999999999)
            for i in Be_C:
                if FC in i :
                    Af_C.append(i)

        else :
            tk.messagebox.showerror('알림', '검색 조건을 확인 해주세요.')
            Home.tkraise()

        for i in Af_C:
            IMIP_listbox1.insert(Num, i)
            Num += 1

    def ShowOPlist() :

        C_center_1=IMOP_cb1.get()
        C_center_2=C_center_1[0:2]

        C_cate=IMOP_cb2.get()

        AA=[C_center_2,C_cate]

        x=Centcode2 # 센터코드명 문자열 리스트
        y=category2 # 카테고리명 문자열 리스트

        if "" not in AA :
            if C_center_2 == '전체' and C_cate == '전체':
                IMOP_listbox1.delete(0,999999999)
                AA_1=[]
                Num=0

                for i in Centcode2 :
                    X_1=SH.U_strTolist('%sIMOP' % i)
                    X_2=X_1[1:]
                    for x in X_2 :
                        AA_1.append(x)

                for i in AA_1 :
                    IMOP_listbox1.insert(Num, i)
                    Num+=1

            elif C_center_2 == '전체' and C_cate != '전체' :
                IMOP_listbox1.delete(0,999999999)
                AA_1=[]
                AA_2=[]
                Num=0

                for i in Centcode2 :
                    X_1=SH.U_strTolist('%sIMOP' % i)
                    X_2=X_1[1:]
                    for x in X_2 :
                        AA_1.append(x)

                for i in AA_1 :
                    if C_cate in i :
                        AA_2.append(i)
                    else :
                        pass

                for i in AA_2 :
                    IMOP_listbox1.insert(Num, i)
                    Num+=1

            elif C_center_2 != '전체' and C_cate == '전체' :
                IMOP_listbox1.delete(0,999999999)
                AA_1=[]
                Num=0

                X_1=SH.U_strTolist('%sIMOP' %C_center_2)
                X_2=X_1[1:]
                for i in X_2 :
                    AA_1.append(i)

                for i in AA_1 :
                    IMOP_listbox1.insert(Num, i)
                    Num+=1

            elif C_center_2 != '전체' and C_cate != '전체' :
                IMOP_listbox1.delete(0,999999999)
                AA_1=[]
                AA_2=[]
                Num = 0

                X_1 = SH.U_strTolist('%sIMOP' % C_center_2)
                X_2 = X_1[1:]
                for i in X_2:
                    AA_1.append(i)

                for i in AA_1 :
                    if C_cate in i :
                        AA_2.append(i)
                    else :
                        pass

                for i in AA_2:
                    IMOP_listbox1.insert(Num, i)
                    Num+=1

            else:
                pass
        else :
            tk.messagebox.showerror('알림', '센터와 카테고리를 모두 선택하여 주세요.')
            Home.tkraise()

    def ShowOPlist_c():

        CB_C=IMOP_cb3.get()
        FC=IMOP_ent1.get()
        Be_C=IMOP_listbox1.get(0,999999999)

        Af_C=[]
        Num=0

        if CB_C != "" and FC != "" :
            IMOP_listbox1.delete(0, 999999999)
            for i in Be_C:
                if FC in i :
                    Af_C.append(i)

        else :
            tk.messagebox.showerror('알림', '검색 조건을 확인 해주세요.')
            Home.tkraise()

        for i in Af_C:
            IMOP_listbox1.insert(Num, str(i))
            Num += 1

    def Cate_info(event) :
        import os.path
        path='0_Category.txt'

        if os.path.isfile(path):

            C_info=tk.Tk()
            C_info.title("카테고리 등록 현황")
            C_info.geometry("400x400")
            C_info.resizable(False, False)

            x = SH.U_strTodic('0_Category')
            catecode = list(x.keys())[1:]
            catelist = list(x.values())[1:]

            catecodestr = ""
            cateliststr = ""

            for i in catecode:
                catecodestr += i
                catecodestr += " "
                catecodestr += "="
                catecodestr += "\n"
                catecodestr += "\n"

            for i in catelist:
                for x in i:
                    cateliststr += x
                    cateliststr += " "
                cateliststr += "\n"
                cateliststr += "\n"

            CCSla5 = tk.Label(C_info, text="%s" % catecodestr)
            CCSla5.place(x=30, y=40)

            CCSla6 = tk.Label(C_info, text="%s" % cateliststr)
            CCSla6.place(x=65, y=40)

            # CCSbtn1 = tk.Button(C_info, command=CCS.destroy, width=15, height=5, text="확인")
            # CCSbtn1.place(x=0, y=300)
        else :
            tk.messagebox.showerror('알림','설정되어있는 카테고리가 없습니다.\n신규 카테고리를 생성해주세요.')

    def IP_Center_info(event) :

        word=IMIP_cb1.get()
        word_A=[]
        word_B=""

        if word != "" :
            if word != "전체" :
                for i in word:
                    if i == " ":
                        del i
                    else :
                        if i.encode().isalpha():
                            word_B+=i
                        else:
                            del i
            else :
                tk.messagebox.showerror('알림', '콤보박스의 센터를 선택하여 주세요.')
        else :
            tk.messagebox.showerror('알림','콤보박스의 센터를 선택하여 주세요.')
        word_A.append(word_B)
        print(word_A)

    def OP_Center_info(event) :

        A=IMOP_cb1.get()






    def IMIP_page() :
        IMIP_Page.tkraise()
        IMIP_Page_A.tkraise()

    def IMOP_page() :
        IMOP_Page.tkraise()
        IMOP_Page_A.tkraise()


    def IPOP_page() :
        IPOP_Page.tkraise()
        IPOP_Page_A.tkraise()
        IPOP_Page_B.tkraise()
        IPOP_Page_C.tkraise()

    Centcode1 = []
    Centcode2 = []
    category1 = []
    category2 = []

    import os.path
    path1 = '0_CCN.txt'
    path2 = '0_Category.txt'

    if os.path.isfile(path1):
        dict = SH.U_strTodic('0_CCN')

        Co_code = list(dict.keys())[1:]
        Co_list = list(dict.values())[1:]

        aa1 = []
        bb1 = []

        for i in Co_code:
            if i in aa1:
                pass
            else:
                aa1.append(i)
            for x in Co_list:
                if x in bb1:
                    pass
                else:
                    bb1.append(x)

        for i in aa1:
            Centcode2.append(i)

        for i in range(len(aa1)):
            globals()['{}'.format(aa1[i])] = bb1[i]
            Centcode1.append(eval(aa1[i]))

    else:
        pass

    if os.path.isfile(path2):
        dict = SH.U_strTodic('0_Category')

        Ca_code = list(dict.keys())[1:]
        Ca_list = list(dict.values())[1:]

        aa2 = []
        bb2 = []

        for i in Ca_code:
            if i in aa2:
                pass
            else:
                aa2.append(i)
            for x in Ca_list:
                if x in bb2:
                    pass
                else:
                    bb2.append(x)

        for i in aa2:
            category2.append(i)

        for i in range(len(aa2)):
            globals()['{}'.format(aa2[i])] = bb2[i]
            category1.append(eval(aa2[i]))

    else:
        pass

    Home = tk.Tk()
    Home.title("Inventory Management Program (IMP)_v 0.1")
    Home.geometry("1600x900")
    Home.resizable(False, False)

    Home_Menu=tk.Menu(Home)

    menu_1=tk.Menu(Home_Menu, tearoff=0)
    menu_1.add_command(label="관리자 모드", command=Manager_Login)
    menu_1.add_separator()
    menu_1.add_command(label="제품관리", command=Product)

    Home_Menu.add_cascade(label="Menu", menu=menu_1)

    Home.config(menu=Home_Menu)

    # 입/출고 처리
    IPOP_Page=tk.Frame(Home, bd=2)
    IPOP_Page.place(x=0, y=0, width=1600, height=900)

    IPOP_Page_A=tk.Frame(Home, relief='groove', bd=2, bg='white')
    IPOP_Page_A.place(x=1025, y=323, width=500, height=500)

    IPOP_Page_B=tk.Frame(Home, relief='groove', bd=2)
    IPOP_Page_B.place(x=48, y=323, width=120, height=200)

    IPOP_Page_C=tk.Frame(Home, relief='groove', bd=2)
    IPOP_Page_C.place(x=48, y=546, width=120, height=200)

    IPOP_listbox1=tk.Listbox(IPOP_Page)
    IPOP_listbox1.yview()
    IPOP_listbox1.place(x=45, y=320, width=120, height=200)
    IPOP_listbox2=tk.Listbox(IPOP_Page)
    IPOP_listbox2.yview()
    IPOP_listbox2.place(x=45, y=545, width=120, height=200)
    IPOP_btn1=tk.Button(IPOP_Page, text="-")
    IPOP_btn1.place(x=45, y=770, width=120, height=50)

    IPOP_listbox3=tk.Listbox(IPOP_Page)
    IPOP_listbox3.yview()
    IPOP_listbox3.place(x=180, y=320, width=800, height=500)

    import os.path
    path=('0_IP_List.txt')
    if os.path.isfile(path) :
        IP_list=SH.U_strTolist('0_IP_List')
        No=0
        for i in IP_list[1:] :
            IPOP_listbox3.insert(No, i)
            No+=1
        IPOP_listbox3.bind('<Double-Button-1>', P_choice)
    else :
        pass


    IPOP_combolist=['상품명']

    IPOP_cb1=tk.ttk.Combobox(IPOP_Page, height=10, values=IPOP_combolist)
    IPOP_cb1.place(x=360, y=840, width=100, height=25)
    IPOP_ent1=tk.Entry(IPOP_Page)
    IPOP_ent1.place(x=475, y=840, width=160, height=25)
    IPOP_btn2=tk.Button(IPOP_Page, text="검색")
    IPOP_btn2.place(x=650, y=840, width=100, height=25)

    IPOP_btn3=tk.Button(IPOP_Page, text="입고리스트", command=IMIP_page)
    IPOP_btn3.place(x=45, y=210, width=200, height=40)
    IPOP_btn4=tk.Button(IPOP_Page, text="출고리스트", command=IMOP_page)
    IPOP_btn4.place(x=45, y=260, width=200, height=40)
    IPOP_btn5=tk.Button(IPOP_Page, text="입/출고\n처리", command=IPOP_page)
    IPOP_btn5.place(x=830, y=210, width=150, height=90)

    IPOP_la1=tk.Label(IPOP_Page, text="현재화면 : 입/출고 처리")
    IPOP_la1.pack(side="bottom")

    # 출고리스트 페이지
    IMOP_Page=tk.Frame(Home, bd=2)
    IMOP_Page.place(x=0, y=0, width=1600, height=900)

    IMOP_Page_A=tk.Frame(Home, relief='groove', bd=2, bg='white')
    IMOP_Page_A.place(x=1025, y=323, width=500, height=500)

    IMOP_cblist_1=[]
    IMOP_cblist_1.append('전체')

    import os.path
    path = ('0_CCN.txt')
    if os.path.isfile(path):
        x = SH.U_strTolist('0_CCN')
        xx = x[1:]
        for i in xx:
            IMOP_cblist_1.append(i)
    else:
        pass

    IMOP_cb1=tk.ttk.Combobox(IMOP_Page, height=10, values=IMOP_cblist_1)
    IMOP_cb1.place(x=45, y=320, width=120, height=25)
    IMOP_cb1.bind('<Double-Button-1>', OP_Center_info)

    IMOP_cblist_2=[]
    IMOP_cblist_2.append('전체')

    import os.path
    path = ('0_Category.txt')
    if os.path.isfile(path):
        x = SH.U_strTolist('0_Category')
        xx = x[1:]
        for i in xx:
            IMOP_cblist_2.append(i[0])
    else:
        pass

    IMOP_cb2=tk.ttk.Combobox(IMOP_Page, height=10, values=IMOP_cblist_2)
    IMOP_cb2.place(x=45, y=545, width=120, height=25)
    IMOP_cb2.bind('<Double-Button-1>', Cate_info)

    IMOP_btn1=tk.Button(IMOP_Page, text="선택", command=ShowOPlist)
    IMOP_btn1.place(x=45, y=770, width=120, height=50)

    IMOP_listbox1=tk.Listbox(IMOP_Page)
    IMOP_listbox1.yview()
    IMOP_listbox1.place(x=180, y=320, width=800, height=500)
    IMOP_listbox1.bind('<Double-Button-1>', OP_choice)

    IMOP_cblist_3=['고유코드', '상품명', '출고일', '유통기한(S)', '유통기한(E)']

    IMOP_cb3=tk.ttk.Combobox(IMOP_Page, height=10, values=IMOP_cblist_3)
    IMOP_cb3.place(x=360, y=840, width=100, height=25)
    IMOP_ent1=tk.Entry(IMOP_Page)
    IMOP_ent1.place(x=475, y=840, width=160, height=25)
    IMOP_btn2=tk.Button(IMOP_Page, text="검색", command=ShowOPlist_c)
    IMOP_btn2.place(x=650, y=840, width=100, height=25)

    IMOP_btn3=tk.Button(IMOP_Page, text="입고리스트", command=IMIP_page)
    IMOP_btn3.place(x=45, y=210, width=200, height=40)
    IMOP_btn4=tk.Button(IMOP_Page, text="출고리스트", command=IMOP_page)
    IMOP_btn4.place(x=45, y=260, width=200, height=40)
    IMOP_btn5=tk.Button(IMOP_Page, text="입/출고\n처리", command=IPOP_page)
    IMOP_btn5.place(x=830, y=210, width=150, height=90)

    IMOP_btn6=tk.Button(IMOP_Page, text="수정")
    IMOP_btn6.place(x=1230, y=830, width=90, height=50)

    IMOP_la1=tk.Label(IMOP_Page, text="현재화면 : 출고리스트")
    IMOP_la1.pack(side="bottom")

    # 입고리스트 페이지
    IMIP_Page=tk.Frame(Home, bd=2)
    IMIP_Page.place(x=0, y=0, width=1600, height=900)

    IMIP_Page_A=tk.Frame(Home, relief='groove', bd=2, bg='white')
    IMIP_Page_A.place(x=1025, y=323, width=500, height=500)

    IMIP_cblist_1=[]
    IMIP_cblist_1.append('전체')

    import os.path
    path=('0_CCN.txt')
    if os.path.isfile(path) :
        x=SH.U_strTolist('0_CCN')
        xx=x[1:]
        for i in xx :
            IMIP_cblist_1.append(i)
    else:
        pass

    IMIP_cb1=tk.ttk.Combobox(IMIP_Page, height=10, values=IMIP_cblist_1)
    IMIP_cb1.place(x=45, y=320, width=120, height=25)
    IMIP_cb1.bind('<Double-Button-1>', IP_Center_info)

    IMIP_cblist_2=[]
    IMIP_cblist_2.append('전체')

    import os.path
    path = ('0_Category.txt')
    if os.path.isfile(path):
        x = SH.U_strTolist('0_Category')
        xx = x[1:]
        for i in xx:
            IMIP_cblist_2.append(i[0])
    else:
        pass

    IMIP_cb2=tk.ttk.Combobox(IMIP_Page, height=10, values=IMIP_cblist_2)
    IMIP_cb2.place(x=45, y=545, width=120, height=25)
    IMIP_cb2.bind('<Double-Button-1>', Cate_info)

    IMIP_btn1=tk.Button(IMIP_Page, text="선택", command=ShowIPlist)
    IMIP_btn1.place(x=45, y=770, width=120, height=50)

    IMIP_listbox1=tk.Listbox(IMIP_Page)
    IMIP_listbox1.yview()
    IMIP_listbox1.place(x=180, y=320, width=800, height=500)
    IMIP_listbox1.bind('<Double-Button-1>', IP_choice)

    IMIP_cblist_3=['고유코드', '상품명', '입고일', '유통기한(S)', '유통기한(E)']

    IMIP_cb3=tk.ttk.Combobox(IMIP_Page, height=10, values=IMIP_cblist_3)
    IMIP_cb3.place(x=360, y=840, width=100, height=25)
    IMIP_ent1=tk.Entry(IMIP_Page)
    IMIP_ent1.place(x=475, y=840, width=160, height=25)
    IMIP_btn2=tk.Button(IMIP_Page, text="검색", command=ShowIPlist_c)
    IMIP_btn2.place(x=650, y=840, width=100, height=25)

    IMIP_btn3=tk.Button(IMIP_Page, text="입고리스트", command=IMIP_page)
    IMIP_btn3.place(x=45, y=210, width=200, height=40)
    IMIP_btn4=tk.Button(IMIP_Page, text="출고리스트", command=IMOP_page)
    IMIP_btn4.place(x=45, y=260, width=200, height=40)
    IMIP_btn5=tk.Button(IMIP_Page, text="입/출고\n처리", command=IPOP_page)
    IMIP_btn5.place(x=830, y=210, width=150, height=90)

    IMIP_la1=tk.Label(IMIP_Page, text="현재화면 : 입고리스트")
    IMIP_la1.pack(side="bottom")

    # 초기화면
    Basic_mode=tk.Frame(Home, bd=2)
    Basic_mode.place(x=0, y=0, width=1600, height=900)

    Basic_mode_A=tk.Frame(Home, relief='groove', bd=2)
    Basic_mode_A.place(x=1025, y=323, width=500, height=500)

    Basic_cblist_1=[]

    Basic_cb1 = tk.ttk.Combobox(Basic_mode, height=10, values=Basic_cblist_1)
    Basic_cb1.place(x=45, y=320, width=120, height=25)

    Basic_cblist_2=[]

    Basic_cb2 = tk.ttk.Combobox(Basic_mode, height=10, values=Basic_cblist_2)
    Basic_cb2.place(x=45, y=545, width=120, height=25)

    Basic_btn1=tk.Button(Basic_mode, text="선택")
    Basic_btn1.place(x=45, y=770, width=120, height=50)

    Basic_listbox1=tk.Listbox(Basic_mode)
    Basic_listbox1.yview()
    Basic_listbox1.place(x=180, y=320, width=800, height=500)

    Basic_cblist_3=[]

    Basic_cb3=tk.ttk.Combobox(Basic_mode,height=10, values=Basic_cblist_3)
    Basic_cb3.place(x=360, y=840, width=100, height=25)
    Basic_ent1=tk.Entry(Basic_mode)
    Basic_ent1.place(x=475, y=840, width=160, height=25)
    Basic_btn2=tk.Button(Basic_mode, text="검색")
    Basic_btn2.place(x=650, y=840, width=100, height=25)

    Basic_btn3=tk.Button(Basic_mode, text="입고리스트", command=IMIP_page)
    Basic_btn3.place(x=45, y=210, width=200, height=40)
    Basic_btn4=tk.Button(Basic_mode, text="출고리스트", command=IMOP_page)
    Basic_btn4.place(x=45, y=260, width=200, height=40)
    Basic_btn5=tk.Button(Basic_mode, text="입/출고\n처리", command=IPOP_page)
    Basic_btn5.place(x=830, y=210, width=150, height=90)

    Home.mainloop()



Passward=Login() # 로그인 리턴값

if Passward == Passward_ch : # 정상적인 로그인 수행
    Main()

else : # 로그인 불가능
    print('시스템을 종료합니다.')

# for i in range(1, 1001):
#     Basic_listbox3.insert(i, str(i) + "/1000")



