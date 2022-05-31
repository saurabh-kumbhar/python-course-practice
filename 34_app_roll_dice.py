import random


def roll():
    return random.randint(1,6), random.randint(1,6)


while True:
    input_value = input("(R)ole Dice or (E)xit? > ")

    if input_value.lower() == "e":
        break

    print(roll())
