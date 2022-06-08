from tkinter import *
import tkinter as tk
import tkinter.ttk
import os
from collections import Counter
import mecrosel_mod2 as mcs2

window = Tk()

window.title("매크로 ")

#################################################

notebook = tkinter.ttk.Notebook(window, width=800, height=500)
notebook.pack()

# tab1 = tkinter.Frame(window)
# notebook.add(tab1, text=" 파일 ")
# tab2 = tkinter.Frame(window)
# notebook.add(tab2, text="시작")
# tab3 = tkinter.Frame(window)
# notebook.add(tab3, text="    ???    ")

tab1 = tkinter.Frame(window)

tab2 = tkinter.Frame(window)
#################################################
def donothing():
    filewin = Toplevel(window)
    window.title("nothing ")
    button = Button(filewin, text="Do nothing button")
    button.pack()

def keyboard():
    win = Tk()
    win.title('3조 매크로')
    ICON = PhotoImage(file="molecule.png")
    win.iconphoto(True, ICON)
    win.geometry("640x478")  # 창의 사이즈
    win.resizable(False, False)  # 창의 사이즈 변경 여부 속성 지정\
    key1 = Toplevel(window)
    key1.title("키보드")
    # button = Button(filewin, text="키보드키를 입력 ")
    # button.pack()
    w1 = Label(key1, text="enter입력")
    w1.pack()
    insutxt1 = Entry(key1)
    insutxt1.pack()



#로그인
loglist = []

mcs2.inpelement()

# def login():
#     if not os.path.isfile("회원정보.txt") == True:
#         gk.signin()
#     ID = entryID.get()
#     PW = entryPW.get()
#     ULIST = open('회원정보.txt', 'r', encoding="utf-8")
#     ULIST = ULIST.readlines()
#     del ULIST[0]
#     for i in range(len(ULIST)):
#         ULIST[i] = ULIST[i].replace('\n', '')
#         ULIST[i] = ULIST[i].split('\t')
#     logdic = {}
#     for i in range(len(ULIST)):
#         IDkey = ULIST[i][0]
#         PWvalue = ULIST[i][1]
#         NNvalue = ULIST[i][4]
#         trustValue = ULIST[i][5]
#         logdic[IDkey] = [PWvalue, NNvalue, trustValue]
#     IDlist = []
#     for i in range(len(ULIST)):
#         IDlist.append(ULIST[i][0])
#     if ID == '':
#         messagebox.showinfo('로그인 실패', '아이디를 입력해주세요.')
#     elif ID not in IDlist:
#         messagebox.showinfo('로그인 실패', '존재하지 않는 아이디입니다.')
#     elif PW == '':
#         messagebox.showinfo('로그인 실패', '비밀번호를 입력해주세요.')
#     elif logdic.get(ID)[0] != PW:
#         messagebox.showinfo('로그인 실패', '비밀번호를 잘못 입력하였습니다.')
#     elif logdic.get(ID)[0] == PW:
#         global loglist
#         loglist.append(logdic.get(ID)[1])
#         loglist.append(logdic.get(ID)[2])
#         loglist.append(ID)
#         loglist.append(PW)
#         messagebox.showinfo('로그인 성공', '로그인 성공!')
#         mainPop()
#         return loglist
#



menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="새매크로", command=donothing)
filemenu.add_command(label="매크로 저장", command=donothing)
filemenu.add_command(label="매크로 불러오기", command=donothing)
# filemenu.add_separator()
filemenu.add_command(label="끝", command=window.quit)
menubar.add_cascade(label="파일", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="실행", command=donothing)
helpmenu.add_command(label="중지", command=donothing)
menubar.add_cascade(label="시작", menu=helpmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="키보드설정", command=keyboard)
helpmenu.add_command(label="마우스설정", command=donothing)
helpmenu.add_command(label="기타설정", command=donothing)
menubar.add_cascade(label="설정", menu=helpmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About macro", command=donothing)
menubar.add_cascade(label="정보", menu=helpmenu)

###################################################

def closing(event):
    window.destroy()
    os.system('C:\\gom\\python gom_gui.py')


lb_hi = Label(tab2, text="Reboot", bg='gray19', fg='gray60', width=10, height=3)
lb_hi.bind('<Button-1>', closing)
lb_hi.place(x=10, y=10)

entry = tk.Entry(tab2, fg="gray19", bg="snow", width=20)
blog = 'blog.naver.com/xenostep'
entry.insert(0, blog)
entry.place(x=10, y=80)

entry1 = tk.Entry(tab2, fg="gray19", bg="snow", width=20)
entry1.insert(0, entry.get().split("/")[1])
entry1.place(x=10, y=100)


def cus():
    cus_list = []
    with open('C:\\gom\\gom.txt') as cus:
        for line in cus:
            cus_list.append(line)

    cus_list = cus_list[2:]

    for i in range(len(cus_list)):
        cus_all.insert(INSERT, cus_list[i])
    cus_all1.insert(INSERT, '\n' + Counter(cus_list).most_common(1)[0][0])


def clear():
    cus_all.delete(0.0, 10.0)
    cus_all1.delete(0.0, 3.0)


cus_all = tk.Text(tab2, width=20, height=10)
cus_all.place(x=200, y=100)
cus_all1 = tk.Text(tab2, width=20, height=3)
cus_all1.place(x=400, y=100)

load_bt = tk.Button(tab2, text='Load', bg='gray19', fg='snow', width=10, command=cus)
load_bt.place(x=300, y=400)
clear_bt = tk.Button(tab2, text='Clear', bg='royalblue', fg='snow', width=7, command=clear)
clear_bt.place(x=385, y=400)
save_bt = tk.Button(tab2, text='Save', bg='gray19', fg='snow', width=10)
save_bt.place(x=450, y=400)
lb_hi = Label(tab2, text="->", fg='gray19')
lb_hi.place(x=360, y=110)


def new_win(event):
    nw = Tk()
    nw.title("Select video")

    def closer(event):
        nw.destroy()

    nw.bind("<Escape>", closer)

    nw.geometry('300x300+300+100')
    nw.mainloop()


def scaled(event):
    img_lb.configure(image=img_big)
    img_lb.place(x=330, y=270)


def Re(event):
    img_lb.config(image=img)
    img_lb.place(x=360, y=300)


WDIR = "D://pycharm//jsm//eunlecture//220517//mecrosel"
img_name = "home.png"
img_name_s = "home_scale.png"

image_path = os.path.join(WDIR, img_name)
image_s_path = os.path.join(WDIR, img_name_s)

img = PhotoImage(file=image_s_path)
img_big = PhotoImage(file=image_path)
img_lb = tk.Label(tab2, image=img)
img_lb.bind("<Button-1>", new_win)
img_lb.bind("<Enter>", scaled)
img_lb.bind("<Leave>", Re)
img_lb.place(x=360, y=300)

window.config(menu=menubar)
window.geometry('500x400+300+100')
window.mainloop()