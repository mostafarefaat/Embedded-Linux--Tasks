from tkinter import *
import random


def update_gauge():
    newvalue = random.randint(min_reading,max_reading)
    canvas.itemconfig(id_text,text=str(newvalue)+"%")
    angle = 120 * (max_reading-newvalue)/(max_reading-min_reading)+30 # 0% at 150deg and 100% at 30deg 
    canvas.itemconfig(id_needle,start = angle)
    root.after(3000,update_gauge)

root = Tk()
root.title("Gauge APP")
root.geometry("500x500")   

canvas_width = 400
canvas_height = 300

canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.grid(row=2,column=1)

coord = 50,50,350,350 #define the size of the Gauge
min_reading = 0
max_reading = 100

canvas.create_arc(coord,start=30, extent=30,fill="white",outline = "red",width=30,style=ARC)
canvas.create_arc(coord,start=60, extent=50,fill="white",outline = "yellow",width=30,style=ARC)
canvas.create_arc(coord,start=110, extent=20,fill="white",outline = "green",width=30,style=ARC)
canvas.create_arc(coord,start=130, extent=20,fill="white",outline = "blue",width=30,style=ARC)
id_needle = canvas.create_arc(coord,start=119, extent=1,fill="black",width=7)

canvas.create_text(200,20,font = "Times 20 italic bold", text="Humidity")
canvas.create_text(60,140,font = "Times 12 italic bold", text=min_reading)
canvas.create_text(340,140,font = "Times 12 italic bold", text=max_reading)
id_text = canvas.create_text(200,220,font = "Times 15 italic bold")

root.after(3000,update_gauge)

root.mainloop()