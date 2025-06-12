from tkinter import *

root = Tk()

e = Entry(root, width = 50, bg='#F2668B', fg='#011F26',borderwidth=5, font=('Consolas',15))
e.pack() 
e.get()
#e.insert(0,'Entre Your Name: ')

def myclick():
    hello = 'Hello!! '+ e.get().title()
    mylebel = Label(root, text=hello, fg='Red', font=('Consolas',15))
    mylebel.pack()
    
myButton = Button(root, text='Submit',font=('Consolas',15), padx=50, pady=10,command=myclick, fg='Green', bg='Black')
myButton.pack()

root.mainloop() 