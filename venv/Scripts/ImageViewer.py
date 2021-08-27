from tkinter import *

from PIL import ImageTk,Image

root=Tk()

root.title("Kritartha")
root.iconbitmap("C:/Users/Krita/Downloads/greenhouse_conservatory_plant_ecology_garden_icon_191960.ico")

my_img1=ImageTk.PhotoImage(Image.open("Image/1.jpg"))
my_img2=ImageTk.PhotoImage(Image.open("Image/2.jpg"))
my_img3=ImageTk.PhotoImage(Image.open("Image/3.jpg"))
my_img4=ImageTk.PhotoImage(Image.open("Image/4.jpg"))
my_img5=ImageTk.PhotoImage(Image.open("Image/5.jpg"))

image_list=[my_img1,my_img2,my_img3,my_img4,my_img5]
status=Label(root,text="Image 1 of "+str(len(image_list)),bd=1,relief=SUNKEN, anchor=E)
#bd:border
my_label=Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()

    my_label=Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))

    button_back = Button(root, text="<<", command=lambda :back(image_number-1))

    if image_number==5:
        button_forward=Button(root,text=">>",state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)

    button_back.grid(row=1, column=0, padx=40, pady=0.1)
    button_forward.grid(row=1, column=2, padx=40, pady=0.1)

    status = Label(root, text="Image "+str(image_number)+" of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)
def back(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()# it deletes the previous image and make space for the next image

    my_label = Label(image=image_list[image_number - 1])#since, 0 indexed
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))

    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)

    button_back.grid(row=1, column=0, padx=40, pady=0.1)
    button_forward.grid(row=1, column=2, padx=40, pady=0.1)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN,
                   anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


button_back=Button(root,text="<<",command=back)
button_exit=Button(root,text="EXIT PROGRAM",command=root.quit)
button_forward=Button(root,text=">>", command=lambda:forward(2))

button_back.grid(row=1,column=0,padx=40,pady=0.1)
button_exit.grid(row=1,column=1,padx=40,pady=0.1)
button_forward.grid(row=1,column=2,padx=40,pady=0.1)

status.grid(row=2,column=0,columnspan=3,sticky=W+E)




root.mainloop()