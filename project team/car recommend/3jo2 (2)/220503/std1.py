


try:
    for i in range(len(CARlist)):
        labelnum = tk.Label(frame3, text="%d." % (i + 1))
        if len(CARlist) > 12:
            if i > 12:
                labelnum.grid(row=7 + (i - 13), column=2, sticky="w")
            else:
                labelnum.grid(row=7 + i, column=0, sticky="w")
        else:
            labelnum.grid(row=7 + i, column=0, sticky="w")
        globals()["btn_{}".format(i)] = tk.Button(frame3, text=CARlist[i], command=partial(resultpage, CARlist[i]))  #
        if len(CARlist) > 12:
            if i > 12:
                globals()["btn_{}".format(i)].grid(row=7 + (i - 13), column=3, sticky="w", padx=10, pady=10)
            else:
                globals()["btn_{}".format(i)].grid(row=7 + i, column=1, sticky="w", padx=10, pady=10)
        else:
            globals()["btn_{}".format(i)].grid(row=7 + i, column=1, sticky="w", padx=10, pady=10)
except UnboundLocalError:
    ResultViewlabel_ViewLabel.config(text="숫자가 아닙니다. 다시 입력해주세요.")
    txt1.delete(0, "end")
    txt2.delete(0, "end")
    txt3.delete(0, "end")
    txt4.delete(0, "end")