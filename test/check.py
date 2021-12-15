from tkinter import *

window = Tk()
window_height = 600
window_width = 800
screen_w = window.winfo_screenwidth()
screen_h = window.winfo_screenheight()
pos_x = (screen_w / 2) - (window_width / 2)
pos_y = (screen_h / 2) - (window_height / 2)
window.geometry(f"{window_width}x{window_height}+{int(pos_x)}+{int(pos_y)}")

window.mainloop()