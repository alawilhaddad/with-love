from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("800x600")
window.configure(bg="#ffffff")
canvas = Canvas(
    window,
    bg="#ffffff",
    height=600,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=f"img/background.png")
background = canvas.create_image(
    400.0, 300.0,
    image=background_img)

canvas.create_text(
    603.0, 556.0,
    text="Haddaddegusti 2021 | v. 2.0.0",
    fill="#232325",
    anchor="nw",
    font=("Montserrat-Regular", 9))

close_img = PhotoImage(file=f"img/close_img.png")
close_button = Button(
    image=close_img,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

close_button.place(
    x=755, y=25,
    width=20,
    height=20)

guide_img = PhotoImage(file=f"img/guide_img.png")
guide_button = Button(
    image=guide_img,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

guide_button.place(
    x=170, y=454,
    width=120,
    height=120)

call_img = PhotoImage(file=f"img/call_img.png")
call_button = Button(
    image=call_img,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

call_button.place(
    x=25, y=454,
    width=120,
    height=120)

setting_img = PhotoImage(file=f"img/setting_img.png")
setting_button = Button(
    image=setting_img,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

setting_button.place(
    x=170, y=311,
    width=120,
    height=120)

mail_img = PhotoImage(file=f"img/mail_img.png")
mail_button = Button(
    image=mail_img,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

mail_button.place(
    x=25, y=311,
    width=120,
    height=120)

random_img = PhotoImage(file=f"img/random_img.png")
random_button = Button(
    image=random_img,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

random_button.place(
    x=170, y=168,
    width=120,
    height=120)

this_that_img = PhotoImage(file=f"img/this_that_img.png")
this_that_button = Button(
    image=this_that_img,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

this_that_button.place(
    x=25, y=168,
    width=120,
    height=120)

countdown_img = PhotoImage(file=f"img/countdown_img.png")
countdown_button = Button(
    image=countdown_img,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

countdown_button.place(
    x=170, y=25,
    width=120,
    height=120)

home_img = PhotoImage(file=f"img/home_img.png")
home_button = Button(
    image=home_img,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

home_button.place(
    x=25, y=25,
    width=120,
    height=120)
# =================================================================================================================
home_title_img = PhotoImage(file=f"img/home_title_img.png")
canvas.create_image(
        365, 243,
        anchor="nw",
        image=home_title_img,
        tags="home")

window.resizable(False, False)
window.mainloop()
