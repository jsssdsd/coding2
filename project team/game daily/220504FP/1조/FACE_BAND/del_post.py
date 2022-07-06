def delmyPost(postClass):
    # 게시물 삭제
    file=open('post.txt','r',encoding='UTF-8')
    lines=file.readlines()
    file.close()
    for i in range(len(lines)):
        lines[i]=lines[i].strip().split('\t')
    for i in range(len(lines)):
        if  lines[i][0] == postClass.postNum:
            del lines[i]
            break
    # 게시물 새로 저장
    file=open('post.txt','w',encoding='UTF-8')
    for i in range(len(lines)):
        file.write('{}\t{}\t{}\t{}\t{}\t{}\n'.format(lines[i][0],lines[i][1],lines[i][2],lines[i][3],lines[i][4],lines[i][5]))
    file.close()
    # 댓글삭제
    file=open('comment.txt','r',encoding='UTF-8')
    lines=file.readlines()
    file.close()
    for i in range(len(lines)):
        lines[i]=lines[i].strip().split('\t')
    for i in range(len(lines)):
        if postClass.postNum == lines[i][0]:
            del lines[i]
            break
    # 댓글 새로 저장
    file=open('comment.txt','w',encoding='UTF-8')
    for i in range(len(lines)):
        file.write('{}\t{}\t{}\t{}\t{}\t{}\n')
    file.close()