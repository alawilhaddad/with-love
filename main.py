from win.main_window import *
from win.properties import Win


if __name__ == "__main__":
    window = Win()
    main = Main(window)
    home = Home(main.canvas)
    countdown = Countdown(main.canvas)
    this_that = ThisThat(main.canvas)
    random_fact = RandomFact(main.canvas)
    mail = Mail(main.canvas)
    setting = Setting(window, main.canvas)
    guide = Guide(main.canvas)
    setting.show()
    window.mainloop()
