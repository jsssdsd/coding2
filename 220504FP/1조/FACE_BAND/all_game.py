import earthwarmgame as earth
import game_gui_test as day
import random
import time
import tkinter as tk
import random as rd
import numpy as np
import onedaylife_data_test as one
import MVP_class as vp

def all_game():
    window1 = tk.Tk()
    window1.title("게임툴")
    window1.geometry("800x600")
    window1.resizable(False, False)

    def destroy_earth():
        window1.destroy()
        earth.game_re_make()

    def destroy_onelife():
        window1.destroy()
        day.game_1()



    earth_btn1=tk.Button(window1,text="지렁이 게임",command=destroy_earth)
    earth_btn1.place(x=100,y=450,width=100,height=50)
    onelife_btn1 = tk.Button(window1, text="하루살이 게임", command=destroy_onelife)
    onelife_btn1.place(x=600, y=450, width=100, height=50)

    window1.mainloop()

all_game()
