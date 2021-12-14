from tkinter import *
from win.controller import *
from tkcalendar import *


class Main:
    def __init__(self, root, window_height=600, window_width=800):
        # Configure main window properties
        self.root = root
        self.screen_w = root.winfo_screenwidth()
        self.screen_h = root.winfo_screenheight()
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
        self.background_img = PhotoImage(file=f"win/img/background.png")
        self.background = self.canvas.create_image(
            400.0, 300.0,
            image=self.background_img)

        # Set copyright and versioning
        self.canvas.create_text(
            594.0, 566.0,
            text="Haddaddegusti 2021 | v. 2.0.0",
            fill="#232325",
            anchor="nw",
            font=("Montserrat-Regular", 9))

        # Initialize close button
        self.close_img = PhotoImage(file=f"win/img/close_img.png")
        self.close_button = Button(
            image=self.close_img,
            borderwidth=0,
            highlightthickness=0,
            command=quit_app,
            relief="flat")
        self.close_button.place(
            x=750, y=25,
            width=20,
            height=20)

        # Menu Bar =====================================================================================================

        # Initialize home button
        self.home_img = PhotoImage(file=f"win/img/home_img.png")
        self.home_button = Button(
            image=self.home_img,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#232325",
            command=btn_clicked,
            relief="flat")
        self.home_button.place(
            x=25, y=25,
            width=120,
            height=120)

        # Initialize countdown button
        self.countdown_img = PhotoImage(file=f"win/img/countdown_img.png")
        self.countdown_button = Button(
            image=self.countdown_img,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#232325",
            command=btn_clicked,
            relief="flat")
        self.countdown_button.place(
            x=170, y=25,
            width=120,
            height=120)

        # Initialize this or that button
        self.this_that_img = PhotoImage(file=f"win/img/this_that_img.png")
        self.this_that_button = Button(
            image=self.this_that_img,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#232325",
            command=btn_clicked,
            relief="flat")
        self.this_that_button.place(
            x=25, y=170,
            width=120,
            height=120)

        # Initialize random button
        self.random_img = PhotoImage(file=f"win/img/random_img.png")
        self.random_button = Button(
            image=self.random_img,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#232325",
            command=btn_clicked,
            relief="flat")
        self.random_button.place(
            x=170, y=170,
            width=120,
            height=120)

        # Initialize mail button
        self.mail_img = PhotoImage(file=f"win/img/mail_img.png")
        self.mail_button = Button(
            image=self.mail_img,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#232325",
            command=btn_clicked,
            relief="flat")
        self.mail_button.place(
            x=25, y=315,
            width=120,
            height=120)

        # Initialize setting button
        self.setting_img = PhotoImage(file=f"win/img/setting_img.png")
        self.setting_button = Button(
            image=self.setting_img,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#232325",
            command=btn_clicked,
            relief="flat")
        self.setting_button.place(
            x=170, y=315,
            width=120,
            height=120)

        # Initialize call button
        self.call_img = PhotoImage(file=f"win/img/call_img.png")
        self.call_button = Button(
            image=self.call_img,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#232325",
            command=btn_clicked,
            relief="flat")
        self.call_button.place(
            x=25, y=460,
            width=120,
            height=120)

        # Initialize guide button
        self.guide_img = PhotoImage(file=f"win/img/guide_img.png")
        self.guide_button = Button(
            image=self.guide_img,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#232325",
            command=btn_clicked,
            relief="flat")
        self.guide_button.place(
            x=170, y=460,
            width=120,
            height=120)


class Home:
    def __init__(self, canvas):
        self.canvas = canvas
        self.home_title_img = PhotoImage(file=f"win/img/home_title_img.png")

    def show(self):
        self.canvas.create_image(
            375, 168,
            anchor="nw",
            image=self.home_title_img,
            tags="home")

    def hide(self):
        self.canvas.delete("home")


class Countdown:
    def __init__(self, canvas):
        self.canvas = canvas
        self.border_img = PhotoImage(file=f"win/img/border_countdown.png")

    def show(self):
        self.canvas.create_image(
            365, 378,
            anchor="nw",
            image=self.border_img,
            tags="countdown")

        self.canvas.create_text(
            375, 95,
            text="Waiting time:",
            fill="#232325",
            anchor="nw",
            font=("Montserrat-Medium", 27),
            tags="countdown")

        self.canvas.create_text(
            550, 145,
            text="100 Hari",
            fill="#232325",
            anchor="n",
            font=("Montserrat-Regular", 60),
            tags="countdown")

        self.canvas.create_text(
            550, 225,
            text="06:04:11",
            fill="#232325",
            anchor="n",
            font=("Montserrat-Regular", 36),
            tags="countdown")

        self.canvas.create_text(
            375, 315,
            text="Flight Schedule:",
            fill="#232325",
            anchor="nw",
            font=("Montserrat-SemiBold", 11),
            tags="countdown")

        self.canvas.create_text(
            375, 330,
            text="6 Januari 2022 | 09:00",
            fill="#232325",
            anchor="nw",
            font=("Montserrat-Medium", 11),
            tags="countdown")

        self.canvas.create_text(
            390, 446, width=320,
            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                 "Sed mi odio, commodo vel est et, bibendum auctor lacus.",
            fill="#232325",
            anchor="w",
            font=("Montserrat-Regular", 12),
            tag="countdown")

    def hide(self):
        self.canvas.delete("countdown")


class ThisThat:
    def __init__(self, canvas):
        self.canvas = canvas

        self.this_button = Button(
            text="Lorem Ipsum Dolor Sit Amet",
            wraplength=165,
            font=("Montserrat-Medium", 14),
            fg="#ffffff",
            bg="#A81D24",
            activeforeground="#ffffff",
            activebackground="#A81D24",
            borderwidth=3,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")

        self.that_button = Button(
            text="Lorem Ipsum Dolor Sit Amet",
            wraplength=165,
            font=("Montserrat-Medium", 14),
            fg="#ffffff",
            bg="#A81D24",
            activeforeground="#ffffff",
            activebackground="#A81D24",
            borderwidth=3,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")

        self.border_this = PhotoImage(file=f"win/img/border_this.png")
        self.border_score = PhotoImage(file=f"win/img/border_score.png")
        self.play_img = PhotoImage(file=f"win/img/play_img.png")
        self.play_button = Button(
            image=self.play_img,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")

    def show_main(self):
        self.canvas.create_text(
            375, 95,
            text="This or That?",
            fill="#232325",
            anchor="nw",
            font=("Montserrat-Medium", 30),
            tag="this_main")

        self.canvas.create_text(
            375, 140,
            text="Question #01",
            fill="#232325",
            anchor="nw",
            font=("Montserrat-Regular", 18),
            tag="this_main")

        self.this_button.place(
            x=375, y=200,
            width=170,
            height=115)

        self.that_button.place(
            x=555, y=200,
            width=170,
            height=115)

        self.canvas.create_image(
            365, 370,
            anchor="nw",
            image=self.border_this,
            tags="this_score")

        self.canvas.create_text(
            390, 440, width=320,
            text="Selamat bermain yah sayang, jawabnya yang emang sesuai preferensi kamu aja yaa",
            fill="#232325",
            anchor="w",
            font=("Montserrat-Regular", 12),
            tag="this_main")

    def hide_main(self):
        self.canvas.delete("this_main")
        self.this_button.place_forget()
        self.that_button.place_forget()

    def show_score(self):
        self.hide_main()
        self.play_button.place(
            x=581, y=454,
            width=174,
            height=51)

        self.canvas.create_text(
            375, 95,
            text="Score:",
            fill="#232325",
            anchor="nw",
            font=("Montserrat-Medium", 27),
            tag="this_score")

        self.canvas.create_text(
            565, 145, width=300,
            text="100 %",
            fill="#232325",
            anchor="n",
            font=("Montserrat-Medium", 48),
            justify="center",
            tags="this_score")

        self.canvas.create_image(
            365, 270,
            anchor="nw",
            image=self.border_score,
            tags="this_score")

        self.canvas.create_text(
            387, 345, width=350,
            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed mi odio, commodo vel est et, bibendum "
                 "auctor lacus.",
            fill="#232325",
            anchor="w",
            font=("Montserrat-Regular", 14),
            tags="this_score")

    def hide_score(self):
        self.canvas.delete("this_score")
        self.play_button.place_forget()


class RandomFact:
    def __init__(self, canvas):
        self.canvas = canvas

        self.refresh_img = PhotoImage(file="win/img/refresh_img.png")
        self.refresh_button = Button(
            image=self.refresh_img,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")

    def show(self):
        self.refresh_button.place(
            x=705, y=108,
            width=27,
            height=27,
            anchor="nw")

        self.canvas.create_text(
            375, 95,
            text="Random Fact #01",
            fill="#232325",
            anchor="nw",
            font=("Montserrat-Medium", 27),
            tags="random_fact")

        self.canvas.create_text(
            375, 166, width=350,
            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed mi odio, commodo vel est et, bibendum "
                 "auctor lacus. Aenean egestas augue sed rhoncus iaculis",
            fill="#232325",
            anchor="nw",
            font=("Montserrat-Regular", 16),
            tags="random_fact")

    def hide(self):
        self.canvas.delete("random_fact")
        self.refresh_button.place_forget()


class Mail:
    def __init__(self, canvas):
        self.canvas = canvas

    def show(self):
        self.canvas.create_text(
            375, 95,
            text="Dear Bit,",
            fill="#232325",
            anchor="nw",
            font=("Montserrat-Medium", 27),
            tags="mail")

        self.canvas.create_text(
            375, 170, width=375,
            text="Semoga pas Bit baca ini, moodnya pas bagus ya. "
                 "Kalau pun lagi ga bagus, semoga pas buka apps ini, moodnya jadi lebih bagus.\n\n"
                 "Anyway, Mas mau bilang kalo Mas ngerasa sampe detik ini,seneng banget masih bisa sama Bit "
                 "dan Mas berharap bisa terus selamanya sama Bit. "
                 'Mengutip dari apa yang pernah Bit bilang, "I wanna grow old with you"\n\n'
                 "Semoga Bit suka apps versi 2.0.0 ini ya, harusnya lebih enak dilihat dan fiturnya juga lebih banyak. "
                 "Kalo ada yang menurut Bit bisa diimprove, coba kabarin Mas aja yahh. "
                 "Nanti mas update di release selanjutnya.\n\n",
            fill="#232325",
            anchor="nw",
            font=("Montserrat-Regular", 11),
            tags="mail")

        self.canvas.create_text(
            645, 490,
            text="with love,\nMas Haddad",
            fill="#232325",
            anchor="nw",
            font=("Montserrat-Regular", 11),
            tags="mail")

    def hide(self):
        self.canvas.delete("mail")


class Setting:
    def __init__(self, root, canvas):
        self.root = root
        self.canvas = canvas

        self.calendar = Calendar(
            self.root,
            selectmode='day',
            year=2022,
            month=1,
            day=7)

    def show(self):
        self.canvas.create_text(
            375, 95,
            text="Setting",
            fill="#232325",
            anchor="nw",
            font=("Montserrat-Medium", 27),
            tags="mail")

        self.calendar.place(
            x=375, y=170,
            width=350,
            height=225)

    def hide(self):
        self.canvas.delete("setting")


class Guide:
    def __init__(self, canvas):
        self.canvas = canvas

    def show(self):
        self.canvas.create_text(
            375, 95,
            text="F.A.Q.",
            fill="#232325",
            anchor="nw",
            font=("Montserrat-Medium", 27),
            tags="mail")

        self.canvas.create_text(
            375, 170, width=375,
            text="Q : Mas, mau ganti tanggal pulang Mas gimana caranya?\n"
                 "A : Bisa klik setting sayang, nanti ganti tanggalnya di situ yaa.\n\n"
                 "Q : Mas, mau request tambahin fitur dong. Bisa ngga?\n"
                 "A : Bisa sayang, coba kontak hotline aja yaa.\n\n"
                 'Q : Score di "This or That" itu gimana maksudnya?"\n'
                 'A : Nah jadi di tiap pertanyaan itu jawaban Bit bakal dibandingin sama preferensi pilihan Mas. '
                 'Dari situ keluar scorenya',
            fill="#232325",
            anchor="nw",
            font=("Montserrat-Regular", 11),
            tags="mail")


def btn_clicked():
    print("clicked")
