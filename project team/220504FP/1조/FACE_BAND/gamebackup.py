import tkinter as tk
import tkinter.font as font
import numpy as np
import random as rd
from tkinter import messagebox
import MVP_class as vp
import time
from PIL import Image, ImageTk

x=0
x2=0
class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
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

class user_data():
    def __init__(self,id,pw,name,n_name,birth,gen,email,coin):
        self.id=id
        self.pw=pw
        self.name=name
        self.n_name=n_name
        self.birth=birth
        self.gen=gen
        self.email=email
        self.coin=coin
user=user_data("1234","1234","박동진","기린","990325","남자","qwe123@naver.com","999999999")

def game_re_make():
    import root
    font=tk.font.Font(size=13)

    # 함수 정의

    # 1.mvp관련 함수
    def num_mvp():
        aa = vp.mvp_cut()[:20]
        temp_str = ''
        for i in range(len(aa)):
            temp_str += ' {}\n'.format(i + 1)
        mvp_count2 = tk.Label(img_mvp, text=temp_str, anchor='n',font=font)
        mvp_count2.place(x=240, y=150, height=315, width=80)

    def live_time():
        aa = vp.mvp_cut()[:20]
        temp_list1 = ''
        for i in range(len(aa)):
            time_get = round(float(aa[i][2]),5)

            temp_list1 += '  {}\n'.format(time_get)
        mvp_listbox2 = tk.Label(img_mvp, text=temp_list1, anchor='n',font=font)
        mvp_listbox2.place(x=320, y=150, height=315, width=80)

    def nick():
        aa = vp.mvp_cut()[:20]
        temp_list3 = ''
        x_place = 580
        y_place=152
        for i in range(len(aa)):
            temp_list3 += '  {}\n'.format(vp.listbox_insert()[i][1])
            mvp_listbox6 = tk.Label(img_mvp, text=temp_list3,anchor='n',font=font)
            mvp_listbox6.place(x=480, y=150, height=315, width=100)
            globals()["vs_btn{}".format(i)]=tk.Button(img_mvp,text='VS')
            eval('vs_btn'+str(i)).place(x=x_place,y=y_place,height=15, width=27)
            y_place+=17
            def vs():
                global user
                opponent=aa[i]


    def mvp_list():
        num_mvp()
        live_time()
        nick()

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

    def showMVP():
        mvp_list()
        img_mvp.tkraise()

    # 2.게임관련 함수
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
            bind_game(img_sun,3)
            show_sun()

        elif sNumbers=='비':
            bind_game(img_rain,5)
            show_rainy()

    def show_main():
        main_img.tkraise()

    def bind_game(a,b):
        where=a
        num=b
        def earth_worm(event):
            global x
            global x2
            text_coin()
            x = 0
            x2 = 0
            now = time.time()

            def space_click(event):
                global x
                if x >= 516:
                    tt = tk.messagebox.showinfo(message='이겨버렸다. 너무 시시해서 죽고싶어졌다.')
                    finish = time.time()
                    finish_time = finish - now
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
                label1 = tk.Label(where, image=listImage[rn])
                label1.place(x=x, y=500)

                if x2 >= 516 > x:
                    tt = tk.messagebox.showinfo(message='졌다.')
                    return
                elif x >= 516:
                    label1.destroy()
                label1.after(300, img)
                label1.after(300, label1.destroy)

            def img2():
                global x2
                if x2 >= 516:
                    return
                rn2 = np.random.randint(2)
                label2 = tk.Label(where, image=listImage[rn2])
                label2.place(x=x2, y=400)
                label2.after(30, img2)
                label2.after(30, label2.destroy)
                x2 += 3

            tm = time.time()
            image1 = tk.PhotoImage(file='image1.png')
            image2 = tk.PhotoImage(file="image2.png")
            listImage = [image1, image2]
            root.bind("<KeyRelease>", space_click)
            img()
            img2()
        root.bind("<space>", earth_worm)

    # def earth_worm(event,where,num):
    #     global x
    #     global x2
    #     text_coin()
    #     x=0
    #     x2=0
    #     now = time.time()
    #     def space_click(event):
    #         global x
    #         if x >= 516:
    #             tt = tk.messagebox.showinfo(message='이겨버렸다. 너무 시시해서 죽고싶어졌다.')
    #             finish=time.time()
    #             finish_time=finish-now
    #             global user
    #             text = open('MVP.txt', 'a', encoding='utf-8')
    #             text.write(user.id+'\t'+user.n_name+'\t'+str(finish_time)+'\n')
    #             text.close()
    #             return
    #         else:
    #             x = x + num
    #         return x
    #
    #     def img():
    #         global x
    #         global x2
    #         rn = np.random.randint(2)
    #         label1 = tk.Label(where, image=listImage[rn])
    #         label1.place(x=x, y=500)
    #
    #         if x2>=516>x:
    #             tt = tk.messagebox.showinfo(message='졌다.')
    #             return
    #         elif x>=516:
    #             label1.destroy()
    #         label1.after(300, img)
    #         label1.after(300, label1.destroy)
    #
    #     def img2():
    #         global x2
    #         if x2 >= 516:
    #             return
    #         rn2 = np.random.randint(2)
    #         label2 = tk.Label(where, image=listImage[rn2])
    #         label2.place(x=x2, y=400)
    #         label2.after(30, img2)
    #         label2.after(30, label2.destroy)
    #         x2 += 3
    #
    #
    #
    #     tm=time.time()
    #     image1 = tk.PhotoImage(file='image1.png')
    #     image2 = tk.PhotoImage(file="image2.png")
    #     listImage = [image1, image2]
    #     root.bind("<space>", space_click)
    #     img()
    #     img2()

    def text_coin():
        global user
        text=open('user.txt','r',encoding='utf-8')
        texts=text.readlines()
        text.close()
        user_list=[]
        for i in texts[1:0]:
            user_list.append(i.replace('\n','').split('\t'))
        user.coin=str(int(user.coin)-1)
        text=open('user.txt','w',encoding='utf-8')
        for i in range(len(user_list)):
            if user.id==user_list[i][0]:
                user_list[i][7]=user.coin
            text.write(user_list[i][0]+'\t'+user_list[i][1]+'\t'+user_list[i][2]+'\t'+user_list[i][3]+'\t'+user_list[i][4]+'\t'+user_list[i][5]+'\t'+user_list[i][6]+'\t'+user_list[i][7]+'\n')
        text.close()
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
        print(user.coin)
        img_mylife.tkraise()

    # 프레임

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

    root.mainloop()

