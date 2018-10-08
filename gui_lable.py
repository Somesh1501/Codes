from tkinter import  *
win = Tk()
win.geometry("200x200")
rLabel = Label(win,text="Red",  bg="green",)
rLabel.pack()

bLabel = Label(win,text="blue", bg="white")
bLabel.pack()

gLabel = Label(win,text="green", bg="red")
gLabel.pack(fill=X)
win.mainloop()
