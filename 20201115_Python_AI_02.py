# -*- coding: utf-8 -*-

from tkinter import *

c_height = 200
c_width = 300
c_color = "black"

pen_x = c_width/2
pen_y = c_height

window = Tk()
window.title("My Canvas")

c = Canvas(bg = c_color, height = c_height, width = c_width)
c.pack()

label = Label(window, text = "My Canvas")
label.pack()

def pen_move_up(event):
    global pen_y
    # [].create_line(시작x위치, 시작 y위치, 끝x위치, 끝y위치, 선의 굵기, 선의 색깔)
    c.create_line(pen_x, pen_y, pen_x, pen_y-5, width = 5, fill = "green")
    pen_y -= 5
    
def Canvas_Clear(event):
    c.delete("all")

    
window.bind("<Up>", pen_move_up)
window.bind("<Delete>", Canvas_Clear)

### key
### https://076923.github.io/posts/Python-tkinter-23/

window.mainloop()