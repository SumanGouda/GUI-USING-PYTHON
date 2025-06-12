from tkinter import *

root = Tk()

#Creating the button

def myclick():
    mylebel = Label(root, text='Look! I clicked a Button!!',fg='Red')
    mylebel.pack()
    
myButton = Button(root, text='Click Me!', padx=50, pady=10,command=myclick, fg='Blue', bg='Black')
myButton.pack()

root.mainloop()