import tkinter
import tkintermapview

ex = tkinter.Tk()
ex.geometry('900x900')

clinic = '쿨펫동물병원'
city = '대전'
map = tkintermapview.TkinterMapView(ex, width=500, height=500, corner_radius=0)
map.pack(anchor='center')
map.set_address(f"{clinic},{city}", marker=True)

ex.mainloop()