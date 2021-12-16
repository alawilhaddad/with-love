import random

with open("../this or that.txt", "r") as file:
    this_that = []
    for line in file.readlines():
        this_that.append(line.strip("\n").split(","))

item = random.choice(this_that)
print(item[0])
print(item[1])
print(item[int(item[2])])
