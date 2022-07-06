import tkinter as tk
from PIL import Image, ImageTk
from itertools import count
import time

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

def startGame():
    global key
    def aa():
        btn2.configure(state='normal')

    btn2.configure(state='disabled')
    lbl.load('타이머.gif')
    frame11.after(4700, lbl.unload)
    frame11.after(4700, lbl.load,'ql.gif')
    frame11.after(4700, aa)

root = tk.Tk()
root.geometry('800x600')
frame11 = tk.Frame(root)
frame11.pack()
lbl = ImageLabel(frame11)
lbl.pack()
btn2=tk.Button(text='start',command=startGame)
btn2.pack()
btn1=tk.Button(text='stop',command=lbl.unload)
btn1.pack()
root.mainloop()
