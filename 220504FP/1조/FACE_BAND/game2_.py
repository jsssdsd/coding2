import tkinter as tk
import numpy as np
import random as rd
from tkinter import messagebox

import time
x=0
x2=0
def game_re_make():
    root = tk.Tk()
    root.title("하루살이 Game")
    root.geometry("800x600")
    root.resizable(False, False)


    # 함수 정의
    def fram_rainy():
        # frame
        frameCnt = 18
        frames_rain = [tk.PhotoImage(file='imghdd.gif', format='gif -index %i' % (i)) for i in range(frameCnt)]

        def update(ind):
            frame = frames_rain[ind]
            ind += 1
            if ind == frameCnt:
                ind = 0
            label1.configure(image=frame)
            root.after(100, update, ind)

        # set image
        label1= tk.Label(img_rain, bg='black')
        label1.place(x=0, y=0,height=380, width=800)
        root.after(100, update, 0)

    def frame_sun():
        frameCnt = 37
        frames = [tk.PhotoImage(file='맑은화면.gif', format='gif -index %i' % (i)) for i in range(frameCnt)]

        def update(ind):
            frame = frames[ind]
            ind += 1
            if ind == frameCnt:
                ind = 0
            label1.configure(image=frame)
            root.after(100, update, ind)

        # set image
        label1 = tk.Label(img_sun, bg='black')
        label1.place(x=0, y=0, height=380, width=800)
        root.after(100, update, 0)

    def show_sun():
        img_sun.tkraise()
        sun_text_label = tk.Label(img_sun, text="70%확률 맑은 프레임")
        sun_text_label.place(x=300, y=15, width=130, height=50)
        sun_text_label.after(1500, sun_text_label.destroy)

    def show_rainy():
        img_rain.tkraise()
        sun_text_label = tk.Label(img_rain, text="30%확률 비오는 프레임")
        sun_text_label.place(x=300, y=15, width=130, height=50)
        sun_text_label.after(1500, sun_text_label.destroy)

    def random_show():
        ephemera=['맑은','비']
        sNumbers = np.random.choice(ephemera,1,p=[0.7,0.3])
        tm_now = time.time()
        if sNumbers=='맑은':
            show_sun()

        elif sNumbers=='비':
            show_rainy()

    def show_main():
        main_img.tkraise()


    def earth_worm():
        global x
        global x2
        x=0
        x2=0
        def space_click(event):
            global x

            if x >= 516:

                tt = tk.messagebox.showinfo(message='이겨버렸다. 너무 시시해서 죽고싶어졌다.')
                return
            else:
                x = x + 2
            return x

        def img():
            global x2
            if x2>=516:

                tt = tk.messagebox.showinfo(message='졌다.')
                return
            rn = np.random.randint(2)
            label1 = tk.Label(main_img, image=listImage[rn])
            label1.place(x=x, y=500)
            label1.after(300, img)
            label1.after(300, label1.destroy)

        def img2():
            global x2

            if x2 >= 516:
                return
            rn2 = np.random.randint(2)
            label2 = tk.Label(main_img, image=listImage[rn2])
            label2.place(x=x2, y=400)
            label2.after(30, img2)
            label2.after(30, label2.destroy)
            x2 += 1.532


        tm=time.time()
        image1 = tk.PhotoImage(file='image1.png')
        image2 = tk.PhotoImage(file="image2.png")
        listImage = [image1, image2]
        root.bind("<KeyRelease>", space_click)
        img()
        img2()

    # 맑은 프레임
    img_sun = tk.Frame(root)
    img_sun.place(x=0, y=0, width=800, height=600)
    frame_sun()
    # 버튼
    sun_btn1 = tk.Button(img_sun, text="랜덤 화면 전환", command=random_show)
    sun_btn1.place(x=720, y=15, width=50, height=50)

    sun_btn3 = tk.Button(img_sun, text="Game", command=show_main)
    sun_btn3.place(x=670, y=15, width=50, height=50)


    # 비오는 프레임
    img_rain = tk.Frame(root)
    img_rain.place(x=0, y=0, width=800, height=600)
    fram_rainy()

    # 버튼
    rain_btn1 = tk.Button(img_rain, text="랜덤 화면전환", command=random_show)
    rain_btn1.place(x=720, y=15, width=50, height=50)

    rain_btn3 = tk.Button(img_rain, text="Game", command=show_main)
    rain_btn3.place(x=670, y=15, width=50, height=50)

    # 메인 프레임
    main_img = tk.Frame(root)
    main_img.place(x=0, y=0, width=800, height=600)
    main_btn1 = tk.Button(main_img, text="랜덤 화면전환", command=random_show)
    main_btn1.place(x=720, y=15, width=50, height=50)
    main_btn2 = tk.Button(main_img, text='게임START', command=earth_worm)
    main_btn2.place(x=620, y=15, width=50, height=50)
    main_btn3 = tk.Button(main_img, text="Game", command=show_main)
    main_btn3.place(x=670, y=15, width=50, height=50)
    lable1=''

    root.mainloop()

game_re_make()