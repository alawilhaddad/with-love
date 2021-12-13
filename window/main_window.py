from window.properties import Win
from tkinter import *
from window.controller import *


class Main:
    def __init__(self, root, window_height=600, window_width=800):
        # Configure main window properties
        self.root = root
        self.screen_w = window.winfo_screenwidth()
        self.screen_h = window.winfo_screenheight()
        self.pos_x = (self.screen_w / 2) - (window_width / 2)
        self.pos_y = (self.screen_h / 2) - (window_height / 2)
        self.root.geometry(f"{window_width}x{window_height}+{int(self.pos_x)}+{int(self.pos_y)}")

        # Set background
        self.canvas = Canvas(
            self.root,
            bg="#ffffff",
            height=600,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)
        self.background_img = PhotoImage(file=f"img/background.png")
        self.background = self.canvas.create_image(
            400.0, 300.0,
            image=self.background_img)

        # Set copyright and versioning
        self.canvas.create_text(
            603.0, 556.0,
            text="Haddaddegusti 2021 | v. 2.0.0",
            fill="#232325",
            anchor="nw",
            font=("Montserrat-Thin", 9))

        # Initialize close button
        self.close_img = PhotoImage(file=f"img/close_img.png")
        self.close_button = Button(
            image=self.close_img,
            borderwidth=0,
            highlightthickness=0,
            command=quit_app,
            relief="flat")
        self.close_button.place(
            x=755, y=25,
            width=20,
            height=20)

        # Menu Bar =====================================================================================================

        # Initialize home button
        self.home_img = PhotoImage(file=f"img/home_img.png")
        self.home_button = Button(
            image=self.home_img,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")
        self.home_button.place(
            x=25, y=25,
            width=120,
            height=120)

        # Initialize countdown button
        self.countdown_img = PhotoImage(file=f"img/countdown_img.png")
        self.countdown_button = Button(
            image=self.countdown_img,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")
        self.countdown_button.place(
            x=170, y=25,
            width=120,
            height=120)

        # Initialize this or that button
        self.this_that_img = PhotoImage(file=f"img/this_that_img.png")
        self.this_that_button = Button(
            image=self.this_that_img,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")
        self.this_that_button.place(
            x=25, y=168,
            width=120,
            height=120)

        # Initialize random button
        self.random_img = PhotoImage(file=f"img/random_img.png")
        self.random_button = Button(
            image=self.random_img,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")
        self.random_button.place(
            x=170, y=168,
            width=120,
            height=120)

        # Initialize mail button
        self.mail_img = PhotoImage(file=f"img/mail_img.png")
        self.mail_button = Button(
            image=self.mail_img,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")
        self.mail_button.place(
            x=25, y=311,
            width=120,
            height=120)

        # Initialize setting button
        self.setting_img = PhotoImage(file=f"img/setting_img.png")
        self.setting_button = Button(
            image=self.setting_img,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")
        self.setting_button.place(
            x=170, y=311,
            width=120,
            height=120)

        # Initialize call button
        self.call_img = PhotoImage(file=f"img/call_img.png")
        self.call_button = Button(
            image=self.call_img,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")
        self.call_button.place(
            x=25, y=454,
            width=120,
            height=120)

        # Initialize guide button
        self.guide_img = PhotoImage(file=f"img/guide_img.png")
        self.guide_button = Button(
            image=self.guide_img,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")
        self.guide_button.place(
            x=170, y=454,
            width=120,
            height=120)


class Home:
    def __init__(self, canvas):
        self.canvas = canvas
        self.home_title_img = PhotoImage(file=f"img/home_title_img.png")

    def show(self):
        self.canvas.create_image(
            365, 243,
            anchor="nw",
            image=self.home_title_img,
            tags="home")

    def hide(self):
        self.canvas.delete("home")


# class Count:
#     def __init__(self):
#
def btn_clicked():
    print("clicked")


if __name__ == "__main__":
    window = Win()
    main = Main(window)
    home = Home(main.canvas)
    home.show()
    window.mainloop()
