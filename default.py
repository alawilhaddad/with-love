import os
from datetime import datetime
from configparser import ConfigParser

#
# class Variable:
#     def __init__(self):
#         self.year = 2022
#         self.month = 1
#         self.day = 6
#         self.hour = 8
#         self.minute = 5
#         self.score = 0
#         self.schedule = datetime(
#             self.year,
#             self.month,
#             self.day,
#             self.hour,
#             self.minute, 0, 0)
#         self.limit = 10
#         self.config_path = "win/config.txt"
#         self.setting = {}
#
#     def default(self):
#         if os.path.isfile(self.config_path):
#             with open(self.config_path, "r+") as file:
#                 for line in list(map(lambda x: x.strip("\n").split("="), file.readlines()))
#                     self.setting[line[0]] = int(line[1])
#
#             print(self.setting)
#             print(self.setting.get("limit"))
    # else:
    #     with open("win/config.txt", "w") as file:
    #         file.write(f"open= \n")
    #         file.write(f"save= ")


if __name__ == "__main__":
    # var = Variable()
    # var.default()
    pars = ConfigParser()
    pars.read("win/config.txt")
    print(pars.get('schedule', 'year'))

