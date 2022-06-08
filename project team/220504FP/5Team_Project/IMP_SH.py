


def U_dicTostr(dict) :
    A_list=[]
    A_str=""
    for i in dict.keys():
        A_list.append(i)
        x=0
        for m in dict[i][x:]:
            A_list.append(m)
        A_list.append("\n")

    for i in A_list:
        if i == "\n":
            A_str=A_str + i
        else:
            A_str=A_str+str(i)+"\t"

    return A_str
# 제품명 센터 섹터 수량 카테고리명 유통기한 (시작 마감) 금액 부피 무게
def U_strTodic(filen) :
    file_CM=open("%s.txt" % filen, "r", encoding="UTF-8")
    Savelist=file_CM.readlines()
    file_CM.close()
    B_list=[]
    filen_dic={}
    for i in Savelist[0:]:
        A_list=[]
        x = i.split("\n")
        del x[-1]
        for m in x:
            y = m.split("\t")
            for n in y:
                if n == "":
                    del n
                else:
                    A_list.append(n)
        B_list.append(A_list)

    for i in B_list :
        filen_dic[i[0]]=i[1:]

    return filen_dic

def U_strTolist(filen) :
    ch_file=open("%s.txt" % filen, "r", encoding="UTF-8")
    Savelist=ch_file.readlines()
    ch_file.close()
    B_list=[]
    for i in Savelist[0:]:
        A_list=[]
        x = i.split("\n")
        del x[-1]
        for m in x:
            y = m.split("\t")
            for n in y:
                if n == "":
                    del n
                else:
                    A_list.append(n)
        B_list.append(A_list)

    return B_list

def catelist() :
    x=U_strTodic('0_category')
    xx=list(x.values())
    xxx=[]
    for i in xx :
        for j in i :
          xxx.append(j)
    return xxx