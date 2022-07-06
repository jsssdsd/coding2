# follow 여부 체크하기
def checkFollow(user,postClass):
    file=open('following.txt','r',encoding='UTF-8')
    lines=file.readlines()
    file.close()
    lines=lines[1:]
    for i in range(len(lines)):
        lines[i]=lines[i].strip().split('\t')
        if user.id == lines[i][0] and postClass.ID == lines[i][1]:
            return
    return 'not yet'
# follow 명단 작성
def checkFollowlist(user):
    file=open('following.txt','r',encoding='UTF-8')
    lines=file.readlines()
    file.close()
    lines=lines[1:]
    temp_1=[]
    for i in range(len(lines)):
        lines[i]=lines[i].strip().split('\t')
        if user.id == lines[i][0]:
            temp_1.append(lines[i][1])
    return temp_1
# follow 하기
def followYou(user,postClass):
    file=open('following.txt','a',encoding='UTF-8')
    file.write('{}\t{}\n'.format(user.id,postClass.ID))
    file.close()
# unfollow하기
def unfollowYou(user,postClass):
    file=open('following.txt','r',encoding='UTF-8')
    lines=file.readlines()
    file.close()
    lines.remove('{}\t{}\n'.format(user.id,postClass.ID))
    file=open('following.txt','w',encoding='UTF-8')
    for i in range(len(lines)):
        file.write(lines[i])
    file.close()
# 맞팔 확인하기
def followBack(user,postClass):
    file=open('following.txt','r',encoding='UTF-8')
    lines=file.readlines()
    file.close()
    for i in range(len(lines)):
        lines[i]=lines[i].strip().split('\t')
    for i in range(len(lines)):
        if user.id == lines[i][0] and postClass.ID == lines[i][1]:
            for m in range(len(lines)):
                if postClass.ID == lines[m][0] and user.id == lines[m][1]:
                    return
    return'followBack'
# 맞팔 확인하기2
def followBack2(user,postData):
    file=open('following.txt','r',encoding='UTF-8')
    lines=file.readlines()
    file.close()
    for i in range(len(lines)):
        lines[i]=lines[i].strip().split('\t')
    for i in range(len(lines)):
        if user.id == lines[i][0] and postData[1] == lines[i][1]:
            for m in range(len(lines)):
                if postData[1] == lines[m][0] and user.id == lines[m][1]:
                    return
    return'followBack'