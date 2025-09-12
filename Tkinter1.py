# import tkinter as tk
# import time

# def update_time():
#     label.config(text=time.strftime("%H:%M:%S\n%d-%m-%Y"))
#     root.after(1000, update_time)

# root = tk.Tk()
# root.title("Digital Clock")
# label = tk.Label(root, font=("Arial", 24),bg="red",fg="white",width=20,height=10)
# label.pack()
# update_time()
# root.mainloop()


import tkinter as tk

def paint(event):
    x1, y1 = (event.x-2), (event.y-2)
    x2, y2 = (event.x+2), (event.y+2)
    canvas.create_oval(x1, y1, x2, y2, fill="red")

root = tk.Tk()
root.title("Paint App")
canvas = tk.Canvas(root, bg="white", width=400, height=300)
canvas.pack()
canvas.bind("<B1-Motion>", paint)
root.mainloop()





