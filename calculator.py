from tkinter import  *

window =Tk()

window.title("Calculator")
window.geometry("500x500")
window.config(bg="#83838B")

#Entry Box
e=Entry(window , width=65, borderwidth=5)
e.place(x=0 , y=0)

#buttons

def click(num):
     result = e.get()
     e.delete(0,END)
     e.insert(0,result+ str(num))

b=Button(window , text="7", width=12, command=lambda :click(7))
b.place(x=8 , y=60)

b=Button(window , text="8", width=12, command=lambda :click(8))
b.place(x=108 , y=60)

b=Button(window , text="9", width=12, command=lambda :click(9))
b.place(x=208 , y=60)

def subtract():
    n1=e.get()
    global i
    global math
    math = "subtract"
    i=int(n1)
    e.delete(0,END)

b=Button(window , text="/", width=12 ,command=subtract)
b.place(x=308 , y=60)

b=Button(window , text="4", width=12, command=lambda :click(4))
b.place(x=8 , y=120)

b=Button(window , text="5", width=12, command=lambda :click(5))
b.place(x=108 , y=120)

b=Button(window , text="6", width=12, command=lambda :click(6))
b.place(x=208 , y=120)

def division():
    n1=e.get()
    global i
    global math
    math= "division"
    i=int(n1)
    e.delete(0,END)
b=Button(window , text="-", width=12, command=division )
b.place(x=308 , y=120)

b=Button(window , text="1", width=12, command=lambda :click(1))
b.place(x=8 , y=180)

b=Button(window , text="2", width=12, command=lambda :click(2))
b.place(x=108 , y=180)

b=Button(window , text="3", width=12, command=lambda :click(3))
b.place(x=208 , y=180)

def add():
    n1=e.get()
    global i
    global math
    math="add"
    i=int(n1)
    e.delete(0,END)
b=Button(window , text="+", width=12 , command=add)
b.place(x=308 , y=180)

b=Button(window , text="0", width=12, command=lambda :click(0))
b.place(x=8 , y=240)

def clear():
    e.delete(0,END)
b=Button(window , text="clear", width=12 ,command=clear)
b.place(x=108 , y=240)


def multiply():
    n1=e.get()
    global i
    global math
    math="multiply"
    i=int(n1)
    e.delete(0,END)
b=Button(window , text="x", width=12,command=multiply)
b.place(x=308 , y=240)

def equal():
    n2=e.get()
    e.delete(0,END)
    if math == "subtract":
        e.insert(0, i/int(n2))
    elif math == "division":
        e.insert(0, i-int(n2))
    elif math == "add":
        e.insert(0, i+int(n2))
    elif math == "multiply":
        e.insert(0, i*int(n2))


b=Button(window , text="=", width=12,command=equal)
b.place(x=208 , y=240)
mainloop()