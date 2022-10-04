from tkinter import *

calc=Tk()
calc.geometry("400x500")
calc.title("CALCULATOR BY CJ")
calclabel = Label(calc,text="CALCULATOR",bg='White',font=("Times",30,'bold'))
calclabel.pack(side=TOP)
calc.config(background='#1f2943')

textin=StringVar()
operator=""

def clickbut(number):  
     global operator
     operator=operator+str(number)
     textin.set(operator)

def equlbut():
     global operator
     add=str(eval(operator))
     textin.set(add)
     operator=''

def equlbut():
     global operator
     sub=str(eval(operator))
     textin.set(sub)
     operator=''

def equlbut():
     global operator
     mul=str(eval(operator))
     textin.set(mul)
     operator=''

def equlbut():
     global operator
     div=str(eval(operator))
     textin.set(div)
     operator=''    

def clrbut():
     textin.set('')

     
metext=Entry(calc,font=("Courier New",12,'bold'),textvar=textin,width=25,bd=3,bg='powder blue')
metext.pack()

but1=Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(1),text="1",font=("Courier New",16,'bold'))
but1.place(x=30,y=100)

but2=Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(2),text="2",font=("Courier New",16,'bold'))
but2.place(x=30,y=170)

but3=Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(3),text="3",font=("Courier New",16,'bold'))
but3.place(x=30,y=240)

but4=Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(4),text="4",font=("Courier New",16,'bold'))
but4.place(x=95,y=100)

but5=Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(5),text="5",font=("Courier New",16,'bold'))
but5.place(x=95,y=170)

but6=Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(6),text="6",font=("Courier New",16,'bold'))
but6.place(x=95,y=240)

but7=Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(7),text="7",font=("Courier New",16,'bold'))
but7.place(x=160,y=100)

but8=Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(8),text="8",font=("Courier New",16,'bold'))
but8.place(x=160,y=170)

but9=Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(9),text="9",font=("Courier New",16,'bold'))
but9.place(x=160,y=240)

but0=Button(calc,padx=14,pady=14,bd=4,bg='white',command=lambda:clickbut(0),text="0",font=("Courier New",16,'bold'))
but0.place(x=30,y=310)

butdot=Button(calc,padx=47,pady=14,bd=4,bg='white',command=lambda:clickbut("."),text=".",font=("Courier New",16,'bold'))
butdot.place(x=95,y=310)

butpl=Button(calc,padx=14,pady=14,bd=4,bg='white',text="+",command=lambda:clickbut("+"),font=("Courier New",16,'bold'))
butpl.place(x=225,y=100)

butsub=Button(calc,padx=14,pady=14,bd=4,bg='white',text="-",command=lambda:clickbut("-"),font=("Courier New",16,'bold'))
butsub.place(x=225,y=170)

butml=Button(calc,padx=14,pady=14,bd=4,bg='white',text="*",command=lambda:clickbut("*"),font=("Courier New",16,'bold'))
butml.place(x=225,y=240)

butdiv=Button(calc,padx=14,pady=14,bd=4,bg='white',text="/",command=lambda:clickbut("/"),font=("Courier New",16,'bold'))
butdiv.place(x=225,y=310)

butclear=Button(calc,padx=14,pady=119,bd=4,bg='white',text="CE",command=clrbut,font=("Courier New",16,'bold'))
butclear.place(x=290,y=100)

butequal=Button(calc,padx=151,pady=14,bd=4,bg='white',command=equlbut,text="=",font=("Courier New",16,'bold'))
butequal.place(x=30,y=380)

calc.mainloop()

