import tkinter

window= tkinter.Tk()
window.geometry("300x300")
window.bg="yellow"

sonuc= tkinter.Label(text="Title:",bg="gray")
sonuc['font'] = "Verdana 12 bold"
sonuc['fg'] = "#FFAABB"
sonuc.place(x=180,y=20)

window.mainloop()