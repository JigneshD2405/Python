'''from tkinter import *
Jignesh=Tk()

Jignesh.title("Tkinter2405")
Jignesh.geometry("500x500")
#Jignesh.config(bg="Green")

frame1=Frame(Jignesh,bg="Blue" ,width=500 ,height=50 , cursor="dot")
frame2=Frame(Jignesh ,bg="Green",width=500 ,height=50)
button1=Button(frame1,text="Button1",bg="Yellow" )
button2=Button(frame1,text="LogOut",fg="red")
button1.pack()
button2.pack()
#inp=Label(Jignesh,text="Hello Jignesh")
#inp.pack()
frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)

Jignesh.mainloop()




from  tkinter import *
from tkinter import Tk

Windows =Tk()

lable1=Label(Windows, text="Email" )
lable2=Label(Windows,text="Password")

e1=Entry(Windows , width=30 , borderwidth=5)
e2=Entry(Windows, width=30,borderwidth=5)

lable1.grid(row=0 , column=1)
lable2.grid(row=1,column=1)
e1.grid(row=0 ,column=2)
e2.grid(row=1,column=2)



from tkinter import *
window =Tk()
window.title("Learning Tkinter")
window.geometry("500x500")


def login():
    print("Loged In")

button1 = Button(window ,width="10" ,text="Login" , bg="Green" ,fg="white",command=login, font=("bold",12),activebackground="red",activeforeground="white")
button1.pack()

mainloop()



from tkinter import *
from turtle import width

window=Tk()

window.title("Learning Tkinter")
window.geometry("500x600")
window.config(bg="#83838B")
#frame1=Frame(window , borderwidth=5 ,width="500" ,height="100")
#frame1.pack()

menu=Menu(window)
jignesh=Menu(menu,tearoff=1)
jignesh.add_command(label="New Project")
jignesh.add_command(label="New")
jignesh.add_command(label="open")
jignesh.add_command(label="save")
jignesh.add_command(label="save as")
jignesh.add_separator()
jignesh.add_command(label="Exit" ,command=window.quit())

menu.add_cascade(label="File" ,menu= jignesh)
window.config(menu = menu)



from tkinter import *
import  tkinter.messagebox

window = Tk()

#tkinter.messagebox.showinfo("Info" ,"Running Out Time")
question=tkinter.messagebox.askyesno("weather", "will It rain?")

if question == True:
    print("Take Umbrella")
else:
    print("okey")

mainloop()


from tkinter import *

window =Tk()


c=Canvas(window ,width=500,height=500)
c.pack()

#c.create_arc(0,150,150,150)
c.create_line(0,0,250,250, width=5)


mainloop()



from tkinter import *

window = Tk()


#message =Message(window , text="Hii"   , padx=50 ,pady=50)
#message.pack()

var=StringVar()
entry_var=StringVar()

def insert():
    result=entry_var.get()
    var.set(result)

message=Message(window , textvariable= var ,relief=RAISED ,padx=50,pady=50)
entry=Entry(window , textvariable=entry_var )
button=Button(window , text="Ok" , command= insert)



message.pack()
entry.pack()
button.pack()

mainloop()
'''

from tkinter import *

window =Tk()

chk_box1=IntVar()
chk_box2=IntVar()
chk_box3=IntVar()

chk_box1=Checkbutton(window, text="apple" , height=2 ,width=10,onvalue=1,offvalue=0)
chk_box2=Checkbutton(window, text="apple" , height=2 ,width=10,onvalue=1,offvalue=0)
chk_box3=Checkbutton(window, text="apple" , height=2 ,width=10,onvalue=1,offvalue=0)


chk_box1.pack()
chk_box2.pack()
chk_box3.pack()


mainloop()




































