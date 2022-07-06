from PIL import Image
import tkinter as tk
import numpy as np
import random as rd
import time




def stop_watch():
    root = tk.Tk()
    root.title("하루살이 Game")
    root.geometry("800x600")
    root.resizable(False, False)
    frameCnt = 30
    frames = [tk.PhotoImage(file='타이머.gif', format='gif -index %i' % (i)) for i in range(frameCnt)]

    def update(ind):
        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        label1.configure(image=frame)
        root.after(100, update, ind)

    # set image
    label1 = tk.Label(root, bg='black')
    label1.place(x=200, y=380, height=220, width=400)
    root.after(100, update, 0)
    root.mainloop()
stop_watch()












