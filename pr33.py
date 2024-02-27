import tkinter as tk
import random

def move_circle():
    x = random.randint(0, 400)  
    y = random.randint(0, 400)  
    canvas.coords(circle, x, y, x+50, y+50)  

root = tk.Tk()
root.title("Анимация круга")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

circle = canvas.create_oval(0, 0, 50, 50, fill="blue")  

button = tk.Button(root, text="Кружим круг!!!", command=move_circle)
button.pack()

root.mainloop()