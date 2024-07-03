from tkinter import *


def Button_Handler():
    global value
    resut.delete("1.0", END) 
    if(value.get() == 1):
        resut.insert(END,str(Num_1.get()+Num_2.get()))
    elif(value.get() == 2):
        resut.insert(END,str(Num_1.get()-Num_2.get()))
    Num_1.set("")
    Num_2.set("")

    
root = Tk()
root.title("Simple Calculator APP")
root.geometry("300x300")

Num_1 = IntVar()
Num_2 = IntVar()
value = IntVar()

Label(root, text="Enter First Number", font=("Helvetica", 15, "bold"), fg="black").pack(pady=5)
Entry(root, textvariable=Num_1, font=("Helvetica", 15, "bold"), fg="black").pack(pady=5)

Label(root, text="Enter Second Number", font=("Helvetica", 15, "bold"), fg="black").pack(pady=5)
Entry(root, textvariable=Num_2, font=("Helvetica", 15, "bold"), fg="black").pack(pady=5)

Radiobutton(root, text="Sum", variable= value,value=1).pack()
Radiobutton(root, text="Sub", variable= value,value=2).pack()


Button(root, text="Calculate", font=("Helvetica", 15, "bold"),command=Button_Handler).pack(pady=5)

resut= Text(root,width=30,height=1.5)
resut.pack(pady=5)


root.mainloop()
