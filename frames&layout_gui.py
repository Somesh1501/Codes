from tkinter import  *
win = Tk()
#frames
topFrame = Frame(win)
topFrame.pack()
bottomFram = Frame(win)
bottomFram.pack(side ="bottom")
#buttons
button1 = Button(topFrame, text="Button1", fg="pink", bg="black", font="Amita")
button2 = Button(topFrame, text="Button2", fg="indigo",bg='red', font="Amita")
button3 = Button(topFrame, text="Button3", fg="cyan", bg='blue',font="Amita")
button4 = Button(bottomFram, text="Button4", fg="red", bg= 'green',font="Amita")

button1.pack(side='right')
button2.pack(side='left')
button3.pack()
button4.pack()
win.mainloop()
