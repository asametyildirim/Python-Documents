import tkinter

window= tkinter.Tk()
window.geometry("300x300")
window.bg="yellow"

txt_url=StringVar()
input1 = Entry(window,textvariable = txt_url, font=('calibre',10,'normal'))
input1.place(relx=0.25, rely=0.255,relwidth=0.6)

def start():
   print(txt_url.get())

button1 = Button(window, text ="Button", command = start)
button1.place(relx=0.9, rely=0.25,relwidth=0.1)

window.mainloop()