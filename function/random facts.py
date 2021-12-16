import random

with open("../random_facts.txt", "r") as file:
    facts = []
    for line in file.readlines():
        facts.append(line.strip("\n").split("|"))
fact = random.choice(facts)

print(fact)
