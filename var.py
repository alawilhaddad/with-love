import configparser
from datetime import datetime
from configparser import ConfigParser
import os


class Configuration:
    def __init__(self):
        try:
            if os.path.isfile("win/config.txt"):
                config = ConfigParser()
                config.read("win/config.txt")
                self.year = int(config.get("schedule", "year"))
                self.month = int(config.get("schedule", "month"))
                self.day = int(config.get("schedule", "day"))
                self.hour = int(config.get("schedule", "hour"))
                self.minute = int(config.get("schedule", "minute"))
                self.score = 0
                self.schedule = datetime(self.year,
                                         self.month,
                                         self.day,
                                         self.hour,
                                         self.minute,
                                         0, 0)
                self.question_limit = int(config.get("this_that", "limit"))
            else:
                self.initiate()
        except configparser.NoSectionError:
            self.initiate()
    def initiate(self):
        text = ["[schedule]\n",
                "year = 2022\n",
                "month = 1\n",
                "day = 6\n",
                "hour = 9\n",
                "minute = 5\n",
                "\n",
                "[this_that]\n",
                "limit = 10"]
        with open("win/config.txt", "w") as configfile:
            configfile.writelines(text)
        self.__init__()

var = Configuration()
