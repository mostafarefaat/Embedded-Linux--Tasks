from tkinter import *
import threading

Word = " "
def Button_Handler():
    global Word
    reversed_text.delete("1.0", END) 
    Word = WordVar.get()[::-1]
    reversed_text.insert(END,Word) 
    WordVar.set("")
    
root = Tk()
root.title("Reverse String APP")
root.geometry("300x300")
WordVar = StringVar()
Label(root, text="Enter a Word", font=("Helvetica", 15, "bold"), fg="black").pack(pady=5)
Entry(root, textvariable=WordVar, font=("Helvetica", 15, "bold"), fg="black").pack(pady=5)
Button(root, text="Reverse", font=("Helvetica", 15, "bold"),command=Button_Handler).pack(pady=5)
reversed_text= Text(root,width=30,height=1.5)
reversed_text.pack(pady=5)


root.mainloop()
