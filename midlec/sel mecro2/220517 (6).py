import tkinter as tk
from tkinter import *
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import mecrosel_mod2 as mm2

import time as t
c=0
listB=''
win = Tk()
win.title('매크로 프로그램')

win.geometry("700x435") #창의 사이즈
win.resizable(True,True) #창의 사이즈 변경 여부 속성 지정\
entry= tk.Entry(win)  #엔트리 값설정 place pack gid가능
framefirst=Frame(win)
framefirst.pack()
framesecond=Frame(win)
framesecond.pack()
framethr=Frame(win)
framethr.pack()
frame4=Frame(win)
frame4.pack()



#키보드 이벤트, 마우스 이벤트, 요소찾기 이벤트, url 가져오기 이벤트, 지우기 이벤트, (크롬드라이버 변경)
def InputURLpage():
    global pro
    global txt1
    pro = Toplevel(win)
    pro.title("URL 입력창")  # 창의 타이틀명
    pro.geometry("500x100")  # 창의 사이즈
    frame2 = tk.Frame(pro)
    frame2.pack()


    lbl2 = Label(frame2, text="URL입력")
    lbl2.grid(row=1, column=0)
    txt1 = Entry(frame2)
    txt1.grid(row=1, column=1)
    txt1.bind("<Return>", txt1.get())
    btn = Button(frame2, text="OK", width=15, command=OKURL)
    btn.grid(row=2, column=1)
    pro.mainloop()
    win.mainloop()
def OKURL():
    listbox.insert(0, "1.URL : %s" % txt1.get())
    pro.withdraw()

def InputElement():
    global pro2
    global txt2
    global answer1
    global c
    pro2 = Toplevel(win)
    pro2.title("요소값 입력창")  # 창의 타이틀명
    pro2.geometry("500x300")  # 창의 사이즈
    answer1 = tk.IntVar()
    Rad1 = tk.Radiobutton(pro2, text="class_name", variable=answer1, value=0)
    Rad1.grid(row=0, column=1, sticky="w")
    Rad2 = tk.Radiobutton(pro2, text="xpath", variable=answer1, value=1)
    Rad2.grid(row=1, column=1, sticky="w")
    Rad3 = tk.Radiobutton(pro2, text="id", variable=answer1, value=2)
    Rad3.grid(row=2, column=1, sticky="w")
    txt2 = Entry(pro2)
    txt2.grid(row=3, column=1)
    txt2.bind("<Return>", txt2.get())
    def ADDElement():
        global c
        c=c+1
        listbox2.insert(c, "2.PATH값 : %s" % txt2.get())
    def DELElement():
        global c
        c= c-1
        listbox2.delete(END)

    def ADELElement():
        global c
        c=0
        listbox2.delete(0,END)

    def LCELElement():
        global listB
        global c
        listB=(listbox2.get(0,END))
        print(len(listB))
        for i in range(len(listB)):
            listbox.insert(1+i, (listbox2.get(i)))
        # print(listB)
        c = 0
        pro2.destroy()

    btntax = tk.Button(pro2, text="추가하기", command=ADDElement)
    btntax.grid(row=4, column=1)
    btntax = tk.Button(pro2, text="삭제하기", command=DELElement)
    btntax.grid(row=5, column=1)
    btntax = tk.Button(pro2, text="전체삭제", command=ADELElement)
    btntax.grid(row=6, column=1)
    btntax = tk.Button(pro2, text="완료", command=LCELElement)
    btntax.grid(row=6, column=3)
    lbl2 = Label(pro2, text="요소리스트")
    lbl2.grid(row=2, column=7)
    listbox2 = Listbox(pro2, selectmode='extended', height=5, width=30)
    listbox2.grid(row=3, column=7)
    pro2.mainloop()
    win.mainloop()
def ResultEle():
    if answer1.get() == 0:
        return driver.find_element(By.CLASS_NAME, txt2.get())
    elif answer1.get() == 1:
        return driver.find_element(By.XPATH, txt2.get())
    elif answer1.get() == 2:
        return driver.find_element(By.ID, txt2.get())
# def OKElement():
#     listbox.insert(END, "2.요소값 : %s" % txt2.get())
#     pro2.withdraw()
# def COMElement():
#     print(listB)
#     # listbox.delete(1) txt2.get()
#     listbox.insert(1, "2.PATH값 : %s" % listB)



def InputSearch():
    global pro3
    global txtsearch
    global txtsearchpath
    pro3 = Toplevel(win)
    pro3.title("검색 기능")  # 창의 타이틀명
    pro3.geometry("500x300")  # 창의 사이즈

    lbl1 = Label(pro3, text="검색창 PATH값")
    lbl1.grid(row=0, column=0)
    lbl2 = Label(pro3, text="검색어")
    lbl2.grid(row=1, column=0)
    txtsearchpath = Entry(pro3)
    txtsearchpath.grid(row=0, column=1)
    txtsearchpath.bind("<Return>", txtsearchpath.get())
    txtsearch = Entry(pro3)
    txtsearch.grid(row=1, column=1)
    txtsearch.bind("<Return>", txtsearch.get())
    btntax = tk.Button(pro3, text="검색", command=OKSearch)
    btntax.grid(row=2, column=1)

    def ADDElement():
        global c
        c= c+2
        listbox2.insert(c, "3.검색창 PATH값 : %s" % txtsearchpath.get())
        listbox2.insert(c+1, "4.검색어 : %s" % txtsearch.get())
    def DELElement():
        global c
        c= c-1
        listbox2.delete(END)

    def ADELElement():
        global c
        c=0
        listbox2.delete(0,END)

    def LCELElement():
        global c
        global listB
        listB=(listbox2.get(0,END))
        print(len(listB))
        for i in range(len(listB)):
            listbox.insert(i+2, (listbox2.get(i))) #검색이니까
        # print(listB)
        c = 0
        pro3.destroy()

    btntax = tk.Button(pro3, text="추가하기", command=ADDElement)
    btntax.grid(row=4, column=1)
    btntax = tk.Button(pro3, text="삭제하기", command=DELElement)
    btntax.grid(row=5, column=1)
    btntax = tk.Button(pro3, text="전체삭제", command=ADELElement)
    btntax.grid(row=6, column=1)
    btntax = tk.Button(pro3, text="완료", command=LCELElement)
    btntax.grid(row=6, column=3)
    lbl2 = Label(pro3, text="검색리스트")
    lbl2.grid(row=2, column=7)
    listbox2 = Listbox(pro3, selectmode='extended', height=5, width=30)
    listbox2.grid(row=3, column=7)

    pro3.mainloop()
    win.mainloop()
def OKSearch():
    listbox.insert(END, "3.검색창 PATH값 : %s" % txtsearchpath.get())
    listbox.insert(END, "4.검색어 : %s" % txtsearch.get())
    pro3.withdraw()

def CollectData():
    global pro4
    global txtDP1
    global txtDP2
    pro4 = Toplevel(win)
    pro4.title("데이터 수집")  # 창의 타이틀명
    pro4.geometry("500x300")  # 창의 사이즈


    lbl1 = Label(pro4, text="예시데이터 PATH값 1")
    lbl1.grid(row=0, column=0)
    lbl2 = Label(pro4, text="예시데이터 PATH값 2")
    lbl2.grid(row=1, column=0)
    txtDP1= Entry(pro4)
    txtDP1.grid(row=0, column=1)
    txtDP1.bind("<Return>", txtDP1.get())
    txtDP2 = Entry(pro4)
    txtDP2.grid(row=1, column=1)
    txtDP2.bind("<Return>", txtDP2.get())
    btntax = tk.Button(pro4, text="데이터 추출", command=OKData)
    btntax.grid(row=2, column=1)
    pro4.mainloop()
    win.mainloop()
def OKData():
    listbox.insert(END, "5.데이터 수집 PATH값 1: %s" % txtDP1.get())
    listbox.insert(END, "6.데이터 수집 PATH값 2: %s" % txtDP2.get())
    pro4.withdraw()

def listToString(str_list):
    result = ""
    for s in str_list:
        result += s + ""
    return result.strip()
def Delete():
    listbox.delete(END)
def ALLDelete():
    listbox.delete(0,END)


def final():
    #if listbox
    global driver
    global a
    driver = webdriver.Chrome("chromedriver.exe")
    url = txt1.get()
    driver.get(url)
    driver.get(driver.current_url)
    try:
        a = ResultEle()
        a.click()
        t.sleep(3)
        print(driver.current_url)
        driver.get(driver.current_url)
        try:
            elem = driver.find_element(By.XPATH, txtsearchpath.get())
            elem.send_keys(txtsearch.get())
            elem.send_keys(Keys.RETURN)
            t.sleep(3)
            driver.get(driver.current_url)
            lista = []
            listb = []
            for i in range(len(txtDP1.get())):  #데이터 수집 txtDP1.get elem값   txtDP2. div[1~ DP2]
                if txtDP1.get()[i] == txtDP2.get()[i]:
                    print(txtDP1.get())
                    print(txtDP2.get())
                    lista.append(txtDP1.get()[i])

                elif txtDP1.get()[i] != txtDP2.get()[i]:
                    print(txtDP1.get())
                    print(txtDP2.get())
                    listb.append(txtDP1.get()[i:len(txtDP1.get())])
                    break
            print(lista)
            print(listb)
            result1 = listToString(lista)
            result2 = listToString(listb)
            for xpath2 in range(1, 100000000000):
                try:
                    xpath100 = result1 + str(xpath2) + result2[1:]
                    print(str(xpath2), ": %s" % driver.find_element(By.XPATH, xpath100).text)

                    d1 = driver.find_element(By.XPATH, xpath100).text
                    # mm2.deldata()
                    mm2.inpelement('', '', d1,'')
                except:
                    print("데이터 수집 완료")
                    break
        except:
            lista = []
            listb = []
            for i in range(len(txtDP1.get())):
                if txtDP1.get()[i] == txtDP2.get()[i]:
                    lista.append(txtDP1.get()[i])
                elif txtDP1.get()[i] != txtDP2.get()[i]:
                    listb.append(txtDP1.get()[i:len(txtDP1.get())])
                    break

            result1 = listToString(lista)
            result2 = listToString(listb)
            for xpath2 in range(1, 100000000000):
                try:
                    xpath100 = result1 + str(xpath2) + result2[1:]
                    print(str(xpath2), ": %s" % driver.find_element(By.XPATH, xpath100).text)
                    d1 = driver.find_element(By.XPATH, xpath100).text
                    # mm2.deldata()
                    mm2.inpelement('', '', d1)
                except:
                    print("데이터 수집 완료")
                    break
    except:
        try:
            elem = driver.find_element(By.XPATH, txtsearchpath.get())
            elem.send_keys(txtsearch.get())
            elem.send_keys(Keys.RETURN)
            t.sleep(3)
            driver.get(driver.current_url)
            lista = []
            listb = []
            for i in range(len(txtDP1.get())):
                if txtDP1.get()[i] == txtDP2.get()[i]:
                    lista.append(txtDP1.get()[i])
                elif txtDP1.get()[i] != txtDP2.get()[i]:
                    listb.append(txtDP1.get()[i:len(txtDP1.get())])
                    break

            result1 = listToString(lista)
            result2 = listToString(listb)
            for xpath2 in range(1, 100000000000):
                try:
                    xpath100 = result1 + str(xpath2) + result2[1:]
                    d1 = driver.find_element(By.XPATH, xpath100).text
                    # mm2.deldata()
                    mm2.inpelement('', '', d1)
                except:
                    print("데이터 수집 완료")
                    break
        except:
            lista = []
            listb = []
            for i in range(len(txtDP1.get())):
                if txtDP1.get()[i] == txtDP2.get()[i]:
                    lista.append(txtDP1.get()[i])
                elif txtDP1.get()[i] != txtDP2.get()[i]:
                    listb.append(txtDP1.get()[i:len(txtDP1.get())])
                    break

            result1 = listToString(lista)
            result2 = listToString(listb)
            for xpath2 in range(1, 100000000000):
                try:
                    xpath100 = result1 + str(xpath2) + result2[1:]
                    print(str(xpath2), ": %s" % driver.find_element(By.XPATH, xpath100).text)
                    d1 = driver.find_element(By.XPATH, xpath100).text
                    # mm2.deldata()
                    mm2.inpelement('', '', d1)
                except:
                    print("데이터 수집 완료")
                    break



def save():
    # d1 = driver.find_element(By.XPATH, xpath100).text
    # mm2.inpelement('', '', d1)
    import os.path
    path = "element.txt"
    print(save)
    if not os.path.isfile(path):
       f = open('element.txt', 'w')

def load():
    print(load)

listbox = Listbox(win, selectmode='extended', height=10, width=100)
listbox.pack()
"""
list_frame=Frame(win)
list_frame.pack(fill="both",padx=5,pady=5)
scrollbar=Scrollbar(list_frame)
scrollbar.pack(side="right",fill="y")
list_file=Listbox(list_frame,selectmode="extended",height=15,yscrollcommand=scrollbar.set)
list_file.pack(side="left",fill="both",expand=True)
scrollbar.config(command=list_file.yview)
"""
btn1=tk.Button(framefirst,width=20,height=10,text="URL입력",font=("bold",10,"bold"),fg="white",bg="mediumturquoise",command=InputURLpage)
btn1.grid(row=3, column=3)
btn2=tk.Button(framefirst,width=20,height=10,text="요소입력",font=("bold",10,"bold"),fg="white",bg="cornflowerblue", command=InputElement)
btn2.grid(row=3, column=4)
btn4=tk.Button(framefirst,width=20,height=10,text="검색값입력",font=("bold",10,"bold"),fg="white",bg="mediumslateblue",command=InputSearch)
btn4.grid(row=3, column=5)
btn3=tk.Button(framefirst,width=20,height=10,text="데이터수집",font=("bold",10,"bold"),fg="white",bg="mediumpurple",command=CollectData)
btn3.grid(row=3, column=6)

lbl0 = Label(win, text="")
lbl0.pack()
btn2=tk.Button(win, text="불러오기",command=load)
# btn2.place(x=50,y=100)
btn2.pack(side='right')
btn1=tk.Button(win, text="저장",command=save)
# btn1.place(x=50,y=100)
btn1.pack(side='right')



btnOUTPUT=tk.Button(win, text="출력",command=final)
btnOUTPUT.pack()
btnreset=tk.Button(win, text="초기화",command=Delete)
btnreset.pack()
btnADEL=tk.Button(win, text="allDEL",command=ALLDelete)
btnADEL.pack()
win.mainloop()