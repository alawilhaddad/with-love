from tkinter import *
from tkinter.messagebox import askyesno
from tkcalendar import *
import webbrowser


class MainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)

        # Set to borderless window
        self.overrideredirect(True)
        self.offset_x = 0
        self.offset_y = 0
        self.bind("<Button-1>", self.click_win)
        self.bind("<B1-Motion>", self.drag_win)

        # Configure window properties
        self.window_height = 600
        self.window_width = 800
        self.config(bg="#A81D24")
        self.screen_w = self.winfo_screenwidth()
        self.screen_h = self.winfo_screenheight()
        self.pos_x = (self.screen_w / 2) - (self.window_width / 2)
        self.pos_y = (self.screen_h / 2) - (self.window_height / 2)
        self.geometry(f"{self.window_width}x{self.window_height}+{int(self.pos_x)}+{int(self.pos_y)}")

        # creating a frame and assigning it to container
        container = Frame(self, height=600, width=800, bg="#A81D24")
        # specifying the region where the frame is packed in root
        container.place(x=0, y=0)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}

        # we'll create the frames themselves later but let's add the components to the dictionary.
        for section in (MenuBar, Home, Countdown, ThisThat, Score, RandomFact, Mail, Configure, Guide):
            frame = section(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[section] = frame

            frame.config(bg="#DCDCD4", width=800, height=600)
            frame.place(x=0, y=0)

        # Using a method to switch frames
        self.show_frame(Home)

    def show_frame(self, section):
        frame = self.frames[section]
        # raises the current frame to the top
        frame.tkraise()

    def drag_win(self, event):
        psx = super().winfo_pointerx() - self.offset_x
        psy = super().winfo_pointery() - self.offset_y
        super().geometry(f"+{psx}+{psy}")
        return event

    def click_win(self, event):
        self.offset_x = super().winfo_pointerx() - super().winfo_rootx()
        self.offset_y = super().winfo_pointery() - super().winfo_rooty()
        return event


class MainMenu(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        # Set background
        self.canvas = Canvas(
            self,
            bg="white",
            height=600,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        self.background_img = PhotoImage(file=f"win/img/background.png")
        self.canvas.create_image(
            400, 300,
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
            command=quit,
            relief="flat")
        self.close_button.place(
            x=750, y=25,
            width=20,
            height=20)


class MenuBar(MainMenu):
    def __init__(self, parent, controller):
        MainMenu.__init__(self, parent)
        # Initialize home button
        self.home_img = PhotoImage(file=f"win/img/home_img.png")
        self.home_button = Button(
            image=self.home_img,
            borderwidth=0,
            highlightthickness=0,
            activebackground="#232325",
            command=lambda: controller.show_frame(Home),
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
            command=lambda: controller.show_frame(Countdown),
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
            command=lambda: controller.show_frame(Score),
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
            command=lambda: controller.show_frame(RandomFact),
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
            command=lambda: controller.show_frame(Mail),
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
            command=lambda: controller.show_frame(Configure),
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
            command=call,
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
            command=lambda: controller.show_frame(Guide),
            relief="flat")
        self.guide_button.place(
            x=170, y=460,
            width=120,
            height=120)


class Home(MainMenu):
    def __init__(self, parent, controller):
        MainMenu.__init__(self, parent)
        self.home_title_img = PhotoImage(file=f"win/img/home_title_img.png")
        self.canvas.create_image(
            375, 168,
            anchor="nw",
            image=self.home_title_img,
            tags="home")


class Countdown(MainMenu):
    def __init__(self, parent, controller):
        MainMenu.__init__(self, parent)
        self.border_img = PhotoImage(file=f"win/img/border_countdown.png")
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


class ThisThat(MainMenu):
    def __init__(self, parent, controller):
        MainMenu.__init__(self, parent)
        self.this_button = Button(
            self,
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
            self,
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

        self.border_this = PhotoImage(file=f"win/img/border_this.png")
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


class Score(MainMenu):
    def __init__(self, parent, controller):
        MainMenu.__init__(self, parent)

        self.play_img = PhotoImage(file=f"win/img/play_img.png")
        self.play_button = Button(
            self,
            image=self.play_img,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")
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

        self.border_score = PhotoImage(file=f"win/img/border_score.png")
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


class RandomFact(MainMenu):
    def __init__(self, parent, controller):
        MainMenu.__init__(self, parent)
        self.refresh_img = PhotoImage(file="win/img/refresh_img.png")
        self.refresh_button = Button(
            self,
            image=self.refresh_img,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")
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


class Mail(MainMenu):
    def __init__(self, parent, controller):
        MainMenu.__init__(self, parent)
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


class Configure(MainMenu):
    def __init__(self, parent, controller):
        MainMenu.__init__(self, parent)
        self.canvas.create_text(
            375, 95,
            text="Setting",
            fill="#232325",
            anchor="nw",
            font=("Montserrat-Medium", 27),
            tags="mail")

        self.calendar = Calendar(
            self,
            selectmode='day',
            year=2022,
            month=1,
            day=7)

        self.calendar.place(
            x=375, y=170,
            width=350,
            height=225)


class Guide(MainMenu):
    def __init__(self, parent, controller):
        MainMenu.__init__(self, parent)
        self.canvas.create_text(
            375, 95,
            text="F.A.Q.",
            fill="#232325",
            anchor="nw",
            font=("Montserrat-Medium", 27),
            tags="guide")

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
            tags="guide")


def call():
    if askyesno(title="Confirmation", message="This action will open web browser. Continue?"):
        webbrowser.open('wa.me/6281334455285')


def btn_clicked():
    print("clicked")


if __name__ == "__main__":
    testObj = MainWindow()
    testObj.mainloop()
