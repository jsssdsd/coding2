def checklist() : # 파일의 여부 확인 및 생성
    import os.path

    path = 'user.txt'
    if os.path.isfile(path) :
        pass
    else :
        x='아이디\t패스워드\t이름\t닉네임\t생년월일\t성별\t이메일\t코인보유량\n'
        list=open('user.txt','w',encoding='UTF-8')
        list.write(x)
        list.close()

    path = "post.txt"
    if os.path.isfile(path) :
        pass
    else :
        x="post_num\tID\t제목\t시간\t비밀글여부\t닉네임\n"
        list=open("post.txt", "w", encoding="UTF-8")
        list.write(x)
        list.close()

    path = 'cnt.txt'
    if os.path.isfile(path):
        pass
    else:
        list=open('cnt.txt','w',encoding='UTF-8')
        list.write('1')
        list.close()

    path = 'cnt2.txt'
    if os.path.isfile(path):
        pass
    else:
        list=open('cnt2.txt','w',encoding='UTF-8')
        list.write('1')
        list.close()

    path = 'following.txt'
    if os.path.isfile(path) :
        pass
    else :
        x='아이디\t팔로잉\n'
        list=open('following.txt','w',encoding='UTF-8')
        list.write(x)
        list.close()

    path = 'comment.txt'
    if os.path.isfile(path) :
        pass
    else :
        x='post_num\tcomment_num\t아이디\t닉네임\t시간\t내용\n'
        list=open('comment.txt','w',encoding='UTF-8')
        list.write(x)
        list.close()

    path = 'like.txt'
    if os.path.isfile(path) :
        pass
    else :
        x='post_num\t아이디\t닉네임\n'
        list=open('like.txt','w',encoding='UTF-8')
        list.write(x)
        list.close()

    path = 'MVP.txt'
    if os.path.isfile(path) :
        pass
    else :
        x='아이디\t닉네임\t걸린 시간\n'
        list=open('MVP.txt','w',encoding='UTF-8')
        list.write(x)
        list.close()

    path = 'coin_get.txt'
    if os.path.isfile(path) :
        pass
    else :
        x='아이디\t포스팅\t로그인\t인기글\n'
        list=open('coin_get.txt','w',encoding='UTF-8')
        list.write(x)
        list.close()

    path = 'onedaylife_coin_use.txt'
    if os.path.isfile(path) :
        pass
    else :
        x='아이디\t닉네임\t사용시간\n'
        list=open('onedaylife_coin_use.txt','w',encoding='UTF-8')
        list.write(x)
        list.close()
