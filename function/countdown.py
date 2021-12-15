import time
from datetime import datetime
from tkinter import *


class Variable:
    def __init__(self):
        self.schedule = datetime(2022, 1, 7, 8, 5, 0, 0)
        self.days = ""
        self.hour = ""
        self.minute = ""
        self.second = ""
        self.message = ""


def countdown(var):
    current_time = datetime.now()
    # current_time = datetime(2022, 1, 18, 13, 15, 0, 0)
    diff = var.schedule - current_time
    print(type(diff))
    var.days = diff.days
    var.hour = str((diff.seconds // 3600)).zfill(2)
    var.minute = str((3720 // 60) % 60).zfill(2)
    var.second = str((diff.seconds % 3600) % 60).zfill(2)
    # print(type(diff.days))
    if var.days < -11:
            print("""
    sayang, kayanya kamu harus kontak hotline deh.
    ini scriptnya udah harus maintenance.""")
    elif diff.seconds < 0 and diff.days > -11:
            print("""yeay! mas udah pulang yahh.
    ayo redeem voucher kamu sayang""")
    else:
            print(f"\nSayang sabar yahh. bentar lagi mas pulang kok.")
            print(f"Tinggal {var.days} hari {var.hour}:{var.minute}:{var.second} sebelum flight mas\nke surabaya")


def update():
    now = datetime.now().strftime("%A, %d %B %Y | %H:%M:%S")
    label.config(text=now)
    label.after(1000, update)


if __name__ == "__main__":
    window = Tk()
    label = Label(window, font=("Calibri", 40))
    label.pack()

    update()
    current_time = datetime.now()
    # current_time = datetime(2022, 1, 18, 13, 15, 0, 0)
    schedule = datetime(2022, 1, 7, 8, 5, 0, 0)
    diff = schedule - current_time

    print(type(diff))
    # time = Variable()
    # countdown(time)
    window.mainloop()
