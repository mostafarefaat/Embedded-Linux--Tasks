from tkinter import *
import threading


def Button_Handler():
    global value
    resut.delete("1.0", END) 
    fact = 1
    for i in range(1,Num_1.get()+1):
        fact *= i

    resut.insert(END,str(fact))
    Num_1.set("")

root = Tk()
root.title("Factorial APP")
root.geometry("300x300")

Num_1 = IntVar()


Label(root, text="Enter Number", font=("Helvetica", 15, "bold"), fg="black").pack(pady=5)
Entry(root, textvariable=Num_1, font=("Helvetica", 15, "bold"), fg="black").pack(pady=5)

Button(root, text="Calculate", font=("Helvetica", 15, "bold"),command=Button_Handler).pack(pady=5)

resut= Text(root,width=30,height=1.5)
resut.pack(pady=5)


root.mainloop()
