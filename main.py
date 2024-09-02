from tkinter import *
root=Tk()
root.title('calculator jihad')
root.geometry('300x400')
root.resizable(0,0)
root.configure(bg='gray')
e=Entry(root,bd=10,width=30,font='arial 20',bg='blue')

def click(number):
    e.insert(32,number)
    
def add():
    e.insert(32,'+')

def clear():
    e.delete(0,END)

def equal():
    current=e.get()
    list=current.split('+')
    result=int(list[0])+int(list[1])
    clear()
    e.insert(32,result)

e.pack()
btn1=Button(root,text='7',font='arial 19 bold',bg='red',bd='10',padx='10',pady='5',command=lambda:click(7))
btn1.place(x=10,y=60)
btn2=Button(root,text='8',font='arial 19 bold',bg='red',bd='10',padx='10',pady='5',command=lambda:click(8))
btn2.place(x=85,y=60)
btn3=Button(root,text='9',font='arial 19 bold',bg='red',bd='10',padx='10',pady='5',command=lambda:click(9))
btn3.place(x=160,y=60)
btn4=Button(root,text='4',font='arial 19 bold',bg='red',bd='10',padx='10',pady='5',command=lambda:click(4))
btn4.place(x=10,y=145)
btn5=Button(root,text='5',font='arial 19 bold',bg='red',bd='10',padx='10',pady='5',command=lambda:click(5))
btn5.place(x=85,y=145)
btn6=Button(root,text='6',font='arial 19 bold',bg='red',bd='10',padx='10',pady='5',command=lambda:click(6))
btn6.place(x=160,y=145)
btn7=Button(root,text='1',font='arial 19 bold',bg='red',bd='10',padx='10',pady='5',command=lambda:click(1))
btn7.place(x=10,y=230)
btn8=Button(root,text='2',font='arial 19 bold',bg='red',bd='10',padx='10',pady='5',command=lambda:click(2))
btn8.place(x=85,y=230)
btn9=Button(root,text='3',font='arial 19 bold',bg='red',bd='10',padx='10',pady='5',command=lambda:click(3))
btn9.place(x=160,y=230)
btn0=Button(root,text='0',font='arial 19 bold',bg='red',bd='10',padx='10',pady='5',command=lambda:click(0))
btn0.place(x=10,y=320)

btn11=Button(root,text='+',font='arial 19 bold',bg='skyBlue',bd='10', height='1',command=add)
btn11.place(x=235,y=60)

btnC=Button(root,text='C',font='arial 19 bold', height='1' , bg='skyBlue',bd='10',command=clear)
btnC.place(x=235,y=230)

btnequl=Button(root,text='=',font='arial 19 bold',height='1' , bg='skyBlue',bd='10',command=equal)
btnequl.place(x=235,y=145)


root.mainloop()
