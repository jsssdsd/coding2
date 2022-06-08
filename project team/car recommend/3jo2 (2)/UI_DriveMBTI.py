import tkinter as tk
from tkinter import *

pro = tk.Tk()
pro.title("운전 성향 검사")
pro.geometry("600x900")
pro.resizable(False, False)


def result():
    score=answer1.get()+answer2.get()+answer3.get()+answer4.get()+answer5.get()+answer6.get()+answer7.get()+answer8.get()+answer9.get()+answer10.get()
    if score == 0:
        lb14.config(text="내향성.")
    elif 1<=score<=2:
        lb14.config(text="내향성.")
    elif score >= 5:
        lb14.config(text="외향성.")
    else:
        lb14.config(text="다시 입력하십시오.")


def retry():
    lb14.config(text="")

def close():
    top.destroy()


def nextpage():
    global top
    top = Toplevel(pro)

    top.title("adsfdf")
    bt1=tk.Button(top, text="클릭", command=close)
    bt1.pack()
    pro.mainloop()



lb1 = tk.Label(pro, text="운전 성향 테스트", bg="yellow")
lb1.grid(row=0, column=0)
lb2 = tk.Label(pro, text="다음 질문의 두가지 선택사항 중 하나를 선택해 주세요.", )
lb2.grid(row=1, column=0)
lb3 = tk.Label(pro)
lb3.grid(row=2, column=0)
lb4 = tk.Label(pro, text="질문 1. 내 차의 청결상태는?")
lb4.grid(row=3, column=0, sticky="w")
lb5 = tk.Label(pro, text="질문 2. 차를 타다 미세한 문콕을 발견한 나는")
lb5.grid(row=6, column=0, sticky="w")
lb6 = tk.Label(pro, text="질문 3. 나는 차에서 노래를")
lb6.grid(row=9, column=0, sticky="w")
lb7 = tk.Label(pro, text="질문 4. 정체구간 깜빡이 넣고 힘겹게 끼어들기하려는 차량이 있다면?")
lb7.grid(row=12, column=0, sticky="w")
lb8 = tk.Label(pro, text="질문 5. 내비게이션이 알려주는 길을")
lb8.grid(row=15, column=0, sticky="w")
lb9 = tk.Label(pro, text="질문 6. 나는 조수석에 타면")
lb9.grid(row=18, column=0, sticky="w")
lb10 = tk.Label(pro, text="질문 7. 내 차에 있는 기능을")
lb10.grid(row=21, column=0, sticky="w")
lb11 = tk.Label(pro, text="질문 8. 나는 약속시간을")
lb11.grid(row=24, column=0, sticky="w")
lb12 = tk.Label(pro, text="질문 9. 내가 생각하는 내 운전실력은")
lb12.grid(row=27, column=0, sticky="w")
lb13 = tk.Label(pro, text="질문 10. 지인이 사고가 났다면 내가 할 말은")
lb13.grid(row=30, column=0, sticky="w")
lb14 = tk.Label(pro)
lb14.grid(row=33, column=0, sticky="w")

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
rad1 = tk.Radiobutton(pro, text="누가봐도 깔끔하게 항상 정돈되어 있다.", variable=answer1, value=0)
rad1.grid(row=4, column=0, sticky="w")
rad2 = tk.Radiobutton(pro, text="어제 먹다 남은 음료수 캔도 그대로 남아있다.", variable=answer1, value=1)
rad2.grid(row=5, column=0, sticky="w")
rad3 = tk.Radiobutton(pro, text="찾는게 더 번거롭다. 그냥 넘어간다.", variable=answer2, value=0)
rad3.grid(row=7, column=0, sticky="w")
rad4 = tk.Radiobutton(pro, text="블랙박스를 돌려 어떻게든 범인을 찾아낸다.", variable=answer2, value=1)
rad4.grid(row=8, column=0, sticky="w")
rad5 = tk.Radiobutton(pro, text="그냥 허전해서 듣는다.", variable=answer3, value=0)
rad5.grid(row=10, column=0, sticky="w")
rad6 = tk.Radiobutton(pro, text="노래방보다 더 신나게 부른다.", variable=answer3, value=1)
rad6.grid(row=11, column=0, sticky="w")
rad7 = tk.Radiobutton(pro, text="초보인가? 불쌍해서 넣어준다.", variable=answer4, value=0)
rad7.grid(row=13, column=0, sticky="w")
rad8 = tk.Radiobutton(pro, text="상습범이 분명해! 절대 안 넣어준다.", variable=answer4, value=1)
rad8.grid(row=14, column=0, sticky="w")
rad9 = tk.Radiobutton(pro, text="거의 다 따라서 간다.", variable=answer5, value=0)
rad9.grid(row=16, column=0, sticky="w")
rad10 = tk.Radiobutton(pro, text="내가 더 빠르다고 생각하는 길을 간다.", variable=answer5, value=1)
rad10.grid(row=17, column=0, sticky="w")
rad11 = tk.Radiobutton(pro, text="군말없이 조용히 있는다.", variable=answer6, value=0)
rad11.grid(row=19, column=0, sticky="w")
rad12 = tk.Radiobutton(pro, text="인간 내비게이션이 되어 운전자를 도와준다.", variable=answer6, value=1)
rad12.grid(row=20, column=0, sticky="w")
rad13 = tk.Radiobutton(pro, text="쓰는 것만 쓴다.", variable=answer7, value=0)
rad13.grid(row=22, column=0, sticky="w")
rad14 = tk.Radiobutton(pro, text="한번씩 다 써보려고 한다.", variable=answer7, value=1)
rad14.grid(row=23, column=0, sticky="w")
rad15 = tk.Radiobutton(pro, text="교통체증까지 미리 계산해서 지킨다.", variable=answer8, value=0)
rad15.grid(row=25, column=0, sticky="w")
rad16 = tk.Radiobutton(pro, text="5분 이상 늦는 편이다.", variable=answer8, value=1)
rad16.grid(row=26, column=0, sticky="w")
rad17 = tk.Radiobutton(pro, text="잘하진 않는다. 조심히 한다.", variable=answer9, value=0)
rad17.grid(row=28, column=0, sticky="w")
rad18 = tk.Radiobutton(pro, text="운전경력에 비해 꽤나 잘한다.", variable=answer9, value=1)
rad18.grid(row=29, column=0, sticky="w")
rad19 = tk.Radiobutton(pro, text="어디 다치신데는 없으셨어요?", variable=answer10, value=0)
rad19.grid(row=31, column=0, sticky="w")
rad20 = tk.Radiobutton(pro, text="보험은 드셨어요?", variable=answer10, value=1)
rad20.grid(row=32, column=0, sticky="w")


btn1 = tk.Button(pro, text="완료", command=result)
btn1.grid(row=34, column=0, sticky="w", padx=10, pady=10)
btn2 = tk.Button(pro, text="다시하기", command=retry)
btn2.grid(row=35, column=0, sticky="w", padx=10)

pro.mainloop()
