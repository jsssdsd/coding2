import Module_SelectCar as sc
def InsuranceCal(age, car):
    global listc
    global listm
    listc=[]
    listm=[]
    for i in sc.list_3:
        listc.append(i[0])
        listm.append(i[3])
    inputcarsmoney=listm[listc.index(car)]
    print(inputcarsmoney)
    Insurance=round((float(inputcarsmoney)*0.03)*10000)
    if 24<=int(age)<26:
        resul_insu=round(Insurance+(float(Insurance*0.3)))
        return resul_insu
    elif 24>int(age):
        resul_insu = round(Insurance + (float(Insurance * 0.8)))
        return resul_insu
    else:
        return Insurance






