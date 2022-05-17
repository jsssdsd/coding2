import tkinter as tk
from tkinter import *
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium import webdriver
import mecrosel_mod2 as mm2
import time as t
win = Tk()
win.title('매크로 프로그램')
win.geometry("840x478") #창의 사이즈
win.resizable(False,False) #창의 사이즈 변경 여부 속성 지정\
framefirst=Frame(win)
framefirst.pack()
framesecond=Frame(win)
framesecond.pack()






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
    listbox.delete(0)
    listbox.insert(0, txt1.get())
    pro.withdraw()

def InputElement():
    global pro2
    global txt2
    global answer1
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
    btntax = tk.Button(pro2, text="적용하기", command=OKElement)
    btntax.grid(row=4, column=1)
    pro2.mainloop()
    win.mainloop()
def ResultEle():
    if answer1.get() == 0:
        return driver.find_element(By.CLASS_NAME, txt2.get())
    elif answer1.get() == 1:
        return driver.find_element(By.XPATH, txt2.get())
    elif answer1.get() == 2:
        return driver.find_element(By.ID, txt2.get())
def OKElement():
    listbox.delete(1)
    listbox.insert(1, "%s" % txt2.get())
    pro2.withdraw()
def final():
    global driver
    driver = webdriver.Chrome("chromedriver.exe")
    try:
        url = txt1.get()
        mm2.inpelement(txt1.get())  #메모장에 추가 url
        driver.get(url)
        a = ResultEle()
        a.click()
        t.sleep(1)
    except:
        lbl0.config(text="모든 값을 입력해주세요.")

#
#
# def recodingM():
#     mm2.inpelement(txt1)
#


#페이지 열림 완료 시점
#
 #2초의 텀을준다.
#프레임전환

#프레임 전환을 해야한다.!! iframe 으로 프레임이 바꼈으므로
# x.switch_to.frame("searchIframe")

#menu_bg menu01 #멜론차트 클래스 불러오기
"""
a= driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/section/div/div[2]/ul[2]/li[5]/a')
print(a.text)
a.click()
t.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
xpath1='/html/body/div[1]/aside/nav/nav/nav[2]/nav/a/span'
try:
    elem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,xpath1))).click()
    elem.click()
except TimeoutException:
    print("타임아웃")
elem2 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/aside/nav/nav/nav[2]/nav/nav/a[1]')))
"""







listbox = Listbox(win, selectmode='extended', height=0)

listbox.pack()
btn1=tk.Button(framefirst,width=25,height=10,text="URL입력",font=("bold",10,"bold"),fg="midnightblue",bg="lightblue",command=InputURLpage)
btn1.grid(row=3, column=3)
btn2=tk.Button(framefirst,width=25,height=10,text="요소입력",font=("bold",10,"bold"),fg="darkslategrey",bg="mediumaquamarine", command=InputElement)
btn2.grid(row=3, column=4)
btn3=tk.Button(framefirst,width=25,height=10,text="데이터수집",font=("bold",10,"bold"),fg="white",bg="cadetblue")#,command=nextpage3)
btn3.grid(row=3, column=5)
btn4=tk.Button(framefirst,width=25,height=10,text="검색값입력",font=("bold",10,"bold"),fg="indigo",bg="thistle")#,command=nextpage4)
btn4.grid(row=3, column=6)
btn5=tk.Button(framefirst,width=25,height=10,text="지우기",font=("bold",10,"bold"),fg="indigo",bg="thistle")#,command=nextpage4)
btn5.grid(row=3, column=7)
btnfin=tk.Button(win,text="출력", command=final)
lbl0 = Label(win, text="")
lbl0.pack()
btnfin.pack()
win.mainloop()