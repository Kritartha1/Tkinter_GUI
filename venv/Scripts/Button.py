from tkinter import *
root=Tk()
e=Entry(root,width=50,bg="white",fg="blue")#input field
e.pack()
e.get()
e.insert(0,"Enter your name: ") #text pre-existing in the input box

def myClick():
    hello="Hello! "+e.get()
    myLabel=Label(root,text=hello)
    myLabel.pack()

myButton=Button(root,text="Enter your name!",command=myClick,fg="blue",bg="red")#button enabled
#myButton=Button(root,text="Click me!",state="disabled",command=myClick,fg="blue",bg="red")#button disabled
#fg:foreground color
#bg:background color
myButton.pack()


root.mainloop()





