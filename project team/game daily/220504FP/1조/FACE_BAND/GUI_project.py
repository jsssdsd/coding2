'''
class user_data():
    def __init__(self,id,pw,name,n_name,birth,gen,email):
        self.id=id
        self.pw=pw
        self.name=name
        self.n_name=n_name
        self.birth=birth
        self.gen=gen
        self.email=email

class postClass:
    def __init__(self,postNum,ID,contents,time,secret,nick):
        self.postNum=postNum
        self.num=num
        self.contents=contents
        self.time=time
        self.ID=ID
        self.secret=secret
        self.nick = nick

class commentClass:
    def __init__(self,postNum,commentNum,id,nick,time,comment):
        self.postNum=postNum
        self.commentNum=commentNum
        self.id=id
        self.nick = nick
        self.time=time
        self.comment=comment
'''

# GUI
import tkinter as tk
import tkinter.font as tkfont

from PIL import Image, ImageTk
from tkinter import messagebox
from itertools import count

# 필요 raw파일 생성 및 체크
import boot_module as bm
bm.checklist()


# 로그인 창
def login_gui():
    import tkinter as tk

    # 로그인 누르면... 확인작업
    def check_data():
        import id_pw as ip
        global user

        def destroy():
            passing.destroy()

        a=entry1.get()
        b=entry2.get()
        # 아이디,패스워드 올바르면
        if ip.check_id_pw(a,b):

            start.destroy()
            passing=tk.Tk()
            passing.geometry('400x150')
            passing.resizable(False,False)
            user=ip.check_id_pw(a,b)
            tk.Label(passing,text='로그인 성공').pack(expand=True)
            tk.Button(passing,text='닫기',command=destroy).pack()
            passing.mainloop()

        else:

            def destroy():
                win2.destroy()

            win2 = tk.Toplevel()
            win2.geometry('400x100')
            win2.resizable(False, False)  # 창 사이즈 변경 여부 속성 지정
            tk.Label(win2, text="해당 사용자가 없습니다.").pack(expand=True)
            tk.Button(win2, text="닫기", command=destroy).pack(expand=True)

            win2.mainloop()

    def pp(event):
        import id_pw as ip
        global user

        def destroy():
            passing.destroy()

        a=entry1.get()
        b=entry2.get()
        # 아이디,패스워드 올바르면
        if ip.check_id_pw(a,b):
            start.destroy()
            passing=tk.Tk()
            passing.geometry('400x150')
            passing.resizable(False,False)
            user=ip.check_id_pw(a,b)
            tk.Label(passing,text='로그인 성공').pack(expand=True)
            tk.Button(passing,text='닫기',command=destroy).pack(expand=True)
            passing.mainloop()

        else:

            def destroy():
                win2.destroy()

            win2 = tk.Toplevel()
            win2.geometry('400x100')
            win2.resizable(False, False)  # 창 사이즈 변경 여부 속성 지정
            tk.Label(win2, text="해당 사용자가 없습니다.").pack(expand=True)
            tk.Button(win2, text="닫기", command=destroy).pack(expand=True)

            win2.mainloop()

    # 회원가입
    def newAccount():

        def destroy():
            win2.destroy()

        def check_man():
            if CheckVar1.get():
                checkbutton2.configure(state='disabled')
            else:
                checkbutton2.configure(state='active')

        def check_girl():
            if CheckVar2.get():
                checkbutton1.configure(state='disabled')
            else:
                checkbutton1.configure(state='active')

        def confirm():
            import EnrollAccount_test as Et
            a=entry7.get()
            b=entry8.get()
            c=entry9.get()
            d=entry10.get()
            e=entry11.get()
            f_1=CheckVar1.get()
            f_2=CheckVar2.get()
            g=entry13.get()

            if f_1:
                f='남자'
            elif f_2:
                f='여자'
            else:
                f='오류'

            if Et.SaveUser(a,b,c,d,e,f,g)=='id':
                def destroy2():
                    win3.destroy()
                win3 = tk.Toplevel()
                win3.geometry('400x100')
                win3.resizable(False, False)  # 창 사이즈 변경 여부 속성 지정
                tk.Label(win3, text='ID가 중복됩니다.').pack(expand=True)
                tk.Button(win3, text='닫기', command=destroy2).pack(expand=True)

            elif Et.SaveUser(a,b,c,d,e,f,g)=='id_alpha':
                def destroy2():
                    win3.destroy()
                win3 = tk.Toplevel()
                win3.geometry('400x100')
                win3.resizable(False, False)  # 창 사이즈 변경 여부 속성 지정
                tk.Label(win3, text='ID는 영어와 숫자로 이루어져야 합니다.').pack(expand=True)
                tk.Button(win3, text='닫기', command=destroy2).pack(expand=True)

            elif Et.SaveUser(a,b,c,d,e,f,g)=='pw':
                def destroy2():
                    win3.destroy()
                win3 = tk.Toplevel()
                win3.geometry('400x100')
                win3.resizable(False, False)  # 창 사이즈 변경 여부 속성 지정
                tk.Label(win3, text='pw가 유효하지 않습니다. 숫자4개이상 사용하세요.').pack(expand=True)
                tk.Button(win3, text='닫기', command=destroy2).pack(expand=True)

            elif Et.SaveUser(a, b, c, d, e, f, g) == 'nick':
                def destroy2():
                    win3.destroy()
                win3 = tk.Toplevel()
                win3.geometry('400x100')
                win3.resizable(False, False)  # 창 사이즈 변경 여부 속성 지정
                tk.Label(win3, text='닉네임이 중복됩니다.').pack(expand=True)
                tk.Button(win3, text='닫기', command=destroy2).pack(expand=True)

            elif Et.SaveUser(a, b, c, d, e, f, g) == 'birth':
                def destroy2():
                    win3.destroy()
                win3 = tk.Toplevel()
                win3.geometry('400x100')
                win3.resizable(False, False)  # 창 사이즈 변경 여부 속성 지정
                tk.Label(win3, text='생년월일 6글자로 입력하세요.').pack(expand=True)
                tk.Button(win3, text='닫기', command=destroy2).pack(expand=True)

            elif Et.SaveUser(a, b, c, d, e, f, g) == 'gen':
                def destroy2():
                    win3.destroy()
                win3 = tk.Toplevel()
                win3.geometry('400x100')
                win3.resizable(False, False)  # 창 사이즈 변경 여부 속성 지정
                tk.Label(win3, text='성별을 선택하세요.').pack(expand=True)
                tk.Button(win3, text='닫기', command=destroy2).pack(expand=True)

            elif Et.SaveUser(a, b, c, d, e, f, g) == 'email':
                def destroy2():
                    win3.destroy()
                win3 = tk.Toplevel()
                win3.geometry('400x100')
                win3.resizable(False, False)  # 창 사이즈 변경 여부 속성 지정
                tk.Label(win3, text='이메일 형식에 맞지 않습니다.').pack(expand=True)
                tk.Button(win3, text='닫기', command=destroy2).pack(expand=True)

            else:
                def destroy2():
                    win3.destroy()
                win3 = tk.Toplevel()
                win3.geometry('400x150')
                win3.resizable(False, False)  # 창 사이즈 변경 여부 속성 지정
                tk.Label(win3, text='정상적으로 회원가입 됬습니다.\n 가입이벤트로 하루살이 50코인을 지급해드립니다.\n 환영합니다~').pack(expand=True)
                tk.Button(win3, text='닫기', command=destroy2).pack(expand=True)
                win2.destroy()

        win2 = tk.Toplevel()
        win2.geometry('400x300')
        win2.resizable(False, False)  # 창 사이즈 변경 여부 속성 지정
        tk.Label(win2, text="아이디\t:").place(x=70, y=30)
        tk.Label(win2, text="패스워드\t:").place(x=70, y=60)
        tk.Label(win2, text="이름\t:").place(x=70, y=90)
        tk.Label(win2, text="닉네임\t:").place(x=70, y=120)
        tk.Label(win2, text="생년월일\t:").place(x=70, y=150)
        tk.Label(win2, text="성별\t:").place(x=70, y=180)
        CheckVar1 = tk.IntVar()
        checkbutton1 = tk.Checkbutton(win2, text="남자",variable= CheckVar1, command=check_man)
        CheckVar2 = tk.IntVar()
        checkbutton2 = tk.Checkbutton(win2, text="여자",variable= CheckVar2, command=check_girl)
        tk.Label(win2, text="이메일\t:").place(x=70, y=210)
        entry7=tk.Entry(win2)
        entry7.place(x=150, y=30)
        entry8=tk.Entry(win2)
        entry8.place(x=150, y=60)
        entry9=tk.Entry(win2)
        entry9.place(x=150, y=90)
        entry10=tk.Entry(win2)
        entry10.place(x=150, y=120)
        entry11=tk.Entry(win2)
        entry11.place(x=150, y=150)
        checkbutton1.place(x=147, y=178)
        checkbutton2.place(x=227, y=178)
        entry13=tk.Entry(win2)
        entry13.place(x=150, y=210)

        tk.Button(win2, text="회원가입", command=confirm).place(x=120, y=250)
        tk.Button(win2, text="취소", command=destroy).place(x=230, y=250)

        win2.mainloop()

    # 아이디 찾기
    def foundAccount():

        def destroy():
            win2.destroy()
        def let_f():
            import find_test as ft
            import tkinter.messagebox as tm

            a=entry3.get()
            b=entry4.get()
            c=entry5.get()
            d=entry6.get()

            if ft.user_find_id(a,b,c,d):
                def destroy2():
                    win3.destroy()
                win3 = tk.Toplevel()
                win3.geometry('400x300')
                win3.resizable(False, False)  # 창 사이즈 변경 여부 속성 지정
                tk.Label(win3, text='ID :\t{}\nPS :\t{}'.format(ft.user_find_id(a, b, c, d)[0],ft.user_find_id(a, b, c, d)[1])).pack()
                tk.Button(win3, text='닫기', command=destroy2).pack()
                win2.destroy()
            else:
                tm.showerror('회원정보 찾기','해당하는 유저가 없습니다.')
                win2.destroy()


        win2 = tk.Toplevel()
        win2.geometry('400x300')
        win2.resizable(False, False)  # 창 사이즈 변경 여부 속성 지정
        tk.Label(win2, text="이름\t:").place(x=70, y=30)
        tk.Label(win2, text="생년월일\t:").place(x=70, y=80)
        tk.Label(win2, text="성별\t:").place(x=70, y=130)
        tk.Label(win2, text="이메일\t:").place(x=70, y=180)
        entry3=tk.Entry(win2)
        entry3.place(x=150, y=30)
        entry4=tk.Entry(win2)
        entry4.place(x=150, y=80)
        entry5=tk.Entry(win2)
        entry5.place(x=150, y=130)
        entry6=tk.Entry(win2)
        entry6.place(x=150, y=180)

        tk.Button(win2, text="확인", command=let_f).place(x=120, y=230)
        tk.Button(win2, text="취소", command=destroy).place(x=230, y=230)

        win2.mainloop()

    start = tk.Tk()
    start.title('FACE_BAND')  # 창의 타이틀 명
    start.geometry('400x300')  # 창의 사이즈
    start.resizable(False, False)  # 창 사이즈 변경 여부 속성 지정
    tk.Label(start, text="ID\t:").place(x=80, y=70)
    tk.Label(start, text="Password\t:").place(x=80, y=100)
    entry1=tk.Entry(start)
    entry1.place(x=170, y=70)
    entry2=tk.Entry(start, show='*')
    entry2.bind('<Return>',pp)
    entry2.place(x=170, y=100)
    tk.Button(start, text="로그인", command=check_data).place(x=60, y=150)
    tk.Button(start, text="회원가입", command=newAccount).place(x=130, y=150)
    tk.Button(start, text="아이디/비밀번호 찾기", command=foundAccount).place(x=210, y=150)

    start.mainloop()


# 메인 창
def main_gui():
    global user
    import search_post as sp
    from tkinter import ttk
    import time

    # 메인화면 가기
    def changeFrame1():
        frame_showing1.tkraise()

    # 내가 작성한 글 보기
    def changeFrame2():
        no_now2.delete(0,tk.END)
        no_now2.insert(tk.END,'1')
        Mypost()
        no_last2.configure(text='/ {}'.format(maxPage2))
        frame_myPage.tkraise()

    # 개인정보 수정하기
    def myData():
        global user
        global mydata

        if mydata:
            mydata.destroy()

        def changeAC():
            global user

            def mod_ac():
                global user

                import EnrollAccount_test as Et
                import change_test as ct

                x= entry_pw.get()
                y=entry_N.get()
                z=entry_e.get()

                if x != u_p:
                    if Et.check_pw(x):
                        user=ct.change_pw(user,x)
                        tk.messagebox.showinfo(message='비밀번호가 성공적으로 재설정 되었습니다.')
                    else:
                        tk.messagebox.showerror(message='비밀번호가 규격에 맞지 않습니다.(숫자 4개 이상 포함)')

                if y != u_N:
                    if Et.check_overlap(y,3):
                        user=ct.change_nick(user,y)
                        tk.messagebox.showinfo(message='닉네임이 성공적으로 변경 되었습니다.')
                    else:
                        tk.messagebox.showerror(message='닉네임이 중복됩니다.')

                if z != u_e:
                    if Et.check_overlap(z,6):
                        user=ct.change_email(user,z)
                        tk.messagebox.showinfo(message='이메일이 성공적으로 변경 되었습니다.')
                    else:
                        tk.messagebox.showerror(message='이메일이 중복됩니다.')
                MyshowRecent()
                mydata.destroy()

            def back_ac():
                mydata.destroy()

            a = entry1.get()

            if a==user.pw:
                u_i = user.id
                u_p = user.pw
                u_n = user.name
                u_N = user.n_name
                u_b = user.birth
                u_g = user.gen
                u_e = user.email
                frame_account = tk.Frame(mydata)
                frame_account.place(x=0, y=0, width=400, height=500)

                label0 = tk.Label(frame_account, text='아이디 :')
                label0.place(x=120, y=100)
                label0 = tk.Label(frame_account, text='{}'.format(u_i))
                label0.place(x=200, y=100)

                label2 = tk.Label(frame_account, text='패스워드 :')
                label2.place(x=120, y=140)
                entry_pw=tk.Entry(frame_account,width=0)
                entry_pw.insert(0,u_p)
                entry_pw.place(x=200, y=140)

                label3 = tk.Label(frame_account, text='이름 :')
                label3.place(x=120, y=180)
                label3_1 = tk.Label(frame_account, text='{}'.format(u_n))
                label3_1.place(x=200, y=180)

                label4 = tk.Label(frame_account, text='닉네임 :')
                label4.place(x=120, y=220)
                entry_N=tk.Entry(frame_account,width=0)
                entry_N.insert(0,u_N)
                entry_N.place(x=200, y=220)


                label5 = tk.Label(frame_account, text='생년월일 :')
                label5.place(x=120, y=260)
                label5_1 = tk.Label(frame_account, text='{}'.format(u_b))
                label5_1.place(x=200, y=260)

                label6 = tk.Label(frame_account, text='성별 :')
                label6.place(x=120, y=300)
                label6_1 = tk.Label(frame_account, text='{}'.format(u_g))
                label6_1.place(x=200, y=300)

                label7 = tk.Label(frame_account, text='이메일 :')
                label7.place(x=120, y=340)
                entry_e = tk.Entry(frame_account, width=0)
                entry_e.insert(0,u_e)
                entry_e.place(x=200, y=340)

                confirm_btn=tk.Button(frame_account,  text='수정하기', command=mod_ac)
                confirm_btn.place(x=120, y=400)
                back_btn=tk.Button(frame_account,  text='취소하기', command=back_ac)
                back_btn.place(x=200, y=400)

                frame_account.tkraise()
            else:
                pass

        def pp(event):
            label1.config(text='비번이 틀렸습니다.')

        mydata=tk.Toplevel()
        mydata.geometry('400x500')
        mydata.title('개인정보 수정')
        mydata.resizable(False,False)

        frame_confirm=tk.Frame(mydata)
        frame_confirm.place(x=0,y=0,width=400,height=500)

        label1=tk.Label(frame_confirm,text='비밀번호 확인')
        label1.place(x=150,y=190)
        entry1=tk.Entry(frame_confirm, show='*')
        entry1.place(x=125,y=230)

        btn1=tk.Button(frame_confirm, command=changeAC,text='확인')
        btn1.bind('<Button-1>',pp)
        btn1.place(x=175,y=270)

        mydata.mainloop()

    # 로그아웃 하기
    def log_out():
        global user
        user = 'no'
        main.destroy()

    # 프로그램 종료하기
    def EXIT():
        main.destroy()

    # 최근 게시물 리스트 출력하기
    def showRecentAll():
        global temp_1
        global maxPage
        global listNum

        import follow_module as fm

        listbox1.delete(0, tk.END)
        listbox2.delete(0,tk.END)
        listbox3.delete(0, tk.END)
        listNum = 20
        if sp.search_all():
            maxPage=sp.show_page(sp.class_list(sp.search_all()),listNum)[1]
            temp_1=sp.show_page(sp.class_list(sp.search_all()),listNum)[2]

            for i in range(len(sp.show_page(sp.class_list(sp.search_all()),listNum)[0])):
                NUM='{}'.format(sp.show_page(sp.class_list(sp.search_all()),listNum)[0][i].num)
                NICK=' {}'.format(sp.show_page(sp.class_list(sp.search_all()),listNum)[0][i].nick)
                listbox1.insert(tk.END,NUM)
                listbox3.insert(tk.END,NICK)
                if user.id == sp.show_page(sp.class_list(sp.search_all()), listNum)[0][i].ID:
                    CONTENTS = ' {}'.format(sp.show_page(sp.class_list(sp.search_all()), listNum)[0][i].contents)
                    listbox2.insert(tk.END, CONTENTS)
                elif sp.show_page(sp.class_list(sp.search_all()), listNum)[0][i].secret == 'yes':
                    if fm.followBack(user,sp.show_page(sp.class_list(sp.search_all()), listNum)[0][i]):
                        CONTENTS = '<<<비밀글 입니다.>>>'
                        listbox2.insert(tk.END, CONTENTS)
                    else:
                        CONTENTS = ' {}'.format(sp.show_page(sp.class_list(sp.search_all()), listNum)[0][i].contents)
                        listbox2.insert(tk.END, CONTENTS)
                else:
                    CONTENTS = ' {}'.format(sp.show_page(sp.class_list(sp.search_all()), listNum)[0][i].contents)
                    listbox2.insert(tk.END, CONTENTS)

        else:
            listbox2.insert(tk.END,'작성한 게시글이 없습니다.')
            maxPage = 1
            pass

    # 쪽수 검색하기
    def showSelnum():
        global maxPage
        global temp_1
        global prev_num

        import follow_module as fm

        try:
            if int(no_now.get()) > int(maxPage):
                tk.messagebox.showerror(message='게시글 최대 페이지를 초과했습니다.')
                if prev_num:
                    no_now.delete(0, tk.END)
                    no_now.insert(tk.END, prev_num)
                else:
                    no_now.delete(0, tk.END)
                    no_now.insert(tk.END, 1)
                return

            listbox1.delete(0, tk.END)
            listbox2.delete(0,tk.END)
            listbox3.delete(0, tk.END)

            a=int(no_now.get())
            b=int(maxPage)

            for i in range(len(sp.sel_others(a,b)[0])):
                NUM='{}'.format(sp.sel_others(a,b)[0][i].num)
                NICK=' {}'.format(sp.sel_others(a,b)[0][i].nick)
                listbox1.insert(tk.END,NUM)
                listbox3.insert(tk.END,NICK)
                if user.id ==  sp.sel_others(a,b)[0][i].ID:
                    CONTENTS = ' {}'.format(sp.sel_others(a,b)[0][i].contents)
                    listbox2.insert(tk.END, CONTENTS)
                elif sp.sel_others(a,b)[0][i].secret == 'yes':
                    if fm.followBack(user,sp.sel_others(a,b)[0][i]):
                        CONTENTS = '<<<비밀글 입니다.>>>'
                        listbox2.insert(tk.END, CONTENTS)
                    else:
                        CONTENTS = ' {}'.format(sp.sel_others(a, b)[0][i].contents)
                        listbox2.insert(tk.END, CONTENTS)
                else:
                    CONTENTS = ' {}'.format(sp.sel_others(a,b)[0][i].contents)
                    listbox2.insert(tk.END, CONTENTS)
            prev_num=a
        except ValueError:
            tk.messagebox.showerror(message='숫자를 입력해 주세요...')
            if prev_num:
                no_now.delete(0,tk.END)
                no_now.insert(tk.END,prev_num)
            else:
                no_now.delete(0,tk.END)
                no_now.insert(tk.END,1)
            return

    # 게임하기 보기
    def showGame():
        global game
        global user
        game='yes'
        main.destroy()

    # 최신글 보기
    def showRecent():
        no_now.delete(0,tk.END)
        no_now.insert(tk.END,'1')
        showRecentAll()
        no_last.configure(text='/ {}'.format(maxPage))
        frame_list.tkraise()

    # 1쪽 보기
    def showRecent2():
        no_now.delete(0,tk.END)
        no_now.insert(tk.END,'1')
        showRecentAll()
        no_last.configure(text='/ {}'.format(maxPage))
        frame_list.tkraise()

    # 마지막 쪽 보기
    def showLast():
        global maxPage
        global prev_num
        import follow_module as fm
        if maxPage != 1:
            no_now.delete(0,tk.END)
            no_now.insert(tk.END,maxPage)

            listbox1.delete(0, tk.END)
            listbox2.delete(0, tk.END)
            listbox3.delete(0, tk.END)

            a = int(maxPage)
            b = int(maxPage)

            for i in range(len(sp.sel_others(a, b)[0])):
                NUM = '{}'.format(sp.sel_others(a, b)[0][i].num)
                NICK = ' {}'.format(sp.sel_others(a, b)[0][i].nick)
                listbox1.insert(tk.END, NUM)
                listbox3.insert(tk.END, NICK)
                if user.id ==  sp.sel_others(a,b)[0][i].ID:
                    CONTENTS = ' {}'.format(sp.sel_others(a,b)[0][i].contents)
                    listbox2.insert(tk.END, CONTENTS)
                elif sp.sel_others(a,b)[0][i].secret == 'yes':
                    if fm.followBack(user,sp.sel_others(a,b)[0][i]):
                        CONTENTS = '<<<비밀글 입니다.>>>'
                        listbox2.insert(tk.END, CONTENTS)
                    else:
                        CONTENTS = ' {}'.format(sp.sel_others(a, b)[0][i].contents)
                        listbox2.insert(tk.END, CONTENTS)
                else:
                    CONTENTS = ' {}'.format(sp.sel_others(a,b)[0][i].contents)
                    listbox2.insert(tk.END, CONTENTS)

            prev_num = a
            frame_list.tkraise()
        else:
            pass

    # 쪽수 검색하기
    def showSel(event):
        showSelnum()
        frame_list.tkraise()

    # 이전 쪽 보기
    def showPrev():
        global prev_num
        try:
            a=int(no_now.get())
            if a != 1:
                prev_num = a - 1
                no_now.delete(0,tk.END)
                no_now.insert(tk.END,a-1)
                showSelnum()
                frame_list.tkraise()

        except ValueError:
            a = prev_num
            if a != 1:
                prev_num = a - 1
                no_now.delete(0, tk.END)
                no_now.insert(tk.END, a - 1)
                showSelnum()
                frame_list.tkraise()

    # 다음 쪽 보기
    def showNext():
        global maxPage
        global prev_num
        try:
            a=int(no_now.get())
            if a != maxPage:
                prev_num = a + 1
                no_now.delete(0,tk.END)
                no_now.insert(tk.END,a+1)
                showSelnum()
                frame_list.tkraise()
        except ValueError:
            a = prev_num
            if a != maxPage:
                prev_num = a + 1
                no_now.delete(0, tk.END)
                no_now.insert(tk.END, a + 1)
                showSelnum()
                frame_list.tkraise()

    # 인기글 보기
    def showCeleb():
        showCelebAll()
        frame_celeb.tkraise()

    def showCelebAll():
        global user
        global temp_5
        import like_module as lm
        import follow_module as fm

        celebbox1.delete(0, tk.END)
        celebbox2.delete(0,tk.END)
        celebbox3.delete(0, tk.END)
        temp_5_1=lm.likeCount(7,20)
        if temp_5_1:
            temp_5 = []
            for i in range(len(temp_5_1)):
                temp_5.append(temp_5_1[i][0])
            for i in range(len(temp_5)):
                NUM='{}'.format(temp_5_1[i][1])
                NICK=' {}'.format(temp_5[i][5])
                celebbox1.insert(tk.END,NUM)
                celebbox3.insert(tk.END,NICK)
                if temp_5[i][1] == user.id :
                    CONTENTS = ' {}'.format(temp_5[i][2])
                    celebbox2.insert(tk.END, CONTENTS)
                elif temp_5[i][4] == 'yes':
                    if fm.followBack2(user,temp_5[i]):
                        CONTENTS = '<<<비밀글 입니다.>>>'
                        celebbox2.insert(tk.END, CONTENTS)
                    else:
                        CONTENTS = ' {}'.format(temp_5[i][2])
                        celebbox2.insert(tk.END, CONTENTS)
                else:
                    CONTENTS = ' {}'.format(temp_5[i][2])
                    celebbox2.insert(tk.END, CONTENTS)
        else:
            celebbox2.insert(tk.END,'작성한 게시글이 없습니다.')
        temp_5=sp.class_list(temp_5)
    # 인기글 클릭
    def selCeleb(event):
        global user
        global openPost
        global temp_5

        import follow_module as fm

        if openPost:
            openPost.destroy()
        page_index=celebbox2.curselection()[0]
        showing=temp_5[page_index]

        if user.id == showing.ID:
            celebAlt1()
        elif showing.secret == 'no':
            celebAlt2_1()
        elif fm.followBack(user,showing):
            celebAlt2_2_1()
        else:
            celebAlt2_2_2()
        pass
    # 내가 쓴 글 Alt 1
    def celebAlt1():
        global temp_5
        global user
        global openPost
        import like_module as lm
        import comment_module as cm

        def delPost():
            import del_post as dp
            x=messagebox.askyesno(message='정말 삭제하시겠습니까?')
            if x:
                dp.delmyPost(showing)
                openPost.destroy()
                showRecent()
            else:
                openPost.tkraise()

        page_index=celebbox2.curselection()[0]
        showing=temp_5[page_index]

        TIME = time.localtime(float(showing.time))
        TIME = time.strftime('%Y-%m-%d %I:%M:%S %p', TIME)

        openPost = tk.Toplevel(main)
        openPost.geometry('600x400')
        openPost.title('내가 작성한 글')
        openPost.resizable(False,False)

        postFrame1 = tk.Frame(openPost)
        postFrame1.place(x=0, y=0, width=600, height=400)
        postLabel1 = tk.Label(postFrame1, text=showing.contents, bg='white')
        postLabel1.place(x=50, y=50, width=350, height=50)
        postLabel2 = tk.Label(postFrame1, text=TIME, bg='white', anchor='e', state='disabled')
        postLabel2.place(x=50, y=110, width=350, height=25)

        a=lm.cntLike(showing)
        lable1 = tk.Label(postFrame1, text='♥ {}'.format(a))
        lable1.place(x=440, y=110, width=50, height=25)

        btn1 = tk.Button(postFrame1, text='삭제하기',command=delPost)
        btn1.place(x=500, y=110, width=50, height=25)

        # 댓글달기
        cm.Makecomment(user,showing,openPost)

        openPost.mainloop()

    # 남이 작성하고 비밀글 아님 Alt 2-1
    def celebAlt2_1():
        global temp_5
        global user
        global openPost
        import comment_module as cm
        import follow_module as fm
        import like_module as lm

        def btnFollowing():
            fm.followYou(user,showing)
            btn2 = tk.Button(postFrame1, text='언팔로우',command=btnUnfollowing)
            btn2.place(x=510, y=110, width=50, height=25)
            showCeleb()

        def btnUnfollowing():
            fm.unfollowYou(user,showing)
            btn2 = tk.Button(postFrame1, text='팔로우',command=btnFollowing)
            btn2.place(x=510, y=110, width=50, height=25)
            showCeleb()

        def btnLike():
            lm.likeowYou(user,showing)
            btn1 = tk.Button(postFrame1, text='♥', command=btnUnlike)
            btn1.place(x=440, y=110, width=50, height=25)
            showCeleb()

        def btnUnlike():
            lm.unlikeYou(user,showing)
            btn1 = tk.Button(postFrame1, text='♡', command=btnLike)
            btn1.place(x=440, y=110, width=50, height=25)
            showCeleb()

        page_index = celebbox2.curselection()[0]
        showing = temp_5[page_index]

        TIME = time.localtime(float(showing.time))
        TIME = time.strftime('%Y-%m-%d %I:%M:%S %p', TIME)

        openPost = tk.Toplevel(main)
        openPost.geometry('600x400')
        openPost.title('{}'.format(showing.contents))

        postFrame2 = tk.Frame(openPost, bg='white')
        postFrame2.place(x=0, y=200)

        postFrame1 = tk.Frame(openPost)
        postFrame1.place(x=0, y=0, width=600, height=400)
        postLabel1 = tk.Label(postFrame1, text=showing.contents, bg='white')
        postLabel1.place(x=50, y=50, width=350, height=50)
        postLabel2 = tk.Label(postFrame1, text=TIME, bg='white', anchor='e', state='disabled')
        postLabel2.place(x=50, y=110, width=350, height=25)

        # 좋아요 여부로 버튼 바꾸기
        if lm.checkLike(user,showing):
            btn1 = tk.Button(postFrame1, text='♡', command=btnLike)
            btn1.place(x=440, y=110, width=50, height=25)
        else:
            btn1 = tk.Button(postFrame1, text='♥', command=btnUnlike)
            btn1.place(x=440, y=110, width=50, height=25)

        # 팔로우 여부 확인으로 버튼 바꾸기
        if fm.checkFollow(user,showing):
            btn2 = tk.Button(postFrame1, text='팔로우',command=btnFollowing)
            btn2.place(x=510, y=110, width=50, height=25)
        else:
            btn2 = tk.Button(postFrame1, text='언팔로우',command=btnUnfollowing)
            btn2.place(x=510, y=110, width=50, height=25)

        cm.Makecomment(user,showing,openPost)

        openPost.mainloop()

    # 남이 작성하고 비밀글이고 맞팔 X Alt2-2-1
    def celebAlt2_2_1():
        global temp_5
        global user
        global openPost

        def cc():
            openPost.destroy()

        openPost = tk.Toplevel(main)
        openPost.geometry('600x400')
        openPost.title('맞팔로우해야 볼 수 있습니다.')

        postFrame2 = tk.Frame(openPost, bg='white')
        postFrame2.place(x=0, y=200)

        postFrame1 = tk.Frame(openPost)
        postFrame1.place(x=0, y=0, width=600, height=400)
        postLabel1 = tk.Label(postFrame1, text='맞팔로우 해야 볼 수 있습니다.', bg='white')
        postLabel1.place(x=50, y=50, width=350, height=50)

        btn2 = tk.Button(postFrame1, text='닫기', command=cc)
        btn2.place(x=510, y=110, width=50, height=25)

        openPost.mainloop()

    # 남이 작성하고 비밀글이고 맞팔 0 Alt2-2-2
    def celebAlt2_2_2():
        global temp_5
        global user
        global openPost
        import comment_module as cm
        import follow_module as fm
        import like_module as lm

        def btnUnfollowing():
            fm.unfollowYou(user,showing)
            openPost.destroy()
            showCeleb()

        def btnLike():
            lm.likeowYou(user,showing)
            btn1 = tk.Button(postFrame1, text='♥', command=btnUnlike)
            btn1.place(x=440, y=110, width=50, height=25)
            showCeleb()

        def btnUnlike():
            lm.unlikeYou(user,showing)
            btn1 = tk.Button(postFrame1, text='♡', command=btnLike)
            btn1.place(x=440, y=110, width=50, height=25)
            showCeleb()

        page_index = celebbox2.curselection()[0]
        showing = temp_5[page_index]

        TIME = time.localtime(float(showing.time))
        TIME = time.strftime('%Y-%m-%d %I:%M:%S %p', TIME)

        openPost = tk.Toplevel(main)
        openPost.geometry('600x400')
        openPost.title('{}'.format(showing.contents))

        postFrame2 = tk.Frame(openPost, bg='white')
        postFrame2.place(x=0, y=200)

        postFrame1 = tk.Frame(openPost)
        postFrame1.place(x=0, y=0, width=600, height=400)
        postLabel1 = tk.Label(postFrame1, text=showing.contents, bg='white')
        postLabel1.place(x=50, y=50, width=350, height=50)
        postLabel2 = tk.Label(postFrame1, text=TIME, bg='white', anchor='e', state='disabled')
        postLabel2.place(x=50, y=110, width=350, height=25)

        if lm.checkLike(user,showing):
            btn1 = tk.Button(postFrame1, text='♡', command=btnLike)
            btn1.place(x=440, y=110, width=50, height=25)
        else:
            btn1 = tk.Button(postFrame1, text='♥', command=btnUnlike)
            btn1.place(x=440, y=110, width=50, height=25)

        btn2 = tk.Button(postFrame1, text='언팔로우',command=btnUnfollowing)
        btn2.place(x=510, y=110, width=50, height=25)

        cm.Makecomment(user,showing,openPost)

        openPost.mainloop()

    # 팔로우 게시물 보기
    def showFollow():
        no_now3.delete(0,tk.END)
        no_now3.insert(tk.END,'1')
        showFollowAll()
        no_last3.configure(text='/ {}'.format(maxPage3))
        frame_follow.tkraise()

    def showFollowAll():
        global temp_3
        global maxPage3
        global listNum3
        global user

        import follow_module as fm

        followbox1.delete(0, tk.END)
        followbox2.delete(0,tk.END)
        followbox3.delete(0, tk.END)
        listNum3 = 20
        if sp.search_follow(user):
            maxPage3=sp.show_page(sp.class_list(sp.search_follow(user)),listNum)[1]
            temp_3=sp.show_page(sp.class_list(sp.search_follow(user)),listNum)[2]

            for i in range(len(sp.show_page(sp.class_list(sp.search_follow(user)),listNum)[0])):
                NUM='{}'.format(sp.show_page(sp.class_list(sp.search_follow(user)),listNum)[0][i].num)
                NICK=' {}'.format(sp.show_page(sp.class_list(sp.search_follow(user)),listNum)[0][i].nick)
                followbox1.insert(tk.END,NUM)
                followbox3.insert(tk.END,NICK)
                if sp.show_page(sp.class_list(sp.search_follow(user)), listNum)[0][i].secret == 'yes':
                    if fm.followBack(user,sp.show_page(sp.class_list(sp.search_follow(user)), listNum)[0][i]):
                        CONTENTS = '<<<비밀글 입니다.>>>'
                        followbox2.insert(tk.END, CONTENTS)
                    else:
                        CONTENTS = ' {}'.format(sp.show_page(sp.class_list(sp.search_follow(user)), listNum)[0][i].contents)
                        followbox2.insert(tk.END, CONTENTS)
                else:
                    CONTENTS = ' {}'.format(sp.show_page(sp.class_list(sp.search_follow(user)), listNum)[0][i].contents)
                    followbox2.insert(tk.END, CONTENTS)

        else:
            followbox2.insert(tk.END,'작성한 게시글이 없습니다.')
            maxPage3 = 1
            pass
        pass

    # 이전 쪽 보기
    def showfollPrev():
        global prev_num3
        try:
            a=int(no_now3.get())
            if a != 1:
                prev_num3 = a - 1
                no_now3.delete(0,tk.END)
                no_now3.insert(tk.END,a-1)
                FollshowSelnum()
                frame_follow.tkraise()

        except ValueError:
            a = prev_num3
            if a != 1:
                prev_num3 = a - 1
                no_now3.delete(0, tk.END)
                no_now3.insert(tk.END, a - 1)
                FollshowSelnum()
                frame_follow.tkraise()

    # 다음 쪽 보기
    def showfollNext():
        global maxPage3
        global prev_num3
        try:
            a=int(no_now3.get())
            if a != maxPage3:
                prev_num3 = a + 1
                no_now3.delete(0,tk.END)
                no_now3.insert(tk.END,a+1)
                FollshowSelnum()
                frame_follow.tkraise()
        except ValueError:
            a = prev_num3
            if a != maxPage3:
                prev_num3 = a + 1
                no_now3.delete(0, tk.END)
                no_now3.insert(tk.END, a + 1)
                FollshowSelnum()
                frame_follow.tkraise()

    # 팔로잉 쪽수 검색
    def showfollSel(event):
        FollshowSelnum()
        frame_follow.tkraise()

    # 팔로잉 마지막 쪽 보기
    def showfollLast():
        global maxPage3
        global prev_num3
        global temp_3
        import follow_module as fm
        if maxPage3 != 1:
            no_now3.delete(0,tk.END)
            no_now3.insert(tk.END,maxPage3)

            followbox1.delete(0, tk.END)
            followbox2.delete(0, tk.END)
            followbox3.delete(0, tk.END)

            a = int(maxPage3)

            for i in range(len(sp.sel_follow(temp_3, a))):
                NUM = '{}'.format(sp.sel_follow(temp_3, a)[i].num)
                NICK = ' {}'.format(sp.sel_follow(temp_3,a)[i].nick)
                followbox1.insert(tk.END, NUM)
                followbox3.insert(tk.END, NICK)
                if user.id ==  sp.sel_follow(temp_3,a)[i].ID:
                    CONTENTS = ' {}'.format(sp.sel_follow(temp_3,a)[i].contents)
                    followbox2.insert(tk.END, CONTENTS)
                elif sp.sel_follow(temp_3,a)[i].secret == 'yes':
                    if fm.followBack(user,sp.sel_follow(temp_3,a)[i]):
                        CONTENTS = '<<<비밀글 입니다.>>>'
                        followbox2.insert(tk.END, CONTENTS)
                    else:
                        CONTENTS = ' {}'.format(sp.sel_follow(temp_3,a)[i].contents)
                        followbox2.insert(tk.END, CONTENTS)
                else:
                    CONTENTS = ' {}'.format(sp.sel_follow(temp_3,a)[i].contents)
                    followbox2.insert(tk.END, CONTENTS)

            prev_num3 = a
            frame_follow.tkraise()
        else:
            pass

    def FollshowSelnum():
        global maxPage3
        global temp_3
        global prev_num3

        import follow_module as fm

        try:
            if int(no_now3.get()) > int(maxPage3):
                tk.messagebox.showerror(message='게시글 최대 페이지를 초과했습니다.')
                if prev_num3:
                    no_now3.delete(0, tk.END)
                    no_now3.insert(tk.END, prev_num3)
                else:
                    no_now3.delete(0, tk.END)
                    no_now3.insert(tk.END, 1)
                return

            followbox1.delete(0, tk.END)
            followbox2.delete(0, tk.END)
            followbox3.delete(0, tk.END)

            a = int(no_now3.get())

            for i in range(len(sp.sel_follow(temp_3,a))):
                NUM = '{}'.format(sp.sel_follow(temp_3,a)[i].num)
                NICK = ' {}'.format(sp.sel_follow(temp_3,a)[i].nick)
                followbox1.insert(tk.END, NUM)
                followbox3.insert(tk.END, NICK)
                if sp.sel_follow(temp_3,a)[i].secret == 'yes':
                    if fm.followBack(user, sp.sel_follow(temp_3,a)[i]):
                        CONTENTS = '<<<비밀글 입니다.>>>'
                        followbox2.insert(tk.END, CONTENTS)
                    else:
                        CONTENTS = ' {}'.format(sp.sel_follow(temp_3,a)[i].contents)
                        followbox2.insert(tk.END, CONTENTS)
                else:
                    CONTENTS = ' {}'.format(sp.sel_follow(temp_3,a)[i].contents)
                    followbox2.insert(tk.END, CONTENTS)
            prev_num3 = a
        except ValueError:
            tk.messagebox.showerror(message='숫자를 입력해 주세요...')
            if prev_num3:
                no_now3.delete(0, tk.END)
                no_now3.insert(tk.END, prev_num3)
            else:
                no_now3.delete(0, tk.END)
                no_now3.insert(tk.END, 1)
            return

    # 내가 쓴 글 Alt 1
    def postAlt1():
        global maxPage
        global listNum
        global temp_1
        global user
        global openPost
        import like_module as lm
        import comment_module as cm

        def delPost():
            import del_post as dp
            x=messagebox.askyesno(message='정말 삭제하시겠습니까?')
            if x:
                dp.delmyPost(showing)
                openPost.destroy()
                showRecent()
            else:
                openPost.tkraise()

        page_index=listbox2.curselection()[0]
        showing=temp_1[int(listbox1.get(0))//listNum][page_index]

        TIME = time.localtime(float(showing.time))
        TIME = time.strftime('%Y-%m-%d %I:%M:%S %p', TIME)

        openPost = tk.Toplevel(main)
        openPost.geometry('600x400')
        openPost.title('내가 작성한 글')
        openPost.resizable(False,False)

        postFrame1 = tk.Frame(openPost)
        postFrame1.place(x=0, y=0, width=600, height=400)
        postLabel1 = tk.Label(postFrame1, text=showing.contents, bg='white')
        postLabel1.place(x=50, y=50, width=350, height=50)
        postLabel2 = tk.Label(postFrame1, text=TIME, bg='white', anchor='e', state='disabled')
        postLabel2.place(x=50, y=110, width=350, height=25)

        a=lm.cntLike(showing)
        lable1 = tk.Label(postFrame1, text='♥ {}'.format(a))
        lable1.place(x=440, y=110, width=50, height=25)

        btn1 = tk.Button(postFrame1, text='삭제하기',command=delPost)
        btn1.place(x=500, y=110, width=50, height=25)


        # 댓글달기
        cm.Makecomment(user,showing,openPost)

        openPost.mainloop()

    # 남이 작성하고 비밀글 아님 Alt 2-1
    def postAlt2_1():
        global maxPage
        global listNum
        global temp_1
        global user
        global openPost
        import comment_module as cm
        import follow_module as fm
        import like_module as lm

        def btnFollowing():
            fm.followYou(user,showing)
            btn2 = tk.Button(postFrame1, text='언팔로우',command=btnUnfollowing)
            btn2.place(x=510, y=110, width=50, height=25)
            showRecent()

        def btnUnfollowing():
            fm.unfollowYou(user,showing)
            btn2 = tk.Button(postFrame1, text='팔로우',command=btnFollowing)
            btn2.place(x=510, y=110, width=50, height=25)
            showRecent()

        def btnLike():
            lm.likeowYou(user,showing)
            btn1 = tk.Button(postFrame1, text='♥', command=btnUnlike)
            btn1.place(x=440, y=110, width=50, height=25)

        def btnUnlike():
            lm.unlikeYou(user,showing)
            btn1 = tk.Button(postFrame1, text='♡', command=btnLike)
            btn1.place(x=440, y=110, width=50, height=25)

        page_index = listbox2.curselection()[0]
        showing = temp_1[int(listbox1.get(0)) // listNum][page_index]

        TIME = time.localtime(float(showing.time))
        TIME = time.strftime('%Y-%m-%d %I:%M:%S %p', TIME)

        openPost = tk.Toplevel(main)
        openPost.geometry('600x400')
        openPost.title('{}'.format(showing.contents))

        postFrame2 = tk.Frame(openPost, bg='white')
        postFrame2.place(x=0, y=200)

        postFrame1 = tk.Frame(openPost)
        postFrame1.place(x=0, y=0, width=600, height=400)
        postLabel1 = tk.Label(postFrame1, text=showing.contents, bg='white')
        postLabel1.place(x=50, y=50, width=350, height=50)
        postLabel2 = tk.Label(postFrame1, text=TIME, bg='white', anchor='e', state='disabled')
        postLabel2.place(x=50, y=110, width=350, height=25)

        # 좋아요 여부로 버튼 바꾸기
        if lm.checkLike(user,showing):
            btn1 = tk.Button(postFrame1, text='♡', command=btnLike)
            btn1.place(x=440, y=110, width=50, height=25)
        else:
            btn1 = tk.Button(postFrame1, text='♥', command=btnUnlike)
            btn1.place(x=440, y=110, width=50, height=25)

        # 팔로우 여부 확인으로 버튼 바꾸기
        if fm.checkFollow(user,showing):
            btn2 = tk.Button(postFrame1, text='팔로우',command=btnFollowing)
            btn2.place(x=510, y=110, width=50, height=25)
        else:
            btn2 = tk.Button(postFrame1, text='언팔로우',command=btnUnfollowing)
            btn2.place(x=510, y=110, width=50, height=25)

        cm.Makecomment(user,showing,openPost)

        openPost.mainloop()

    # 남이 작성하고 비밀글이고 맞팔 X Alt2-2-1
    def postAlt2_2_1():
        global maxPage
        global listNum
        global temp_1
        global user
        global openPost

        def cc():
            openPost.destroy()

        openPost = tk.Toplevel(main)
        openPost.geometry('600x400')
        openPost.title('맞팔로우해야 볼 수 있습니다.')

        postFrame2 = tk.Frame(openPost, bg='white')
        postFrame2.place(x=0, y=200)

        postFrame1 = tk.Frame(openPost)
        postFrame1.place(x=0, y=0, width=600, height=400)
        postLabel1 = tk.Label(postFrame1, text='맞팔로우 해야 볼 수 있습니다.', bg='white')
        postLabel1.place(x=50, y=50, width=350, height=50)

        btn2 = tk.Button(postFrame1, text='닫기', command=cc)
        btn2.place(x=510, y=110, width=50, height=25)

        openPost.mainloop()

    # 남이 작성하고 비밀글이고 맞팔 0 Alt2-2-2
    def postAlt2_2_2():
        global maxPage
        global listNum
        global temp_1
        global user
        global openPost
        import comment_module as cm
        import follow_module as fm
        import like_module as lm

        def btnUnfollowing():
            fm.unfollowYou(user,showing)
            openPost.destroy()
            showRecent()

        def btnLike():
            lm.likeowYou(user,showing)
            btn1 = tk.Button(postFrame1, text='♥', command=btnUnlike)
            btn1.place(x=440, y=110, width=50, height=25)

        def btnUnlike():
            lm.unlikeYou(user,showing)
            btn1 = tk.Button(postFrame1, text='♡', command=btnLike)
            btn1.place(x=440, y=110, width=50, height=25)

        page_index = listbox2.curselection()[0]
        showing = temp_1[int(listbox1.get(0)) // listNum][page_index]

        TIME = time.localtime(float(showing.time))
        TIME = time.strftime('%Y-%m-%d %I:%M:%S %p', TIME)

        openPost = tk.Toplevel(main)
        openPost.geometry('600x400')
        openPost.title('{}'.format(showing.contents))

        postFrame2 = tk.Frame(openPost, bg='white')
        postFrame2.place(x=0, y=200)

        postFrame1 = tk.Frame(openPost)
        postFrame1.place(x=0, y=0, width=600, height=400)
        postLabel1 = tk.Label(postFrame1, text=showing.contents, bg='white')
        postLabel1.place(x=50, y=50, width=350, height=50)
        postLabel2 = tk.Label(postFrame1, text=TIME, bg='white', anchor='e', state='disabled')
        postLabel2.place(x=50, y=110, width=350, height=25)

        if lm.checkLike(user,showing):
            btn1 = tk.Button(postFrame1, text='♡', command=btnLike)
            btn1.place(x=440, y=110, width=50, height=25)
        else:
            btn1 = tk.Button(postFrame1, text='♥', command=btnUnlike)
            btn1.place(x=440, y=110, width=50, height=25)

        btn2 = tk.Button(postFrame1, text='언팔로우',command=btnUnfollowing)
        btn2.place(x=510, y=110, width=50, height=25)

        cm.Makecomment(user,showing,openPost)

        openPost.mainloop()

    # 최신 게시글 클릭
    def sel_page(event):
        global maxPage
        global listNum
        global temp_1
        global user
        global openPost
        import follow_module as fm

        if openPost:
            openPost.destroy()

        page_index=listbox2.curselection()[0]
        showing=temp_1[int(listbox1.get(0))//listNum][page_index]

        if user.id == showing.ID:
            postAlt1()
        elif showing.secret == 'no':
            postAlt2_1()
        elif fm.followBack(user,showing):
            postAlt2_2_1()
        else:
            postAlt2_2_2()

    # 남이 작성하고 비밀글 아님 Alt 2-1
    def followAlt2_1():
        global maxPage3
        global listNum3
        global temp_3
        global user
        global openPost
        import comment_module as cm
        import follow_module as fm
        import like_module as lm

        def btnUnfollowing():
            fm.unfollowYou(user,showing)
            openPost.destroy()
            showFollow()

        def btnLike():
            lm.likeowYou(user,showing)
            btn1 = tk.Button(postFrame1, text='♥', command=btnUnlike)
            btn1.place(x=440, y=110, width=50, height=25)

        def btnUnlike():
            lm.unlikeYou(user,showing)
            btn1 = tk.Button(postFrame1, text='♡', command=btnLike)
            btn1.place(x=440, y=110, width=50, height=25)

        page_index = followbox2.curselection()[0]
        showing = temp_3[int(followbox1.get(0)) // listNum3][page_index]

        TIME = time.localtime(float(showing.time))
        TIME = time.strftime('%Y-%m-%d %I:%M:%S %p', TIME)

        openPost = tk.Toplevel(main)
        openPost.geometry('600x400')
        openPost.title('{}'.format(showing.contents))

        postFrame2 = tk.Frame(openPost, bg='white')
        postFrame2.place(x=0, y=200)

        postFrame1 = tk.Frame(openPost)
        postFrame1.place(x=0, y=0, width=600, height=400)
        postLabel1 = tk.Label(postFrame1, text=showing.contents, bg='white')
        postLabel1.place(x=50, y=50, width=350, height=50)
        postLabel2 = tk.Label(postFrame1, text=TIME, bg='white', anchor='e', state='disabled')
        postLabel2.place(x=50, y=110, width=350, height=25)

        # 좋아요 여부로 버튼 바꾸기
        if lm.checkLike(user,showing):
            btn1 = tk.Button(postFrame1, text='♡', command=btnLike)
            btn1.place(x=440, y=110, width=50, height=25)
        else:
            btn1 = tk.Button(postFrame1, text='♥', command=btnUnlike)
            btn1.place(x=440, y=110, width=50, height=25)

        # 팔로우 여부 확인으로 버튼 바꾸기
        btn2 = tk.Button(postFrame1, text='언팔로우',command=btnUnfollowing)
        btn2.place(x=510, y=110, width=50, height=25)

        cm.Makecomment(user,showing,openPost)

        openPost.mainloop()

    # 남이 작성하고 비밀글이고 맞팔 X Alt2-2-1
    def followAlt2_2_1():
        global openPost

        def cc():
            openPost.destroy()

        openPost = tk.Toplevel(main)
        openPost.geometry('600x400')
        openPost.title('맞팔로우해야 볼 수 있습니다.')

        postFrame2 = tk.Frame(openPost, bg='white')
        postFrame2.place(x=0, y=200)

        postFrame1 = tk.Frame(openPost)
        postFrame1.place(x=0, y=0, width=600, height=400)
        postLabel1 = tk.Label(postFrame1, text='맞팔로우 해야 볼 수 있습니다.', bg='white')
        postLabel1.place(x=50, y=50, width=350, height=50)

        btn2 = tk.Button(postFrame1, text='닫기', command=cc)
        btn2.place(x=510, y=110, width=50, height=25)

        openPost.mainloop()

    # 남이 작성하고 비밀글이고 맞팔 0 Alt2-2-2
    def followAlt2_2_2():
        global maxPage3
        global listNum3
        global temp_3
        global user
        global openPost
        import comment_module as cm
        import follow_module as fm
        import like_module as lm

        def btnUnfollowing():
            fm.unfollowYou(user,showing)
            openPost.destroy()
            showFollow()

        def btnLike():
            lm.likeowYou(user,showing)
            btn1 = tk.Button(postFrame1, text='♥', command=btnUnlike)
            btn1.place(x=440, y=110, width=50, height=25)

        def btnUnlike():
            lm.unlikeYou(user,showing)
            btn1 = tk.Button(postFrame1, text='♡', command=btnLike)
            btn1.place(x=440, y=110, width=50, height=25)

        page_index = followbox2.curselection()[0]
        showing = temp_3[int(followbox1.get(0)) // listNum3][page_index]

        TIME = time.localtime(float(showing.time))
        TIME = time.strftime('%Y-%m-%d %I:%M:%S %p', TIME)

        openPost = tk.Toplevel(main)
        openPost.geometry('600x400')
        openPost.title('{}'.format(showing.contents))

        postFrame2 = tk.Frame(openPost, bg='white')
        postFrame2.place(x=0, y=200)

        postFrame1 = tk.Frame(openPost)
        postFrame1.place(x=0, y=0, width=600, height=400)
        postLabel1 = tk.Label(postFrame1, text=showing.contents, bg='white')
        postLabel1.place(x=50, y=50, width=350, height=50)
        postLabel2 = tk.Label(postFrame1, text=TIME, bg='white', anchor='e', state='disabled')
        postLabel2.place(x=50, y=110, width=350, height=25)

        if lm.checkLike(user,showing):
            btn1 = tk.Button(postFrame1, text='♡', command=btnLike)
            btn1.place(x=440, y=110, width=50, height=25)
        else:
            btn1 = tk.Button(postFrame1, text='♥', command=btnUnlike)
            btn1.place(x=440, y=110, width=50, height=25)

        btn2 = tk.Button(postFrame1, text='언팔로우',command=btnUnfollowing)
        btn2.place(x=510, y=110, width=50, height=25)

        openPost.mainloop()

    # 팔로잉 게시글 클릭
    def selFollowing(event):
        global maxPage3
        global listNum3
        global temp_3
        global user
        global openPost
        import follow_module as fm

        if openPost:
            openPost.destroy()

        page_index=followbox2.curselection()[0]
        showing=temp_3[int(followbox1.get(0))//listNum][page_index]

        if showing.secret == 'no':
            followAlt2_1()
        elif fm.followBack(user,showing):
            followAlt2_2_1()
        else:
            followAlt2_2_2()

    # Mypage에서 글 작성
    def refresh(event):
        global user
        import posting_test as pt
        global prev_num2
        global maxPage2

        prev_num2=1
        your_secret=tk.messagebox.askquestion('비밀이야?','비밀글로 작성하나요?')
        a = texting.get()

        pt.pt(user.id,a,your_secret,user.n_name)

        texting.delete(0, tk.END)
        texting.insert(tk.END, '오늘은 어떤 생각을 하셨나요?')
        no_now2.delete(0,tk.END)
        no_now2.insert(tk.END,1)
        changeFrame2()

    # refresh와 같은 기능
    def refresh2():
        global user
        import posting_test as pt
        global prev_num2
        global maxPage2
        prev_num2=1

        your_secret=tk.messagebox.askquestion('비밀이야?','비밀글로 작성하나요?')
        a = texting.get()

        pt.pt(user.id,a,your_secret,user.n_name)

        texting.delete(0, tk.END)
        texting.insert(tk.END, '오늘은 어떤 생각을 하셨나요?')
        no_now2.delete(0,tk.END)
        no_now2.insert(tk.END,1)
        changeFrame2()

    def Mypost():
        global user
        global prev_num2
        global maxPage2
        global temp_2
        global listNum2

        prev_num2=1

        myListbox_num.delete(0, tk.END)
        myListbox.delete(0,tk.END)
        myListbox_day.delete(0, tk.END)
        listNum2 = 10
        if sp.search_someone(user):
            maxPage2 = sp.show_page(sp.class_list(sp.search_someone(user)), listNum2)[1]
            temp_2 = sp.show_page(sp.class_list(sp.search_someone(user)), listNum2)[2]

            for i in range(len(sp.show_page(sp.class_list(sp.search_someone(user)),listNum2)[0])):
                NUM='{}'.format(sp.show_page(sp.class_list(sp.search_someone(user)),listNum2)[0][i].num)
                CONTENTS = ' {}'.format(sp.show_page(sp.class_list(sp.search_someone(user)), listNum2)[0][i].contents)
                NICK=' {}'.format(sp.show_page(sp.class_list(sp.search_someone(user)),listNum2)[0][i].nick)
                myListbox_num.insert(tk.END,NUM)
                myListbox.insert(tk.END, CONTENTS)
                myListbox_day.insert(tk.END,NICK)
        else:
            myListbox.insert(tk.END,'작성한 게시글이 없습니다.')
            maxPage2 = 1

    # 내가 쓴 글 Alt 1
    def mypostAlt1(event):
        global maxPage2
        global listNum2
        global temp_2
        global user
        global openPost
        import comment_module as cm
        import like_module as lm

        def delPost():
            import del_post as dp
            x=messagebox.askyesno(message='정말 삭제하시겠습니까?')
            if x:
                dp.delmyPost(showing)
                openPost.destroy()
                changeFrame2()
            else:
                openPost.tkraise()

        if openPost:
            openPost.destroy()

        page_index=myListbox.curselection()[0]
        showing=temp_2[int(myListbox_num.get(0))//listNum2][page_index]

        TIME = time.localtime(float(showing.time))
        TIME = time.strftime('%Y-%m-%d %I:%M:%S %p', TIME)

        openPost = tk.Toplevel(main)
        openPost.geometry('600x400')
        openPost.title('내가 작성한 글')

        postFrame2 = tk.Frame(openPost, bg='white')
        postFrame2.place(x=0, y=200)

        postFrame1 = tk.Frame(openPost)
        postFrame1.place(x=0, y=0, width=600, height=400)
        postLabel1 = tk.Label(postFrame1, text=showing.contents, bg='white')
        postLabel1.place(x=50, y=50, width=350, height=50)
        postLabel2 = tk.Label(postFrame1, text=TIME, bg='white', anchor='e', state='disabled')
        postLabel2.place(x=50, y=110, width=350, height=25)

        a=lm.cntLike(showing)
        lable1 = tk.Label(postFrame1, text='♥ {}'.format(a))
        lable1.place(x=440, y=110, width=50, height=25)

        btn1 = tk.Button(postFrame1, text='삭제하기',command=delPost)
        btn1.place(x=510, y=110, width=50, height=25)

        cm.Makecomment(user,showing,openPost)

        openPost.mainloop()

    def MyshowSelnum():
        global maxPage2
        global temp_2
        global prev_num2
        global openPost

        try:
            if int(no_now2.get()) > int(maxPage2):
                tk.messagebox.showerror(message='게시글 최대 페이지를 초과했습니다.')
                if prev_num2:
                    no_now2.delete(0, tk.END)
                    no_now2.insert(tk.END, prev_num2)
                else:
                    no_now2.delete(0, tk.END)
                    no_now2.insert(tk.END, 1)
                return

            myListbox_num.delete(0, tk.END)
            myListbox.delete(0,tk.END)
            myListbox_day.delete(0, tk.END)

            a=int(no_now2.get())
            b=int(maxPage2)

            for i in range(len(sp.sel_others(a,b)[0])):
                NUM='{}'.format(sp.sel_others(a,b)[0][i].num)
                CONTENTS = ' {}'.format(sp.sel_others(a,b)[0][i].contents)
                NICK=' {}'.format(sp.sel_others(a,b)[0][i].nick)
                myListbox_num.insert(tk.END,NUM)
                myListbox.insert(tk.END, CONTENTS)
                myListbox_day.insert(tk.END,NICK)

            prev_num2=a
        except ValueError:
            tk.messagebox.showerror(message='숫자를 입력해 주세요...')
            if prev_num2:
                no_now2.delete(0,tk.END)
                no_now2.insert(tk.END,prev_num2)
            else:
                no_now2.delete(0,tk.END)
                no_now2.insert(tk.END,1)
            return

    # 1쪽 보기
    def MyshowRecent():
        no_now2.delete(0, tk.END)
        no_now2.insert(tk.END, '1')
        Mypost()
        frame_myPage.tkraise()

    # 마지막 쪽 보기
    def MyshowLast():
        global maxPage2
        global prev_num2

        if maxPage2 != 1:
            no_now2.delete(0, tk.END)
            no_now2.insert(tk.END, maxPage2)

            myListbox_num.delete(0, tk.END)
            myListbox.delete(0, tk.END)
            myListbox_day.delete(0, tk.END)

            a = int(maxPage2)
            b = int(maxPage2)

            for i in range(len(sp.sel_others(a, b)[0])):
                NUM = '{}'.format(sp.sel_others(a, b)[0][i].num)
                CONTENTS = ' {}'.format(sp.sel_others(a, b)[0][i].contents)
                NICK = ' {}'.format(sp.sel_others(a, b)[0][i].nick)
                myListbox_num.insert(tk.END, NUM)
                myListbox.insert(tk.END, CONTENTS)
                myListbox_day.insert(tk.END, NICK)

            prev_num2 = a
            frame_myPage.tkraise()
        else:
            pass

    def MyshowSel(event):
        MyshowSelnum()
        frame_myPage.tkraise()

    def MyshowPrev():
        global prev_num2
        try:
            a = int(no_now2.get())
            if a != 1:
                prev_num2 = a - 1
                no_now2.delete(0, tk.END)
                no_now2.insert(tk.END, a - 1)
                MyshowSelnum()
                frame_myPage.tkraise()
        except ValueError:
            a = prev_num2
            if a != 1:
                prev_num2 = a - 1
                no_now2.delete(0, tk.END)
                no_now2.insert(tk.END, a - 1)
                MyshowSelnum()
                frame_myPage.tkraise()

    def MyshowNext():
        global maxPage2
        global prev_num2
        try:
            a = int(no_now2.get())
            if a != maxPage2:
                prev_num2 = a + 1
                no_now2.delete(0, tk.END)
                no_now2.insert(tk.END, a + 1)
                MyshowSelnum()
                frame_myPage.tkraise()

        except ValueError:
            a = prev_num2
            if a != maxPage2:
                prev_num2 = a + 1
                no_now2.delete(0, tk.END)
                no_now2.insert(tk.END, a + 1)
                MyshowSelnum()
                frame_myPage.tkraise()

    # 검색하기 버튼
    def searchPost():
        global keyList

        def searchKey():
            global keyList
            import search_post as sp

            a= searchEnt.get()
            if sp.search_keyword(a):
                searchWin.destroy()
                keyList=sp.search_keyword(a)
                showSearch()
            else:
                messagebox.showerror(message='검색어에 해당하는 글이 없습니다.')
                searchWin.tkraise()

        searchWin=tk.Toplevel(main)
        searchWin.geometry('350x150')
        searchWin.resizable(False,False)

        searchEnt=tk.Entry(searchWin)
        searchEnt.place(x=50,y=50,width=250)

        searchBtn1=tk.Button(searchWin, text='검색하기', command=searchKey)
        searchBtn1.place(x=73,y=90,width=75)
        searchBtn2=tk.Button(searchWin, text='닫기', command=searchWin.destroy)
        searchBtn2.place(x=190,y=90,width=75)

    def showSearch():
        no_now4.delete(0,tk.END)
        no_now4.insert(tk.END,'1')
        showSearchAll()
        no_last4.configure(text='/ {}'.format(maxPage4))
        frame_search.tkraise()

    # 검색된 리스트 출력
    def showSearchAll():
        global keyList
        global maxPage4
        global listNum4
        global temp_4
        global user

        import follow_module as fm


        searchbox1.delete(0, tk.END)
        searchbox2.delete(0,tk.END)
        searchbox3.delete(0, tk.END)
        listNum4 = 20
        if keyList:
            maxPage4=sp.show_page(sp.class_list(keyList),listNum)[1]
            temp_4=sp.show_page(sp.class_list(keyList),listNum)[2]

            for i in range(len(sp.show_page(sp.class_list(keyList),listNum)[0])):
                NUM='{}'.format(sp.show_page(sp.class_list(keyList),listNum)[0][i].num)
                NICK=' {}'.format(sp.show_page(sp.class_list(keyList),listNum)[0][i].nick)
                searchbox1.insert(tk.END,NUM)
                searchbox3.insert(tk.END,NICK)
                if sp.show_page(sp.class_list(keyList), listNum)[0][i].secret == 'yes':
                    if fm.followBack(user,sp.show_page(sp.class_list(keyList), listNum)[0][i]):
                        CONTENTS = '<<<비밀글 입니다.>>>'
                        searchbox2.insert(tk.END, CONTENTS)
                    else:
                        CONTENTS = ' {}'.format(sp.show_page(sp.class_list(keyList), listNum)[0][i].contents)
                        searchbox2.insert(tk.END, CONTENTS)
                else:
                    CONTENTS = ' {}'.format(sp.show_page(sp.class_list(keyList), listNum)[0][i].contents)
                    searchbox2.insert(tk.END, CONTENTS)

        else:
            searchbox2.insert(tk.END,'작성한 게시글이 없습니다.')
            maxPage4 = 1
            pass

    # 내가 쓴 글 Alt 1
    def searchAlt1():
        global maxPage4
        global listNum4
        global temp_4
        global user
        global openPost

        import like_module as lm

        def delPost():
            import del_post as dp
            x=messagebox.askyesno(message='정말 삭제하시겠습니까?')
            if x:
                dp.delmyPost(showing)
                openPost.destroy()
                showSearch()
            else:
                openPost.tkraise()

        page_index=searchbox2.curselection()[0]
        showing=temp_1[int(searchbox1.get(0))//listNum4][page_index]

        TIME = time.localtime(float(showing.time))
        TIME = time.strftime('%Y-%m-%d %I:%M:%S %p', TIME)

        openPost = tk.Toplevel(main)
        openPost.geometry('600x400')
        openPost.title('내가 작성한 글')

        postFrame2 = tk.Frame(openPost, bg='white')
        postFrame2.place(x=0, y=200)

        postFrame1 = tk.Frame(openPost)
        postFrame1.place(x=0, y=0, width=600, height=400)
        postLabel1 = tk.Label(postFrame1, text=showing.contents, bg='white')
        postLabel1.place(x=50, y=50, width=350, height=50)
        postLabel2 = tk.Label(postFrame1, text=TIME, bg='white', anchor='e', state='disabled')
        postLabel2.place(x=50, y=110, width=350, height=25)

        a=lm.cntLike(showing)
        lable1 = tk.Label(postFrame1, text='♥ {}'.format(a))
        lable1.place(x=440, y=110, width=50, height=25)

        btn1 = tk.Button(postFrame1, text='삭제하기',command=delPost)
        btn1.place(x=510, y=110, width=50, height=25)

        openPost.mainloop()

    # 남이 작성하고 비밀글 아님 Alt 2-1
    def searchAlt2_1():
        global maxPage4
        global listNum4
        global temp_4
        global user
        global openPost
        import comment_module as cm
        import follow_module as fm
        import like_module as lm

        def btnFollowing():
            fm.followYou(user,showing)
            btn2 = tk.Button(postFrame1, text='언팔로우',command=btnUnfollowing)
            btn2.place(x=510, y=110, width=50, height=25)
            showSearch()

        def btnUnfollowing():
            fm.unfollowYou(user,showing)
            btn2 = tk.Button(postFrame1, text='팔로우',command=btnFollowing)
            btn2.place(x=510, y=110, width=50, height=25)
            showSearch()

        def btnLike():
            lm.likeowYou(user,showing)
            btn1 = tk.Button(postFrame1, text='♥', command=btnUnlike)
            btn1.place(x=440, y=110, width=50, height=25)

        def btnUnlike():
            lm.unlikeYou(user,showing)
            btn1 = tk.Button(postFrame1, text='♡', command=btnLike)
            btn1.place(x=440, y=110, width=50, height=25)

        page_index = searchbox2.curselection()[0]
        showing = temp_4[int(searchbox1.get(0)) // listNum4][page_index]

        TIME = time.localtime(float(showing.time))
        TIME = time.strftime('%Y-%m-%d %I:%M:%S %p', TIME)

        openPost = tk.Toplevel(main)
        openPost.geometry('600x400')
        openPost.title('{}'.format(showing.contents))

        postFrame2 = tk.Frame(openPost, bg='white')
        postFrame2.place(x=0, y=200)

        postFrame1 = tk.Frame(openPost)
        postFrame1.place(x=0, y=0, width=600, height=400)
        postLabel1 = tk.Label(postFrame1, text=showing.contents, bg='white')
        postLabel1.place(x=50, y=50, width=350, height=50)
        postLabel2 = tk.Label(postFrame1, text=TIME, bg='white', anchor='e', state='disabled')
        postLabel2.place(x=50, y=110, width=350, height=25)

        # 좋아요 여부로 버튼 바꾸기
        if lm.checkLike(user,showing):
            btn1 = tk.Button(postFrame1, text='♡', command=btnLike)
            btn1.place(x=440, y=110, width=50, height=25)
        else:
            btn1 = tk.Button(postFrame1, text='♥', command=btnUnlike)
            btn1.place(x=440, y=110, width=50, height=25)

        # 팔로우 여부 확인으로 버튼 바꾸기
        if fm.checkFollow(user,showing):
            btn2 = tk.Button(postFrame1, text='팔로우',command=btnFollowing)
            btn2.place(x=510, y=110, width=50, height=25)
        else:
            btn2 = tk.Button(postFrame1, text='언팔로우',command=btnUnfollowing)
            btn2.place(x=510, y=110, width=50, height=25)

        cm.Makecomment(user,showing,openPost)

        openPost.mainloop()

    # 남이 작성하고 비밀글이고 맞팔 X Alt2-2-1
    def searchAlt2_2_1():
        global maxPage4
        global listNum4
        global temp_4
        global user
        global openPost

        def cc():
            openPost.destroy()

        openPost = tk.Toplevel(main)
        openPost.geometry('600x400')
        openPost.title('맞팔로우해야 볼 수 있습니다.')

        postFrame2 = tk.Frame(openPost, bg='white')
        postFrame2.place(x=0, y=200)

        postFrame1 = tk.Frame(openPost)
        postFrame1.place(x=0, y=0, width=600, height=400)
        postLabel1 = tk.Label(postFrame1, text='맞팔로우 해야 볼 수 있습니다.', bg='white')
        postLabel1.place(x=50, y=50, width=350, height=50)

        btn2 = tk.Button(postFrame1, text='닫기', command=cc)
        btn2.place(x=510, y=110, width=50, height=25)

        openPost.mainloop()

    # 남이 작성하고 비밀글이고 맞팔 0 Alt2-2-2
    def searchAlt2_2_2():
        global maxPage4
        global listNum4
        global temp_4
        global user
        global openPost
        import comment_module as cm
        import follow_module as fm
        import like_module as lm

        def btnUnfollowing():
            fm.unfollowYou(user,showing)
            openPost.destroy()
            showSearch()

        def btnLike():
            lm.likeowYou(user,showing)
            btn1 = tk.Button(postFrame1, text='♥', command=btnUnlike)
            btn1.place(x=440, y=110, width=50, height=25)

        def btnUnlike():
            lm.unlikeYou(user,showing)
            btn1 = tk.Button(postFrame1, text='♡', command=btnLike)
            btn1.place(x=440, y=110, width=50, height=25)

        page_index = searchbox2.curselection()[0]
        showing = temp_1[int(searchbox1.get(0)) // listNum4][page_index]

        TIME = time.localtime(float(showing.time))
        TIME = time.strftime('%Y-%m-%d %I:%M:%S %p', TIME)

        openPost = tk.Toplevel(main)
        openPost.geometry('600x400')
        openPost.title('{}'.format(showing.contents))

        postFrame2 = tk.Frame(openPost, bg='white')
        postFrame2.place(x=0, y=200)

        postFrame1 = tk.Frame(openPost)
        postFrame1.place(x=0, y=0, width=600, height=400)
        postLabel1 = tk.Label(postFrame1, text=showing.contents, bg='white')
        postLabel1.place(x=50, y=50, width=350, height=50)
        postLabel2 = tk.Label(postFrame1, text=TIME, bg='white', anchor='e', state='disabled')
        postLabel2.place(x=50, y=110, width=350, height=25)

        if lm.checkLike(user,showing):
            btn1 = tk.Button(postFrame1, text='♡', command=btnLike)
            btn1.place(x=440, y=110, width=50, height=25)
        else:
            btn1 = tk.Button(postFrame1, text='♥', command=btnUnlike)
            btn1.place(x=440, y=110, width=50, height=25)

        btn2 = tk.Button(postFrame1, text='언팔로우',command=btnUnfollowing)
        btn2.place(x=510, y=110, width=50, height=25)

        cm.Makecomment(user,showing,openPost)

        openPost.mainloop()

    # 게시물 클릭
    def selSearch(event):
        global maxPage4
        global listNum4
        global temp_4
        global user
        global openPost
        import follow_module as fm

        if openPost:
            openPost.destroy()

        page_index = searchbox2.curselection()[0]
        showing = temp_4[int(listbox1.get(0)) // listNum4][page_index]

        if user.id == showing.ID:
            searchAlt1()
        elif showing.secret == 'no':
            searchAlt2_1()
        elif fm.followBack(user, showing):
            searchAlt2_2_1()
        else:
            searchAlt2_2_2()

    # 마지막 쪽 보기
    def searchLast():
        global maxPage4
        global prev_num4
        global temp_4
        global user

        import follow_module as fm
        if maxPage4 != 1:
            no_now4.delete(0,tk.END)
            no_now4.insert(tk.END,maxPage4)

            searchbox1.delete(0, tk.END)
            searchbox2.delete(0, tk.END)
            searchbox3.delete(0, tk.END)

            a = int(maxPage4)


            for i in range(len(sp.sel_follow(temp_4, a))):
                NUM = '{}'.format(sp.sel_follow(temp_4, a)[i].num)
                NICK = ' {}'.format(sp.sel_follow(temp_4, a)[i].nick)
                searchbox1.insert(tk.END, NUM)
                searchbox3.insert(tk.END, NICK)
                if user.id ==  sp.sel_follow(temp_4, a)[i].ID:
                    CONTENTS = ' {}'.format(sp.sel_follow(temp_4, a)[i].contents)
                    searchbox2.insert(tk.END, CONTENTS)
                elif sp.sel_follow(temp_4, a)[i].secret == 'yes':
                    if fm.followBack(user,sp.sel_follow(temp_4, a)[i]):
                        CONTENTS = '<<<비밀글 입니다.>>>'
                        searchbox2.insert(tk.END, CONTENTS)
                    else:
                        CONTENTS = ' {}'.format(sp.sel_follow(temp_4, a)[i].contents)
                        searchbox2.insert(tk.END, CONTENTS)
                else:
                    CONTENTS = ' {}'.format(sp.sel_follow(temp_4, a)[i].contents)
                    searchbox2.insert(tk.END, CONTENTS)

            prev_num4 = a
            frame_search.tkraise()
        else:
            pass

    # 쪽수 검색하기
    def searchSelnum():
        global maxPage4
        global temp_4
        global prev_num4

        import follow_module as fm

        try:
            if int(no_now4.get()) > int(maxPage4):
                tk.messagebox.showerror(message='게시글 최대 페이지를 초과했습니다.')
                if prev_num4:
                    no_now4.delete(0, tk.END)
                    no_now4.insert(tk.END, prev_num4)
                else:
                    no_now4.delete(0, tk.END)
                    no_now4.insert(tk.END, 1)
                return

            searchbox1.delete(0, tk.END)
            searchbox2.delete(0,tk.END)
            searchbox3.delete(0, tk.END)

            a=int(no_now4.get())

            for i in range(len(sp.sel_follow(temp_4,a))):
                NUM='{}'.format(sp.sel_follow(temp_4,a)[i].num)
                NICK=' {}'.format(sp.sel_follow(temp_4,a)[i].nick)
                searchbox1.insert(tk.END,NUM)
                searchbox3.insert(tk.END,NICK)
                if user.id ==  sp.sel_follow(temp_4,a)[i].ID:
                    CONTENTS = ' {}'.format(sp.sel_follow(temp_4,a)[i].contents)
                    searchbox2.insert(tk.END, CONTENTS)
                elif sp.sel_follow(temp_4,a)[i].secret == 'yes':
                    if fm.followBack(user,sp.sel_follow(temp_4,a)[i]):
                        CONTENTS = '<<<비밀글 입니다.>>>'
                        searchbox2.insert(tk.END, CONTENTS)
                    else:
                        CONTENTS = ' {}'.format(sp.sel_follow(temp_4,a)[i].contents)
                        searchbox2.insert(tk.END, CONTENTS)
                else:
                    CONTENTS = ' {}'.format(sp.sel_follow(temp_4,a)[i].contents)
                    searchbox2.insert(tk.END, CONTENTS)
            prev_num4=a
        except ValueError:
            tk.messagebox.showerror(message='숫자를 입력해 주세요...')
            if prev_num4:
                no_now4.delete(0,tk.END)
                no_now4.insert(tk.END,prev_num4)
            else:
                no_now4.delete(0,tk.END)
                no_now4.insert(tk.END,1)
            return

    # 쪽수 검색하기
    def searchSel(event):
        searchSelnum()
        frame_search.tkraise()

    # 이전 쪽 보기
    def searchPrev():
        global prev_num4
        try:
            a=int(no_now4.get())
            if a != 1:
                prev_num4 = a - 1
                no_now4.delete(0,tk.END)
                no_now4.insert(tk.END,a-1)
                showSelnum()
                frame_list.tkraise()

        except ValueError:
            a = prev_num4
            if a != 1:
                prev_num4 = a - 1
                no_now4.delete(0, tk.END)
                no_now4.insert(tk.END, a - 1)
                searchSelnum()
                frame_search.tkraise()

    # 다음 쪽 보기
    def searchNext():
        global maxPage4
        global prev_num4
        try:
            a=int(no_now.get())
            if a != maxPage4:
                prev_num4 = a + 1
                no_now4.delete(0,tk.END)
                no_now4.insert(tk.END,a+1)
                searchSelnum()
                frame_search.tkraise()
        except ValueError:
            a = prev_num4
            if a != maxPage4:
                prev_num4 = a + 1
                no_now4.delete(0, tk.END)
                no_now4.insert(tk.END, a + 1)
                searchSelnum()
                frame_follow.tkraise()

    main = tk.Tk()
    main.title('FACE_BAND')  # 창의 타이틀 명
    main.geometry('800x600')  # 창의 사이즈
    main.resizable(False, False)  # 창 사이즈 변경 여부 속성 지정

    # 메뉴바 설정
    menubar=tk.Menu(main)

    myPage = tk.Menu(menubar,tearoff=0)
    myPage.add_command(label='HOME', command=changeFrame1)
    myPage.add_separator()
    myPage.add_command(label='내 페이지',command=changeFrame2)
    myPage.add_command(label='개인정보 수정하기', command=myData)
    myPage.add_separator()
    myPage.add_command(label='로그아웃',command=log_out)
    myPage.add_separator()
    myPage.add_command(label='종료하기',command=EXIT)
    menubar.add_cascade(label='MyPage',menu=myPage)

    COMMUNITY = tk.Menu(menubar,tearoff=0)
    COMMUNITY.add_command(label='최신글 보기',command=showRecent)
    COMMUNITY.add_command(label='인기글 보기',command=showCeleb)
    COMMUNITY.add_command(label='팔로우 게시물 보기', command=showFollow)
    menubar.add_cascade(label='COMMUNITY',menu=COMMUNITY)

    onedayLife = tk.Menu(menubar,tearoff=0)
    onedayLife.add_command(label='지렁이게임',command=showGame)
    menubar.add_cascade(label='게임하기',menu=onedayLife)

    main.config(menu=menubar)

    # 이미지
    home_icon1=Image.open('home_icon1.png')
    wpercent = (35 / float(home_icon1.size[0]))
    hsize = int((float(home_icon1.size[1]) * float(wpercent)))
    home_icon1 = home_icon1.resize((35, hsize))
    home_icon=ImageTk.PhotoImage(home_icon1)
    mypage_icon1=Image.open('Mypage_icon.png')
    mypage_icon1 = mypage_icon1.resize((90, 35))
    mypage_icon=ImageTk.PhotoImage(mypage_icon1)
    community_icon1=Image.open('Community_icon.png')
    community_icon1 = community_icon1.resize((120, 35))
    community_icon=ImageTk.PhotoImage(community_icon1)
    game_icon1=Image.open('Game_icon.png')
    game_icon1 = game_icon1.resize((60, 35))
    game_icon=ImageTk.PhotoImage(game_icon1)
    mypage_back1=Image.open('mypage_back.png')
    mypage_back1 = mypage_back1.resize((800, 600))
    mypage_back=ImageTk.PhotoImage(mypage_back1)
    posting_icon1=Image.open('posting_icon.png')
    posting_icon1 = posting_icon1.resize((80, 29))
    posting_icon=ImageTk.PhotoImage(posting_icon1)
    edit_icon1=Image.open('Edit_icon.png')
    edit_icon1 = edit_icon1.resize((110, 27))
    edit_icon=ImageTk.PhotoImage(edit_icon1)
    logout_icon1=Image.open('logout_icon.png')
    logout_icon1 = logout_icon1.resize((80, 27))
    logout_icon=ImageTk.PhotoImage(logout_icon1)
    exit_icon1=Image.open('EXIT.png')
    exit_icon1 = exit_icon1.resize((50, 23))
    exit_icon=ImageTk.PhotoImage(exit_icon1)
    icon1=Image.open('icon1.png')
    icon1 = icon1.resize((25, 20))
    icon1=ImageTk.PhotoImage(icon1)
    icon2=Image.open('icon2.png')
    icon2 = icon2.resize((14, 20))
    icon2=ImageTk.PhotoImage(icon2)
    icon3=Image.open('icon3.png')
    icon3 = icon3.resize((14, 20))
    icon3=ImageTk.PhotoImage(icon3)
    icon4=Image.open('icon4.png')
    icon4 = icon4.resize((25, 20))
    icon4=ImageTk.PhotoImage(icon4)
    recent_back1=Image.open('recent_back.png')
    recent_back1 = recent_back1.resize((800, 600))
    recent_back=ImageTk.PhotoImage(recent_back1)
    follow_back1=Image.open('follow_back.jpg')
    follow_back1 = follow_back1.resize((800, 600))
    follow_back=ImageTk.PhotoImage(follow_back1)
    celeb_back1=Image.open('celeb_back.jpg')
    celeb_back1 = celeb_back1.resize((800, 600))
    celeb_back=ImageTk.PhotoImage(celeb_back1)
    top_icon1=Image.open('topicon.png')
    top_icon1 = top_icon1.resize((75, 28))
    top_icon=ImageTk.PhotoImage(top_icon1)
    follow_icon1=Image.open('followingicon.png')
    follow_icon1 = follow_icon1.resize((75, 28))
    follow_icon=ImageTk.PhotoImage(follow_icon1)
    search_icon1=Image.open('searchicon.png')
    search_icon1 = search_icon1.resize((65, 28))
    search_icon=ImageTk.PhotoImage(search_icon1)
    top_icon2=Image.open('topicon2.png')
    top_icon2 = top_icon2.resize((65, 28))
    top_icon2=ImageTk.PhotoImage(top_icon2)
    community_icon2=Image.open('communityicon2.png')
    community_icon2 = community_icon2.resize((90, 28))
    community_icon2=ImageTk.PhotoImage(community_icon2)
    community_icon3=Image.open('communityicon1.png')
    community_icon3 = community_icon3.resize((90, 28))
    community_icon3=ImageTk.PhotoImage(community_icon3)
    follow_icon2=Image.open('followingicon2.png')
    follow_icon2 = follow_icon2.resize((75, 28))
    follow_icon2=ImageTk.PhotoImage(follow_icon2)
    back_icon=Image.open('backicon.png')
    back_icon = back_icon.resize((45, 28))
    back_icon=ImageTk.PhotoImage(back_icon)

    # 최신글보기
    frame_list=tk.Frame(main,bd=2)
    frame_list.place(x=0,y=0,width=800, height=600)
    # 폰트
    font_list = tkfont.Font(family='Consolas', size=12)
    # 배경화면
    back_label=tk.Label(frame_list,image=recent_back)
    back_label.place(x=0,y=0,width=800,height=600)
    # 숫자
    listbox1=tk.Listbox(frame_list,relief='flat',bg='#f7d5d9')
    listbox1.bindtags((listbox1,main,'all'))
    listbox1.place(x=125,y=50,height=410,width=25)
    listbox1.config(font=font_list)
    # 내용
    listbox2=tk.Listbox(frame_list,relief='flat',bg='#f7d5d9')
    listbox2.place(x=155,y=50,height=410,width=390)
    listbox2.bind('<Double-Button-1>', sel_page)
    listbox2.config(font=font_list)
    # 닉네임
    listbox3=tk.Listbox(frame_list,relief='flat',bg='#f7d5d9')
    listbox3.bindtags((listbox3, main, 'all'))
    listbox3.place(x=550,y=50,height=410,width=130)
    listbox3.config(font=font_list)
    # 버튼
    toHome = tk.Button(frame_list, image=home_icon, command=changeFrame1, bg='#ab93c9',relief='flat')
    toHome.place(x=390, y=10, width=35, height=35)
    toCel = tk.Button(frame_list, image=top_icon ,command=showCeleb, bg='#0a2830',relief='flat')
    toCel.place(x=500, y=468, width=75, height=28)
    toFol = tk.Button(frame_list, image=follow_icon, command=showFollow, bg='#05141a',relief='flat')
    toFol.place(x=600, y=468, width=75, height=28)
    searchBtn = tk.Button(frame_list, image=search_icon, command=searchPost ,bg='#0a2830',relief='flat')
    searchBtn.place(x=125, y=468, width=65,height=28)
    showRecentAll()
    #쪽 수 (맨 앞 페이지 가기, 앞 페이지, 현재 페이지, 뒷 페이지, 맨 뒷 페이지)
    no_1=tk.Button(frame_list,text='<<',command=showRecent2)
    no_previous = tk.Button(frame_list, text='<',command=showPrev)
    no_now = tk.Entry(frame_list)
    no_now.insert(tk.END,'1')
    no_now.bind('<Return>',showSel)
    no_last = tk.Label(frame_list,text='/ {}'.format(maxPage), anchor='w', state='disabled')
    no_next = tk.Button(frame_list, text='>',command=showNext)
    no_100 = tk.Button(frame_list, text='>>',command=showLast)
    no_1.place(x=250,y=468,width=25)
    no_previous.place(x=280,y=468,width=20)
    no_now.place(x=315,y=472,width=45)
    no_last.place(x=362,y=470,width=50)
    no_next.place(x=420,y=468,width=20)
    no_100.place(x=450,y=468,width=25)

    # 검색글보기1
    frame_search=tk.Frame(main,bd=2)
    frame_search.place(x=0,y=0,width=800, height=600)
    # 폰트
    font_list = tkfont.Font(family='Consolas', size=12)
    # 배경화면
    back_label=tk.Label(frame_search,image=recent_back)
    back_label.place(x=0,y=0,width=800,height=600)
    # 숫자
    searchbox1=tk.Listbox(frame_search)
    searchbox1.bindtags((searchbox1,main,'all'))
    searchbox1.place(x=125,y=50,height=410,width=25)
    searchbox1.config(font=font_list)
    # 내용
    searchbox2=tk.Listbox(frame_search)
    searchbox2.place(x=155,y=50,height=410,width=390)
    searchbox2.bind('<Double-Button-1>', selSearch)
    searchbox2.config(font=font_list)
    # 닉네임
    searchbox3=tk.Listbox(frame_search)
    searchbox3.bindtags((searchbox3, main, 'all'))
    searchbox3.place(x=550,y=50,height=410,width=130)
    searchbox3.config(font=font_list)
    # 버튼
    toHome = tk.Button(frame_search, image=home_icon, command=changeFrame1, bg='white',relief='flat')
    toHome.place(x=390, y=10, width=35, height=35)
    toCel = tk.Button(frame_search, image=top_icon,command=showCeleb, bg='#0a2830',relief='flat')
    toCel.place(x=500, y=468, width=75, height=28)
    toFol = tk.Button(frame_search, image=follow_icon, command=showFollow, bg='#05141a',relief='flat')
    toFol.place(x=600, y=468, width=75, height=28)
    searchBtn = tk.Button(frame_search, image=back_icon, command=showRecent, bg='#0a2830',relief='flat')
    searchBtn.place(x=125, y=468, width=45, height=28)
    showSearchAll()
    #쪽 수 (맨 앞 페이지 가기, 앞 페이지, 현재 페이지, 뒷 페이지, 맨 뒷 페이지)
    no_4=tk.Button(frame_search,text='<<',command=showSearch)
    no_previous4 = tk.Button(frame_search, text='<',command=searchPrev)
    no_now4 = tk.Entry(frame_search)
    no_now4.insert(tk.END,'1')
    no_now4.bind('<Return>',searchSel)
    no_last4 = tk.Label(frame_search,text='/ {}'.format(maxPage4), anchor='w', state='disabled')
    no_next4 = tk.Button(frame_search, text='>',command=searchNext)
    no_1004 = tk.Button(frame_search, text='>>',command=searchLast)
    no_4.place(x=250,y=468,width=25)
    no_previous4.place(x=280,y=468,width=20)
    no_now4.place(x=315,y=472,width=45)
    no_last4.place(x=362,y=470,width=50)
    no_next4.place(x=420,y=468,width=20)
    no_1004.place(x=450,y=468,width=25)

    # 인기글 프레임
    frame_celeb=tk.Frame(main,bg='white',bd=2)
    frame_celeb.place(x=0,y=0,width=800, height=600)
    my_oneday=tk.Label(frame_celeb,text='인기글 보기')
    my_oneday.place(x=0,y=0)
    # 배경화면
    back_label=tk.Label(frame_celeb,image=celeb_back)
    back_label.place(x=0,y=0,width=800,height=600)
    # 숫자
    celebbox1=tk.Listbox(frame_celeb,relief='flat',bg='#48737c')
    celebbox1.bindtags((celebbox1,main,'all'))
    celebbox1.place(x=125,y=50,height=410,width=25)
    celebbox1.config(font=font_list)
    # 내용
    celebbox2=tk.Listbox(frame_celeb, relief='flat',bg='#48737c')
    celebbox2.place(x=155,y=50,height=410,width=390)
    celebbox2.bind('<Double-Button-1>', selCeleb)
    celebbox2.config(font=font_list)
    # 닉네임
    celebbox3=tk.Listbox(frame_celeb, relief='flat',bg='#48737c')
    celebbox3.bindtags((celebbox3, main, 'all'))
    celebbox3.place(x=550,y=50,height=410,width=130)
    celebbox3.config(font=font_list)
    # 버튼
    toHome = tk.Button(frame_celeb, image=home_icon, command=changeFrame1, bg='#3f3b5c',relief='flat')
    toHome.place(x=390, y=10, width=35, height=35)
    toCel = tk.Button(frame_celeb, image=community_icon3,command=showRecent,bg='#f8e3c8',relief='flat')
    toCel.place(x=485, y=468, width=90, height=28)
    toFol = tk.Button(frame_celeb, image=follow_icon2,command=showFollow,bg='#f8e3c8',relief='flat')
    toFol.place(x=600, y=468, width=75, height=28)

    # 팔로우 게시물 보기
    frame_follow=tk.Frame(main,bg='white',bd=2)
    frame_follow.place(x=0,y=0,width=800, height=600)
    my_oneday=tk.Label(frame_follow,text='팔로우 게시물 보기')
    my_oneday.place(x=0,y=0)
    # 배경화면
    back_label=tk.Label(frame_follow,image=follow_back)
    back_label.place(x=0,y=0,width=800,height=600)
    # 숫자
    followbox1=tk.Listbox(frame_follow)
    followbox1.bindtags((followbox1,main,'all'))
    followbox1.place(x=125,y=50,height=410,width=25)
    followbox1.config(font=font_list)
    # 내용
    followbox2=tk.Listbox(frame_follow)
    followbox2.place(x=155,y=50,height=410,width=390)
    followbox2.bind('<Double-Button-1>', selFollowing)
    followbox2.config(font=font_list)
    # 닉네임
    followbox3=tk.Listbox(frame_follow)
    followbox3.bindtags((followbox3, main, 'all'))
    followbox3.place(x=550,y=50,height=410,width=130)
    followbox3.config(font=font_list)
    # 버튼
    toHome = tk.Button(frame_follow, image=home_icon, command=changeFrame1, bg='#363930',relief='flat')
    toHome.place(x=390, y=10, width=35, height=35)
    toCel = tk.Button(frame_follow, image=top_icon2, command=showCeleb,bg='#5d6754',relief='flat')
    toCel.place(x=500, y=472, width=65, height=28)
    toFol = tk.Button(frame_follow, image=community_icon2, command=showRecent,bg='#2e3028',relief='flat')
    toFol.place(x=585, y=468, width=90, height=28)
    showFollowAll()
    #쪽 수 (맨 앞 페이지 가기, 앞 페이지, 현재 페이지, 뒷 페이지, 맨 뒷 페이지)
    no_3=tk.Button(frame_follow,text='<<',command=showFollow)
    no_previous3 = tk.Button(frame_follow, text='<',command=showfollPrev)
    no_now3 = tk.Entry(frame_follow)
    no_now3.insert(tk.END,'1')
    no_now3.bind('<Return>',showfollSel)
    no_last3 = tk.Label(frame_follow,text='/ {}'.format(maxPage), anchor='w', state='disabled')
    no_next3 = tk.Button(frame_follow, text='>',command=showfollNext)
    no_1003 = tk.Button(frame_follow, text='>>',command=showfollLast)
    no_3.place(x=250,y=468,width=25)
    no_previous3.place(x=280,y=468,width=20)
    no_now3.place(x=315,y=472,width=45)
    no_last3.place(x=362,y=470,width=50)
    no_next3.place(x=420,y=468,width=20)
    no_1003.place(x=450,y=468,width=25)

    # 내 페이지
    frame_myPage=tk.Frame(main,bd=2,bg='#fcb7a2')
    frame_myPage.place(x=0,y=0,width=800, height=600)
    #배경
    background=tk.Label(frame_myPage,image=mypage_back)
    background.place(x=0,y=0,width=800,height=600)
    # 글 작성하기
    texting=tk.Entry(frame_myPage,bg='#ffc591')
    texting.insert(tk.END,'오늘은 어떤 생각을 하셨나요?')
    texting.bind('<Return>',refresh)
    texting.place(x=35,y=500,width=300)
    #리스트박스
    myListbox=tk.Listbox(frame_myPage,bg='#ffc591',relief='flat')
    myListbox.place(x=420, y=275,width=300,height=170)
    myListbox.bind('<Double-Button-1>',mypostAlt1)
    myListbox_num=tk.Listbox(frame_myPage)
    myListbox_num.bindtags((myListbox_num, main, 'all'))
    myListbox_num.place(x=800, y=600,width=50,height=170)
    myListbox_day=tk.Listbox(frame_myPage)
    myListbox_day.bindtags((myListbox_day, main, 'all'))
    myListbox_day.place(x=800, y=600,width=100,height=170)
    # 버튼
    toHome = tk.Button(frame_myPage, image=home_icon, command=changeFrame1, bg='#ffaa88',relief='flat')
    toHome.place(x=390, y=10, width=35, height=35)
    postbtn=tk.Button(frame_myPage,image=posting_icon,command=refresh2,bg='#641464',relief='flat')
    postbtn.place(x=35,y=535,width=80,height=30)
    mod_PS=tk.Button(frame_myPage,image=edit_icon, command=myData,bg='#cc0444',relief='flat')
    mod_PS.place(x=420,y=535,width=110,height=27)
    tk.Button(frame_myPage, image=logout_icon, command=log_out,bg='#cc0444',relief='flat').place(x=555, y=535, width=80,height=27)
    tk.Button(frame_myPage, image=exit_icon, command=EXIT,bg='#cc0444',relief='flat').place(x=660, y=535, width=50,height=23)
    Mypost()
    #쪽 수 (맨 앞 페이지 가기, 앞 페이지, 현재 페이지, 뒷 페이지, 맨 뒷 페이지)
    no_12=tk.Button(frame_myPage,image=icon1,bg='#cc0444',relief='flat',command=MyshowRecent)
    no_previous2 = tk.Button(frame_myPage, image=icon2,bg='#cc0444',relief='flat',command=MyshowPrev)
    no_now2 = tk.Entry(frame_myPage,bg='#cc0444',relief='flat')
    no_now2.insert(tk.END,'1')
    no_now2.bind('<Return>',MyshowSel)
    no_last2 = tk.Label(frame_myPage,text='/ {}'.format(maxPage2), anchor='w', state='disabled')
    no_next2 = tk.Button(frame_myPage,image=icon3,bg='#cc0444',relief='flat',command=MyshowNext)
    no_1002 = tk.Button(frame_myPage,image=icon4,bg='#cc0444',relief='flat',command=MyshowLast)
    no_12.place(x=450,y=460,width=25,height=20)
    no_previous2.place(x=495,y=460,width=14,height=20)
    no_now2.place(x=520,y=462,width=45)
    no_last2.place(x=570,y=460,width=50)
    no_next2.place(x=630,y=460,width=14,height=20)
    no_1002.place(x=665,y=460,width=25,height=20)

    # 기본 화면
    frame_showing1=tk.Frame(main,bd=2,bg='#021418')
    frame_showing1.place(x=0,y=0,width=800, height=600)
    font_home=tkfont.Font(family='맑은 고딕',size=12)
    # 메인 GIF 이미지
    class ImageLabel(tk.Label):
        def load(self, im):
            if isinstance(im, str):
                im = Image.open(im)
            self.loc = 0
            self.frames = []
            try:
                for i in count(1):
                    self.frames.append(ImageTk.PhotoImage(im.copy().resize((800, 500))))
                    im.seek(i)
            except EOFError:
                pass
            try:
                self.delay = im.info['duration']
            except:
                self.delay = 100

            if len(self.frames) == 1:
                self.config(image=self.frames[0])
            else:
                self.next_frame()

        def unload(self):
            self.config(image="")
            self.frames = None

        def next_frame(self):
            if self.frames:
                self.loc += 1
                self.loc %= len(self.frames)
                self.config(image=self.frames[self.loc])
                self.after(self.delay, self.next_frame)
    mainLabel=tk.Label(frame_showing1,bg='#021418',relief="flat")
    lbl = ImageLabel(mainLabel)
    lbl.pack()
    lbl.load('MAIN.gif')
    mainLabel.place(x=0,y=0,width=800,height=500)
    # 버튼
    toMe = tk.Button(frame_showing1,image=mypage_icon,font=font_home, command=changeFrame2,relief='flat',bg='#021418')
    toMe.place(x=135, y=520, width=90, height=35)
    toRecnet = tk.Button(frame_showing1, image=community_icon,font=font_home, command=showRecent,relief='flat',bg='#021418')
    toRecnet.place(x=340, y=520, width=120, height=35)
    toOneday = tk.Button(frame_showing1, image=game_icon,font=font_home, command=showGame,relief='flat',bg='#021418')
    toOneday.place(x=600, y=520, width=60, height=35)
    main.mainloop()

def game_re_make():
    global user
    import tkinter as tk
    import tkinter.font as font
    import numpy as np
    from tkinter import messagebox
    import MVP_class as vp
    import time
    from PIL import Image, ImageTk
    from itertools import count
    class ImageLabel2(tk.Label):
        """a label that displays images, and plays them if they are gifs"""

        def load(self, im):
            if isinstance(im, str):
                im = Image.open(im)
            self.loc = 0
            self.frames = []

            try:
                for i in count(1):
                    self.frames.append(ImageTk.PhotoImage(im.copy().resize((800, 470))))
                    im.seek(i)
            except EOFError:
                pass

            try:
                self.delay = im.info['duration']
            except:
                self.delay = 100

            if len(self.frames) == 1:
                self.config(image=self.frames[0])
            else:
                self.next_frame()

        def unload(self):
            self.config(image="")
            self.frames = None

        def next_frame(self):
            if self.frames:
                self.loc += 1
                self.loc %= len(self.frames)
                self.config(image=self.frames[self.loc])
                self.after(self.delay, self.next_frame)

    x = 0
    x2 = 0

    root = tk.Tk()
    root.title("지렁이 Game")
    root.geometry("800x600")
    root.resizable(False, False)
    font=tk.font.Font(size=13)

    # 함수 정의

    # 1.mvp관련 함수
    def num_mvp():
        aa = vp.mvp_cut()[:20]
        temp_str = ''
        for i in range(len(aa)):
            temp_str += ' {}\n'.format(i + 1)
        mvp_count2 = tk.Label(img_mvp, text=temp_str, anchor='n',font=font)
        mvp_count2.place(x=240, y=150, height=350, width=80)

    def live_time():
        aa = vp.mvp_cut()[:20]
        temp_list1 = ''
        for i in range(len(aa)):
            time_get = round(float(aa[i][2]),5)

            temp_list1 += '  {}\n'.format(time_get)
        mvp_listbox2 = tk.Label(img_mvp, text=temp_list1, anchor='n',font=font)
        mvp_listbox2.place(x=320, y=150, height=350, width=80)

    def nick():
        def letFight(index):
            opponent=aa[index]
            x2_go1=float(opponent[2])
            x2_go2=650/x2_go1
            x2_go3 = x2_go2* 0.2
            def bind_game(a,b,what_bg):
                global x
                global x2
                where = a
                num = b
                def vs_earth_worm(event):
                    global x
                    global x2
                    x = 0
                    x2 = 0
                    now = time.time()
                    root.unbind("<space>")
                    def space_click(event):
                        global x
                        if x >= 650:
                            root.unbind("<KeyRelease>")
                            tt = tk.messagebox.showinfo(message='이겨버렸다. 너무 시시해서 죽고싶어졌다.')
                            finish = time.time()
                            finish_time = finish - now
                            global user
                            return
                        else:
                            x = x + num
                        return x
                    def img():
                        global x
                        global x2
                        rn = np.random.randint(2)
                        label1 = tk.Label(where, image=listImage[rn],bg=what_bg)
                        label1.place(x=x, y=550)

                        if x2 >= 650 > x:
                            tt = tk.messagebox.showinfo(message='졌다.')
                            return
                        elif x >= 650:
                            label1.destroy()
                        label1.after(100, img)
                        label1.after(100, label1.destroy)
                    def img2():
                        global x2
                        rn2 = np.random.randint(2)
                        label2 = tk.Label(where, image=listImage[rn2],bg=what_bg)
                        label2.place(x=x2, y=470)
                        label2.after(200, img2)
                        label2.after(200, label2.destroy)
                        x2 += x2_go3

                    tm = time.time()
                    image1 = Image.open('image1.png')
                    image1 = ImageTk.PhotoImage(image1.resize((150, 50)))
                    image2 = Image.open('image2.png')
                    image2 = ImageTk.PhotoImage(image2.resize((150, 50)))
                    listImage = [image1, image2]
                    root.bind("<KeyRelease>", space_click)
                    img()
                    img2()
                    if x2 >= 650:
                        label1.destroy()
                root.bind("<space>", vs_earth_worm)
            def random_show():
                ephemera = ['맑은', '비']
                sNumbers = np.random.choice(ephemera, 1, p=[0.75, 0.25])
                tm_now = time.time()
                if sNumbers == '맑은':
                    show_sun()
                    bind_game(img_sun, 3,"#05131c")

                elif sNumbers == '비':
                    show_rainy()
                    bind_game(img_rain, 5,"#17100c")
            random_show()

        aa = vp.mvp_cut()[:20]
        temp_list3 = ''
        x_place = 580
        y_place=152
        for i in range(len(aa)):
            temp_list3 += '  {}\n'.format(vp.listbox_insert()[i][1])
            mvp_listbox6 = tk.Label(img_mvp, text=temp_list3,anchor='n',font=font)
            mvp_listbox6.place(x=480, y=150, height=350, width=100)
            globals()["vs_btn{}".format(i)]=tk.Button(img_mvp,text='VS', command= lambda c=i : letFight(c))
            eval('vs_btn'+str(i)).place(x=x_place,y=y_place,height=15, width=27)
            y_place+=17

    def mvp_list():
        num_mvp()
        live_time()
        nick()

    def fram_rainy():
        lbl1 = ImageLabel2(img_rain)
        lbl1.pack()
        lbl1.load('개도둑5.gif')
        img_rain.place(x=0, y=0, width=800, height=600)
        back_label = tk.Label(img_rain, bg="#17100c")
        back_label.place(x=0, y=440, width=800, height=160)

    def frame_sun():
        lbl = ImageLabel2(img_sun)
        lbl.pack()
        lbl.load('game2.gif')
        img_sun.place(x=0, y=0, width=800, height=600)
        back_label = tk.Label(img_sun, bg="#05131c")
        back_label.place(x=0, y=470, width=800, height=130)

    def showMVP():
        mvp_list()
        img_mvp.tkraise()

    # 2.게임관련 함수
    def show_sun():
        img_sun.tkraise()
        sun_text_label = tk.Label(img_sun, text="75%확률 맑은 프레임")
        sun_text_label.place(x=300, y=15, width=130, height=50)
        sun_text_label.after(1500, sun_text_label.destroy)

    def show_rainy():
        img_rain.tkraise()
        sun_text_label = tk.Label(img_rain, text="25%확률 비오는 프레임")
        sun_text_label.place(x=300, y=15, width=130, height=50)
        sun_text_label.after(1500, sun_text_label.destroy)

    def random_show():
        global user
        text_coin()
        ephemera=['맑은','비']
        sNumbers = np.random.choice(ephemera,1,p=[0.75,0.25])
        tm_now = time.time()
        if sNumbers=='맑은'and int(user.coin)>=1:
            show_sun()
            bind_game(img_sun,3,"#05131c")

        elif sNumbers=='비'and int(user.coin)>=1:
            show_rainy()
            bind_game(img_rain,5,"#17100c")

    def show_main():
        main_img.tkraise()

    def bind_game(a,b,what_bg):
        where=a
        num=b
        def earth_worm(event):
            global x
            start_time=time.time()
            text_coin()
            x = 0
            now = time.time()
            root.unbind("<space>")
            def space_click(event):
                global x
                if x >= 650:
                    end_time=time.time()
                    root.unbind("<KeyRelease>")
                    tt = tk.messagebox.showinfo(message='%f'%(end_time-start_time))
                    finish_time = end_time-start_time
                    global user
                    text = open('MVP.txt', 'a', encoding='utf-8')
                    text.write(user.id + '\t' + user.n_name + '\t' + str(finish_time) + '\n')
                    text.close()
                    return
                else:
                    x = x + num
                return x

            def img():
                global x
                global x2
                rn = np.random.randint(2)
                label1 = tk.Label(where, image=listImage[rn], bg=what_bg)
                label1.place(x=x, y=550)

                if x >= 650:
                    label1.destroy()
                label1.after(200, img)
                label1.after(200, label1.destroy)



            tm = time.time()
            image1=Image.open('image1.png')
            image1 = ImageTk.PhotoImage(image1.resize((150,50)))
            image2=Image.open('image2.png')
            image2 = ImageTk.PhotoImage(image2.resize((150,50)))
            listImage = [image1, image2]
            root.bind("<KeyRelease>", space_click)
            img()
        root.bind("<space>", earth_worm)

    def text_coin():
        global user
        text=open('user.txt','r',encoding='utf-8')
        texts=text.readlines()
        use_time=str(time.time())
        text.close()
        user_list=[]
        for i in texts:
            user_list.append(i.replace('\n','').split('\t'))
        user.coin=str(int(user.coin)-1)
        text_write=open('user.txt','w',encoding='utf-8')
        for i in range(len(user_list)):
            if user.id==user_list[i][0]:
                user_list[i][7]=user.coin
            text_write.write(user_list[i][0]+'\t'+user_list[i][1]+'\t'+user_list[i][2]+'\t'+user_list[i][3]+'\t'+user_list[i][4]+'\t'+user_list[i][5]+'\t'+user_list[i][6]+'\t'+user_list[i][7]+'\n')
        text_write.close()
        text_coin_use = open('onedaylife_coin_use.txt', 'a', encoding='utf-8')
        text_coin_use.write(user.id + '\t' + user.n_name + '\t' + str(use_time) + '\n')
        text_coin_use.close()
    # 3.mylife관련 함수

    def user_coin_list():
        usecoin = tk.Listbox(img_mylife)
        usecoin.yview()
        usecoin.place(x=240, y=190, height=200, width=300)
        user_list = vp.txt_check_user(user)
        temp_str_space = ' ' * 7
        count_all=0
        temp_list4 = ''
        for i in range(len(user_list)): #234 -  -   0
            for j in range(len(user_list[i][1:])):
                if user_list[i][1]!='-':
                    count_all+=5
                    time_get = time.localtime(float(user_list[i][1]))
                    time_set = time.strftime('%y-%m-%d %H:%M', time_get)
                    temp_list4 += '  {}\n'.format(user_list[i][0]+temp_str_space+'포스팅'+temp_str_space+time_set+temp_str_space+str(count_all)+('(+5)'))
                    usecoin.insert(0, temp_list4)
                    temp_list4 = ''
                elif user_list[i][2]!='-':
                    count_all+=3
                    time_get = time.localtime(float(user_list[i][2]))
                    time_set = time.strftime('%y-%m-%d %H:%M', time_get)
                    temp_list4 += '  {}\n'.format(user_list[i][0]+temp_str_space+'로그인'+temp_str_space+time_set+temp_str_space+str(count_all)+('(+3)'))
                    usecoin.insert(0, temp_list4)
                    temp_list4 = ''
                elif user_list[i][3] != '-':
                    count_all+=4
                    time_get = time.localtime(float(user_list[i][3]))
                    time_set = time.strftime('%y-%m-%d %H:%M', time_get)
                    temp_list4 += '  {}\n'.format(user_list[i][0]+temp_str_space+'인기글'+temp_str_space+time_set+temp_str_space+str(count_all)+('(+4)'))
                    usecoin.insert(0, temp_list4)
                    temp_list4 = ''
                btn4 = tk.Button(img_mylife, text='획\n득\n내\n역', command=mylife_new)
                btn4.place(x=210, y=190, width=30, height=70)
                img_mylife.tkraise()

    def mylife_new():
        mylife_listbox1 = tk.Listbox(img_mylife)
        mylife_listbox1.yview()
        mylife_listbox1.place(x=240, y=190, height=200, width=300)
        user_list = vp.coin_use(user)
        temp_str_space = ' ' * 10
        temp_list4 = ''
        count_num=0
        for i in range(len(user_list)):
            count_num+=1
            time_get = time.localtime(float(user_list[i][2]))
            time_set = time.strftime('%y-%m-%d %H:%M', time_get)
            temp_list4 += '  {}\n'.format(
                time_set + temp_str_space + user_list[i][1] + temp_str_space +str(count_num))
            mylife_listbox1.insert(0, temp_list4)
            temp_list4 = ''
            img_mylife.tkraise()

        mylife_label2 = tk.Label(img_mylife, text=str(len(user_list)))
        mylife_label2.place(x=280, y=140, height=20, width=30)
        mylife_coinuse_label = tk.Label(img_mylife, text='코인 사용량')
        mylife_coinuse_label.place(x=260, y=115, height=20, width=80)

        btn4 = tk.Button(img_mylife, text='사\n용\n내\n역', command=user_coin_list)
        btn4.place(x=210, y=190, width=30, height=70)

    def show_mylife():
        mylife_new()
        img_mylife.tkraise()

    def returnMain():
        global game
        game = 'no'
        root.destroy()

    # 마이라이프 프레임
    img_mylife=tk.Frame(root)
    img_mylife.place(x=0, y=0, width=800, height=600)

    mylife_btn1 = tk.Button(img_mylife, text="랜덤 화면전환", command=random_show)
    mylife_btn1.place(x=720, y=15, width=50, height=50)
    mylife_btn2 = tk.Button(img_mylife, text="main", command=show_main)
    mylife_btn2.place(x=670, y=15, width=50, height=50)
    mylife_btn3 = tk.Button(img_mylife, text="MVP", command=showMVP)
    mylife_btn3.place(x=620, y=15, width=50, height=50)


    # 맑은 프레임
    img_sun = tk.Frame(root)
    img_sun.place(x=0, y=0, width=800, height=600)
    frame_sun()

    sun_btn1 = tk.Button(img_sun, text="랜덤 화면 전환", command=random_show)
    sun_btn1.place(x=720, y=15, width=50, height=50)
    sun_btn2 = tk.Button(img_sun, text="main", command=show_main)
    sun_btn2.place(x=670, y=15, width=50, height=50)
    sun_btn3 = tk.Button(img_sun, text="MVP", command=showMVP)
    sun_btn3.place(x=620, y=15, width=50, height=50)
    sun_btn4 = tk.Button(img_sun, text="mylife", command=show_mylife)
    sun_btn4.place(x=570, y=15, width=50, height=50)

    # 비오는 프레임
    img_rain = tk.Frame(root)
    img_rain.place(x=0, y=0, width=800, height=600)
    fram_rainy()

    rain_btn1 = tk.Button(img_rain, text="랜덤 화면전환", command=random_show)
    rain_btn1.place(x=720, y=15, width=50, height=50)
    rain_btn2 = tk.Button(img_rain, text="main", command=show_main)
    rain_btn2.place(x=670, y=15, width=50, height=50)
    rain_btn3 = tk.Button(img_rain, text="MVP", command=showMVP)
    rain_btn3.place(x=620, y=15, width=50, height=50)
    rain_btn4 = tk.Button(img_rain, text="mylife", command=show_mylife)
    rain_btn4.place(x=570, y=15, width=50, height=50)

    # mvp 프레임
    img_mvp = tk.Frame(root)
    img_mvp.place(x=0, y=0, width=800, height=600)

    mvp_btn1 = tk.Button(img_mvp, text="랜덤 화면전환", command=random_show)
    mvp_btn1.place(x=720, y=15, width=50, height=50)
    mvp_btn2 = tk.Button(img_mvp, text="main", command=show_main)
    mvp_btn2.place(x=670, y=15, width=50, height=50)
    mvp_btn4 = tk.Button(img_mvp, text="mylife", command=show_mylife)
    mvp_btn4.place(x=620, y=15, width=50, height=50)

    # 메인 프레임
    main_img = tk.Frame(root)
    main_img.place(x=0, y=0, width=800, height=600)

    main_btn1 = tk.Button(main_img, text="랜덤 화면전환", command=random_show)
    main_btn1.place(x=720, y=15, width=50, height=50)
    main_btn2 = tk.Button(main_img, text="main", command=show_main)
    main_btn2.place(x=670, y=15, width=50, height=50)
    main_btn3 = tk.Button(main_img, text="MVP", command=showMVP)
    main_btn3.place(x=620, y=15, width=50, height=50)
    main_btn4 = tk.Button(main_img, text="mylife", command=show_mylife)
    main_btn4.place(x=570, y=15, width=50, height=50)
    main_btn5 = tk.Button(main_img, text="돌아가기", command=returnMain)
    main_btn5.place(x=520, y=15, width=50, height=50)
    main_btn6 = tk.Button(main_img, text="종료하기", command=root.destroy)
    main_btn6.place(x=470, y=15, width=50, height=50)


    root.mainloop()


on=True
while on:
    user = ''
    openPost=''
    keyList=''
    mydata=''
    game=''
    on=False
    maxPage=1
    maxPage2=1
    maxPage3=1
    maxPage4=1
    prev_num=0
    prev_num2=0
    prev_num3=0
    prev_num4=0
    login_gui()
    while user:
        main_gui()
        if user=='no':
            on = True
            break
        elif game=='yes':
            game_re_make()
            if user=='no':
                on = True
                break
            elif game=='no':
                continue
            else:
                on = False
                break
        else:
            on=False
            break
