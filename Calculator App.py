from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.configure(bg="#000000")
root.title("Simple Calculator")

e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=1,columnspan=3,padx=10,pady=10)

def button_add():
    return

# Define Button

button_1 = Button(root, text="1", padx=40, pady=20, command=button_add,bg="#1BF90F")
button_2 = Button(root, text="2", padx=40, pady=20, command=button_add,bg="#1BF90F") 
button_3 = Button(root, text="3", padx=40, pady=20, command=button_add,bg="#1BF90F") 
button_4 = Button(root, text="4", padx=40, pady=20, command=button_add,bg="#1BF90F") 
button_5 = Button(root, text="5", padx=40, pady=20, command=button_add,bg="#1BF90F") 
button_6 = Button(root, text="6", padx=40, pady=20, command=button_add,bg="#1BF90F") 
button_7 = Button(root, text="7", padx=40, pady=20, command=button_add,bg="#1BF90F") 
button_8 = Button(root, text="8", padx=40, pady=20, command=button_add,bg="#1BF90F")   
button_9 = Button(root, text="9", padx=40, pady=20, command=button_add,bg="#1BF90F")     
button_0 = Button(root, text="0", padx=40, pady=20, command=button_add,bg="#1BF90F")  
button_sum = Button(root, text="+", padx=39, pady=19, command=button_add, bg="#1BF90F")
button_equal = Button(root, text="=", padx=39, pady=20, command=button_add, bg="#1BF90F")
button_clear = Button(root, text="Clear", padx=30, pady=20, command=button_add, bg="#1BF90F")
# Put Button On The Screen 

button_1.grid(row=3,column=1)
button_2.grid(row=3,column=2)
button_3.grid(row=3,column=3)

button_4.grid(row=2,column=1)
button_5.grid(row=2,column=2)
button_6.grid(row=2,column=3)

button_7.grid(row=1,column=1)
button_8.grid(row=1,column=2)
button_9.grid(row=1,column=3)

button_0.grid(row=4,column=2)
button_sum.grid(row=1,column=4)
button_clear.grid(row=4,column=1)
button_equal.grid(row=4,column=3)

root.mainloop()


    
