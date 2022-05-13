import tkinter as tk
from tkinter import ttk

# 코멘트 클래스
class commentClass:
    def __init__(self,postNum,commentNum,id,nick,time,comment):
        self.postNum=postNum
        self.commentNum=commentNum
        self.id=id
        self.nick = nick
        self.time=time
        self.comment=comment
# 댓글 작성
def writeComment(user,postClass,comment): # 파일에 데이터 추가
    import time

    file=open('cnt2.txt','r',encoding='UTF-8')
    cnt=file.readline()
    file.close()
    cnt=int(cnt)
    tm=time.time()
    a = open("comment.txt", "a", encoding="UTF-8")
    a.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (postClass.postNum,'co_{}'.format(cnt),user.id,user.n_name,tm,comment))
    a.close()
    cnt+=1
    file=open('cnt2.txt','w',encoding='UTF-8')
    file.write(str(cnt))
    file.close()
# 답글 작성
def writeReply(user,commentClass,reply):
    import time

    tm=time.time()
    a = open("comment.txt", "a", encoding="UTF-8")
    a.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (commentClass.postNum,commentClass.commentNum,user.id,user.n_name,tm,reply))
    a.close()
# 댓글 리스트 뽑기
def showComent(postClass):
    file=open('comment.txt','r',encoding='UTF-8')
    lines=file.readlines()
    file.close()
    for i in range(len(lines)):
        lines[i]=lines[i].strip().split('\t')
    tempList1=[]
    for i in range(len(lines)):
        if postClass.postNum == lines[i][0]:
            tempList1.append(lines[i])
    tempList2=[]
    for i in range(len(tempList1)):
        tempList2_2=[]
        if not tempList2:
            tempList2.append(tempList1[i])
        for m in range(len(tempList2)):
            tempList2_2.append(tempList2[m][1])
        if tempList1[i][1] not in tempList2_2:
            tempList2.append(tempList1[i])
    tempList3=[]
    for i in range(len(tempList2)):
        tempList3.append(commentClass(tempList2[i][0],tempList2[i][1],tempList2[i][2],tempList2[i][3],tempList2[i][4],tempList2[i][5]))
    return tempList3
# 답글 리스트 뽑기
def showReply(commentClass):
    file=open('comment.txt','r',encoding='UTF-8')
    lines=file.readlines()
    file.close()
    for i in range(len(lines)):
        lines[i]=lines[i].strip().split('\t')
    tempList=[]
    for i in range(len(lines)):
        if lines[i][1]==commentClass.commentNum:
            tempList.append(lines[i])
    return tempList
# 댓글 답글 다 뽑기
def showAllcomment(postClass):
    tempList1=showComent(postClass)
    tempList2=[]
    for i in range(len(tempList1)):
        tempList0 = []
        for m in range(len(showReply(tempList1[i]))):
            tempList0.append(commentClass(showReply(tempList1[i])[m][0],showReply(tempList1[i])[m][1],showReply(tempList1[i])[m][2],showReply(tempList1[i])[m][3],showReply(tempList1[i])[m][4],showReply(tempList1[i])[m][5]))
        tempList2.append(tempList0)
    return tempList2
# 댓글창 구현
def Makecomment(user,postClass,win):
    import time
    from time import strftime
    # 답글작성
    def Reply(user,postClass,commentIndex,comment,win):
        commentList=showAllcomment(postClass)[commentIndex]
        commentClass=commentList[0]
        writeReply(user, commentClass, comment)
        Makecomment(user, postClass, win)
        win.tkraise()
    # 댓글작성
    def write_Comment(user, postClass, comment,win):
        writeComment(user, postClass, comment)
        Makecomment(user, postClass, win)
        win.tkraise()

    # 댓글 <-> 답글
    def switchBtn(index):
        global commentIndex
        if btn[index]['text']=='답글':
            for i in range(len(btn)):
                if i==index:
                    btn[i].configure(text='X')
                else:
                    btn[i].configure(text='X',state='disabled')
            btn2.tkraise()
            commentIndex=index
        else:
            for i in range(len(btn)):
                if i==index:
                    btn[i].configure(text='답글')
                else:
                    btn[i].configure(text='답글',state='normal')
            btn1.tkraise()
            commentIndex=''
    # 프레임 생성
    frame = tk.Frame(win)
    frame.place(x=50, y=200, width=500, height=150)
    # 캔버스 생성
    comment_canvas = tk.Canvas(frame)
    # 캔버스에 스크롤 바 추가
    comment_scrollbar = ttk.Scrollbar(frame, orient='vertical', command=comment_canvas.yview)
    comment_scrollbar.pack(side='right', fill='y')
    comment_scrollbar2 = ttk.Scrollbar(frame, orient='horizontal', command=comment_canvas.xview)
    comment_scrollbar2.pack(side='bottom', fill='x')
    comment_canvas.pack(side='left', fill='both', expand=1)
    # 캔버스 변경하기
    comment_canvas.configure(yscrollcommand=comment_scrollbar.set,xscrollcommand=comment_scrollbar2.set)
    comment_canvas.bind('<Configure>',lambda e: comment_canvas.configure(scrollregion=comment_canvas.bbox('all')))
    # 캔버스 안에 다른 프레임 생성
    second_frame = tk.Frame(comment_canvas)
    second_frame.pack()
    # 캔버스 안에 새로운 프레임을 창에 추가하기
    comment_canvas.create_window((0,0), window=second_frame, anchor='nw')
    # 내용 정렬하여 넣어주기
    cnt1=0
    cnt2=0
    btn=[]
    for i in range(len(showAllcomment(postClass))):
        for m in range(len(showAllcomment(postClass)[i])):
            if m==0:
                tm= strftime('%Y-%m-%d %I:%M:%S %p', time.localtime(float(showAllcomment(postClass)[i][0].time)))
                ttk.Label(second_frame,anchor='w', text="{}.  ".format(cnt1+1)).grid(row=cnt2, column=0)
                ttk.Label(second_frame,anchor='w', text='{}'.format(showAllcomment(postClass)[i][0].comment)).grid(row=cnt2, column=1)
                ttk.Label(second_frame,anchor='w', text='\t{}'.format(showAllcomment(postClass)[i][0].nick)).grid(row=cnt2, column=2)
                ttk.Label(second_frame,anchor='w', text='\t{}'.format(tm)).grid(row=cnt2, column=3)
                btn.append(ttk.Button(second_frame, text='답글',command=lambda c=cnt1: switchBtn(c),width=4))
                btn[cnt1].grid(row=cnt2, column=4)
                cnt1+=1
            else:
                tm= strftime('%Y-%m-%d %I:%M:%S %p', time.localtime(float(showAllcomment(postClass)[i][m].time)))
                ttk.Label(second_frame, anchor='w',text="  ┖").grid(row=cnt2, column=0)
                ttk.Label(second_frame, anchor='w', text="{}".format(showAllcomment(postClass)[i][m].comment)).grid(row=cnt2, column=1)
                ttk.Label(second_frame, anchor='w', text="\t{}".format(showAllcomment(postClass)[i][m].nick)).grid(row=cnt2, column=2)
                ttk.Label(second_frame, anchor='w', text="\t{}".format(tm)).grid(row=cnt2, column=3)
            cnt2+=1
    # 댓글 및 답글 작성
    comment=tk.Entry(win)
    comment.place(x=50,y=150, width=400,height=30)
    # 답글 버튼
    btn2=tk.Button(win,text='답글',command=lambda c=comment.get(): Reply(user, postClass, commentIndex, comment.get(),win))
    btn2.place(x=470,y=150,width=80,height=30)
    # 댓글 버튼
    btn1=tk.Button(win,text='댓글',command=lambda c=comment.get(): write_Comment(user, postClass, comment.get(),win))
    btn1.place(x=470,y=150,width=80,height=30)

