import pyperclip3 as pc
import tkinter
import random
import string
from PIL import Image,ImageTk

def button_command(lenlenofpass):
    def passwordgenerator(lenlenofpass) :
        options = list(string.ascii_letters + string.digits + "!@#$%^&*()")

        password = []
        for i in range(0,lenlenofpass):
            password.append(random.choice(options))
    
        random.shuffle(password)
        result=("".join(password))
        return result
    
    passwordgenerator(lenlenofpass)
    
    l2=tkinter.Text(window,height=2,width=20,fg='White',bg='black')
    l2.insert(tkinter.INSERT,passwordgenerator(lenlenofpass))
    l2.configure(state="disabled")
    l2.place(x=150,y=80)



window=tkinter.Tk()
window.geometry("400x200")

head_image=Image.open("head_image.jpg")
myimg=ImageTk.PhotoImage(head_image)
image_label=tkinter.Label(window,image=myimg,height=200,width=200)
image_label.place(x=0,y=0,relheight=1,relwidth=1)
l1=tkinter.Label(window,text="Enter length of password :",fg='white',bg='black')
l1.place(x=25,y=40)
len = tkinter.Entry(window,width = 4)
len.place(x=170,y=42)
b1=tkinter.Button(window,text="Submit",command=lambda: button_command(int(len.get())),width=5,height=1)
b1.place(x=205,y=40)
l3=tkinter.Label(window,text='Suggeseted Password :',fg='white',bg='black')
l3.place(x=25,y=80)

window.mainloop()
