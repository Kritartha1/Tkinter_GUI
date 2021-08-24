from tkinter import *
root=Tk()
root.title("Simple calculator")

e=Entry(root,width=35,borderwidth=5)#input field
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

#e.insert(0,"Enter your name: ") #text pre-existing in the input box
def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def button_clear():
    e.delete(0,END)
def button_add():
    first_number=e.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_number)
    e.delete(0,END)
def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if(math=="addition"):
        e.insert(0,f_num+int(second_number))
    if (math == "subtraction"):
        e.insert(0, f_num - int(second_number))
    if (math == "multiplication"):
        e.insert(0, f_num * int(second_number))
    if (math == "division"):
        e.insert(0, f_num / int(second_number))
def button_substract():
    first_number = e.get()
    global f_num
    global math
    math = "substraction"
    f_num = float(first_number)
    e.delete(0, END)
def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)
def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)
button_1=Button(root,text="1",command=lambda:button_click(1),padx=40,pady=20)
button_2=Button(root,text="2",command=lambda:button_click(2),padx=40,pady=20)
button_3=Button(root,text="3",command=lambda:button_click(3),padx=40,pady=20)
button_4=Button(root,text="4",command=lambda:button_click(4),padx=40,pady=20)
button_5=Button(root,text="5",command=lambda:button_click(5),padx=40,pady=20)
button_6=Button(root,text="6",command=lambda:button_click(6),padx=40,pady=20)
button_7=Button(root,text="7",command=lambda:button_click(7),padx=40,pady=20)
button_8=Button(root,text="8",command=lambda:button_click(8),padx=40,pady=20)
button_9=Button(root,text="9",command=lambda:button_click(9),padx=40,pady=20)
button_0=Button(root,text="0",command=lambda:button_click(0),padx=40,pady=20)
button_add=Button(root,text="+",command=button_add,padx=39,pady=20)
button_equal=Button(root,text="=",command=button_equal,padx=91,pady=20)
button_clear=Button(root,text="Clear",command=button_clear,padx=79,pady=20)

button_substract=Button(root,text="-",command=button_substract,padx=41,pady=20)
button_multiply=Button(root,text="*",command=button_multiply,padx=40,pady=20)
button_divide=Button(root,text="/",command=button_divide,padx=41,pady=20)

#put buttons on the screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)
button_clear.grid(row=4,column=1,columnspan=2)

button_substract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)







root.mainloop()





