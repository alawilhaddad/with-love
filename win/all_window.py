import random
from datetime import datetime
from tkinter import *
from tkinter.messagebox import askyesno, showinfo
from tkcalendar import *
import webbrowser
from var import var
from configparser import ConfigParser


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
        for section in (MenuButton, Home, Countdown, ThisThat, Score, RandomFact, Mail, Configure, Guide):
            frame = section(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[section] = frame

            frame.config(bg="#DCDCD4", width=800, height=600)
            frame.place(x=0, y=0)

        # Using a method to switch frames
        self.show_frame(Home)

    # Raises the current frame to the top
    def show_frame(self, section):
        frame = self.frames[section]
        frame.tkraise()

    # Click and drag window
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


class MenuButton(MainMenu):
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
            command=lambda: controller.show_frame(ThisThat),
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
        self.controller = controller

        # Set home title
        self.home_title_img = PhotoImage(file=f"win/img/home_title_img.png")
        self.canvas.create_image(
            375, 168,
            anchor="nw",
            image=self.home_title_img,
            tags="home")


class Countdown(MainMenu):
    def __init__(self, parent, controller):
        MainMenu.__init__(self, parent)
        self.controller = controller

        self.canvas.create_text(
            375, 95,
            text="Waiting time:",
            fill="#232325",
            anchor="nw",
            font=("Montserrat-Medium", 27),
            tags="countdown")

        self.days_text = self.canvas.create_text(
            550, 145,
            text="100 Hari",
            fill="#232325",
            anchor="n",
            font=("Montserrat-Regular", 60),
            tags="countdown")
        self.time_text = self.canvas.create_text(
            435, 240,
            text="06",
            fill="#232325",
            anchor="nw",
            font=("Courier New", 36),
            tags="countdown")

        self.canvas.create_text(
            375, 315,
            text="Schedule:",
            fill="#232325",
            anchor="nw",
            font=("Montserrat-SemiBold", 11),
            tags="countdown")

        self.schedule_text = self.canvas.create_text(
            375, 335,
            text=var.schedule.strftime("%A, %d %B %Y | %H:%M:%S"),
            fill="#232325",
            anchor="nw",
            font=("Montserrat-Medium", 11),
            tags="countdown")

        self.border_img = PhotoImage(file=f"win/img/border_countdown.png")
        self.canvas.create_image(
            365, 378,
            anchor="nw",
            image=self.border_img,
            tags="countdown")

        self.messages = self.canvas.create_text(
            390, 446, width=320,
            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                 "Sed mi odio, commodo vel est et, bibendum auctor lacus.",
            fill="#232325",
            anchor="w",
            font=("Montserrat-Regular", 12),
            tag="countdown")

        self.update_time()

    def update_time(self):
        current_time = datetime.now()
        diff = var.schedule - current_time
        days = diff.days
        hours = str((diff.seconds // 3600)).zfill(2)
        minutes = str((3720 // 60) % 60).zfill(2)
        seconds = str((diff.seconds % 3600) % 60).zfill(2)
        if int(diff.total_seconds()) <= 0:
            days, hours, minutes, seconds = ["0", "00", "00", "00"]
            messages = "Yeay! mas udah pulang yahh. Ayo cepetan redeem voucher Bit. " \
                       "Kalo ternyata Mas udah on duty lagi, ganti tanggal pulang Mas di setting yaa"
        else:
            messages = "Ditahan dulu ya kangennya, sayang. Mas masih mengusahakan tabungan demi 24/7 kita. " \
                       "Bentar lagi Mas pulang kok. See you soon, Sayaang"

        self.canvas.itemconfig(
            self.days_text,
            text=f"{days} Hari")

        self.canvas.itemconfig(
            self.time_text,
            text=f"{hours}:{minutes}:{seconds}")

        self.canvas.itemconfig(
            self.messages,
            text=messages)

        self.canvas.after(1000, self.update_time)

    def tkraise(self, aboveThis=None):
        # Get the selected item from start_page
        self.canvas.itemconfig(self.schedule_text, text=var.schedule.strftime("%A, %d %B %Y | %H:%M:%S"))

        # Call the real .tkraise
        super().tkraise(aboveThis)


class ThisThat(MainMenu):
    def __init__(self, parent, controller):
        MainMenu.__init__(self, parent)

        with open("win/this or that.txt", "r") as file:
            self.this_that = []
            for line in file.readlines():
                self.this_that.append(line.strip("\n").split(","))
        self.active = list(self.this_that)
        self.item = []
        self.count = 1

        self.canvas.create_text(
            375, 95,
            text="This or That?",
            fill="#232325",
            anchor="nw",
            font=("Montserrat-Medium", 27),
            tag="this_main")

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
            command=lambda: self.next(controller, answer=0),
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
            command=lambda: self.next(controller, answer=1),
            relief="flat")

        self.number = self.canvas.create_text(
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
            365, 378,
            anchor="nw",
            image=self.border_this,
            tags="this_score")

        self.canvas.create_text(
            390, 446, width=320,
            text="Jawabnya sesuai preferensi Bit aja yaa. "
                 "Hasil akhirnya ga ngaruh apa-apa kok. Sama asik, beda juga asik. "
                 "Enjoy the game ya, bby.",
            fill="#232325",
            anchor="w",
            font=("Montserrat-Regular", 12),
            tag="this_main")

        self.rdm()

    def rdm(self):
        self.item = random.choice(self.active)
        self.active.remove(self.item)
        self.this_button.config(text=self.item[0])
        self.that_button.config(text=self.item[1])

    def next(self, controller, answer):
        if int(answer) == int(self.item[2]):
            var.score += 10
        if self.count != var.question_limit:
            self.count += 1
            self.canvas.itemconfig(self.number, text=f"Question #{str(self.count).zfill(2)}")
            self.rdm()
        elif self.count == var.question_limit:
            var.score = int(var.score / (var.question_limit * 10) * 100)
            controller.show_frame(Score)
            self.restart()

    def restart(self):
        self.count = 1
        var.score = 0
        self.active = list(self.this_that)
        self.rdm()
        self.canvas.itemconfig(self.number, text=f"Question #{str(self.count).zfill(2)}")


class Score(MainMenu):
    def __init__(self, parent, controller):
        MainMenu.__init__(self, parent)
        self.controller = controller
        self.messages = ["Let's share our similarities and celebrate our differences",
                         "A great relationship is about two things: First, appreciating our similarities and second, "
                         "respecting our differences.",
                         "Love is the power to see similarity in the dissimilar",
                         "A great relationship isn't when a perfect couple comes together, "
                         "but when an imperfect couple learns to enjoy their differences",
                         "The happiest relationship are between two people that have understanding of their differences"
                         ""]
        self.restart = PhotoImage(file=f"win/img/restart.png")
        self.play_button = Button(
            self,
            image=self.restart,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame(ThisThat),
            relief="flat")
        self.play_button.place(
            x=625, y=460,
            width=100,
            height=40)

        self.canvas.create_text(
            375, 95,
            text="Similarity:",
            fill="#232325",
            anchor="nw",
            font=("Montserrat-Medium", 27),
            tag="this_score")

        self.score = self.canvas.create_text(
            565, 145, width=300,
            text=f"{var.score} %",
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

        self.message_text = self.canvas.create_text(
            387, 355, width=320,
            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed mi odio, commodo vel est et, bibendum "
                 "auctor lacus.",
            fill="#232325",
            anchor="w",
            font=("Montserrat-Regular", 12),
            tags="this_score")

    def tkraise(self, aboveThis=None):
        # Get the selected item from start_page
        self.canvas.itemconfig(self.message_text, text=random.choice(self.messages))
        self.canvas.itemconfig(self.score, text=f"{var.score} %")

        # Call the real .tkraise
        super().tkraise(aboveThis)


class RandomFact(MainMenu):
    def __init__(self, parent, controller):
        MainMenu.__init__(self, parent)
        self.controller = controller
        with open("win/random_facts.txt", "r") as file:
            self.facts = []
            for line in file.readlines():
                self.facts.append(line.strip("\n").split("|"))

        self.refresh_img = PhotoImage(file="win/img/refresh_img.png")
        self.refresh_button = Button(
            self,
            image=self.refresh_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.randomize,
            relief="flat")
        self.refresh_button.place(
            x=710, y=109,
            width=27,
            height=27,
            anchor="nw")

        self.number = self.canvas.create_text(
            375, 95,
            text="Random Fact #01",
            fill="#232325",
            anchor="nw",
            font=("Montserrat-Medium", 27),
            tags="random_fact")

        self.fact = self.canvas.create_text(
            375, 300, width=350,
            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed mi odio, commodo vel est et, bibendum "
                 "auctor lacus. Aenean egestas augue sed rhoncus iaculis",
            fill="#232325",
            anchor="w",
            font=("Montserrat-Regular", 16),
            tags="random_fact")

        self.randomize()

    def randomize(self):
        fact = random.choice(self.facts)
        self.canvas.itemconfig(self.number, text=f"Random Fact #{fact[0].zfill(2)}")
        self.canvas.itemconfig(self.fact, text=fact[1])


class Mail(MainMenu):
    def __init__(self, parent, controller):
        MainMenu.__init__(self, parent)
        self.controller = controller

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
        self.controller = controller
        self.limit = IntVar(value=var.question_limit)
        self.hour = IntVar(value=var.hour)
        self.minute = IntVar(value=var.minute)

        self.canvas.create_text(
            375, 95,
            text="Question Limit",
            fill="#232325",
            anchor="nw",
            font=("Montserrat-Medium", 27),
            tags="mail")

        self.limit_box = Spinbox(
            self,
            from_=5,
            to=20,
            format="%02.0f",
            wrap=True,
            textvariable=self.limit,
            width=2,
            state="readonly",
            font=("Montserrat-Medium", 11),
            justify=CENTER)
        self.limit_box.place(x=375, y=170, width=75, height=25)

        self.save_img = PhotoImage(file="win/img/save_img.png")
        self.save_limit = Button(
            self,
            image=self.save_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.save_limit,
            relief="flat")
        self.save_limit.place(
            x=650, y=170,
            width=75,
            height=25,
            anchor="nw")

        self.canvas.create_line(
            365, 202, 735, 202,
            fill="#232325",
            width=2)
        self.canvas.create_text(
            375, 195,
            text="Schedule",
            fill="#232325",
            anchor="nw",
            font=("Montserrat-Medium", 27),
            tags="mail")

        self.calendar = Calendar(
            self,
            selectmode='day',
            font=("Montserrat-Medium", 10),
            year=var.year,
            month=var.month,
            day=var.day)
        self.calendar.place(
            x=375, y=270,
            width=350,
            height=200)

        self.hour_box = Spinbox(
            self,
            from_=0,
            to=23,
            format="%02.0f",
            wrap=True,
            textvariable=self.hour,
            width=2,
            state="readonly",
            font=("Montserrat-Medium", 11),
            justify=CENTER)
        self.hour_box.place(x=375, y=480, width=75, height=25)

        self.minute_box = Spinbox(
            self,
            from_=00,
            to=59,
            format="%02.0f",
            wrap=True,
            textvariable=self.minute,
            width=2,
            state="readonly",
            font=("Montserrat-Medium", 11),
            justify=CENTER)
        self.minute_box.place(x=468, y=480, width=75, height=25)

        self.canvas.create_text(
            456, 476,
            text=":",
            fill="#232325",
            anchor="nw",
            font=("Montserrat-Medium", 16),
            tags="mail")

        self.canvas.create_text(
            553, 480,
            text="GMT+7",
            fill="#232325",
            anchor="nw",
            font=("Montserrat-Medium", 12),
            tags="mail")

        self.save_schedule = Button(
            self,
            image=self.save_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.save_schedule,
            relief="flat")
        self.save_schedule.place(
            x=650, y=505,
            width=75,
            height=25,
            anchor="nw")

    def save_limit(self):
        var.question_limit = int(self.limit_box.get())
        config = ConfigParser()
        config.read("win/config.txt")
        config.set("this_that", "limit", str(var.question_limit))
        with open("win/config.txt", "r+") as configfile:
            config.write(configfile)
        showinfo(title="Question Limit Changed", message=f"Sip, udah kesave ya, sayang.\n\n"
                                                         f'Question limit/game:{var.question_limit} Question')

    def save_schedule(self):
        var.month, var.day, var.year = list(map(lambda x: int(x), self.calendar.get_date().split("/")))
        var.year += 2000
        var.hour = int(self.hour_box.get())
        var.minute = int(self.minute_box.get())
        var.schedule = datetime(var.year, var.month, var.day, var.hour, var.minute, 0, 0)

        config = ConfigParser()
        config.read("win/config.txt")
        config.set("schedule", "year", str(var.year))
        config.set("schedule", "month", str(var.month))
        config.set("schedule", "day", str(var.day))
        config.set("schedule", "hour", str(var.hour))
        config.set("schedule", "minute", str(var.minute))
        with open("win/config.txt", "w") as configfile:
            config.write(configfile)
        showinfo(title="Schedule Changed", message=f"Sip, udah kesave ya, sayang.\n\n"
                                                   f"Schedule:\n"
                                                   f"{var.schedule.strftime('%A, %d %B %Y | %H:%M:%S')}")


class Guide(MainMenu):
    def __init__(self, parent, controller):
        MainMenu.__init__(self, parent)
        self.controller = controller
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
                 'Q : Similarity di "This or That" itu gimana maksudnya?"\n'
                 'A : Nah jadi di tiap pertanyaan itu jawaban Bit bakal dibandingin sama preferensi pilihan Mas. '
                 'Dari situ keluar nilai similarity kita.',
            fill="#232325",
            anchor="nw",
            font=("Montserrat-Regular", 11),
            tags="guide")


def call():
    if askyesno(title="Confirmation", message="This action will open web browser. Continue?"):
        webbrowser.open('wa.me/6281334455285')


if __name__ == "__main__":
    testObj = MainWindow()
    testObj.show_frame(RandomFact)
    testObj.mainloop()
