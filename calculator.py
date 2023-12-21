import tkinter
from tkinter import *

root=Tk()
root.title("simple Calculator")
root.geometry("370x550+100+200")
root.resizable(False,False)
root.configure(bg="#17161b")

equation = ""

def show(value):
    global equation
    equation+=value
    Label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    Label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation!="":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    Label_result.config(text=result)
            


Label_result=Label(root,width=25,height=2,text="",font=("arial",30))
Label_result.pack()

Button(root,text="C",width=3,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#3697f5",command=lambda: clear()).place(x=10,y=100)
Button(root,text="(",width=3,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("(")).place(x=100,y=100)
Button(root,text=")",width=3,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show(")")).place(x=190,y=100)
Button(root,text="%",width=3,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("%")).place(x=280,y=100)

Button(root,text="7",width=3,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("7")).place(x=10,y=190)
Button(root,text="8",width=3,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("8")).place(x=100,y=190)
Button(root,text="9",width=3,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("9")).place(x=190,y=190)
Button(root,text="/",width=3,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("/")).place(x=280,y=190)

Button(root,text="4",width=3,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("4")).place(x=10,y=280)
Button(root,text="5",width=3,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("5")).place(x=100,y=280)
Button(root,text="6",width=3,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("6")).place(x=190,y=280)
Button(root,text="*",width=3,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("*")).place(x=280,y=280)

Button(root,text="1",width=3,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("1")).place(x=10,y=370)
Button(root,text="2",width=3,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("2")).place(x=100,y=370)
Button(root,text="3",width=3,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("3")).place(x=190,y=370)
Button(root,text="+",width=3,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("+")).place(x=280,y=370)

Button(root,text="-",width=3,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("-")).place(x=10,y=460)
Button(root,text="0",width=3,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("0")).place(x=100,y=460)
Button(root,text=".",width=3,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: show(".")).place(x=190,y=460)
Button(root,text="=",width=3,height=1, font=("arial",30,"bold"), bd=1,fg="#fff",bg="#2a2d36",command=lambda: calculate()).place(x=280,y=460)



root.mainloop()
