#!/usr/bin/python3
import random


def judge_tow_beans(bean1, bean2):
    if bean1 != bean2:
        return "White"
    if bean1 == bean2:
        return "Black"


def coffee_beans_game(black_num, white_num):
    if black_num < 0:
        print ("The black_num must bigger than 0")
    if white_num < 0:
        print ("The white_num must bigger than 0")
    if white_num + black_num == 0:
        print ("There should be some beans in the coffee can. Right?")
    if white_num + black_num == 1:
        print ("There should be more beans in the coffee can to start the game.")
    if white_num + black_num > 1:
        coffee_can = ["Black"] * black_num + ["White"] * white_num
        random.shuffle(coffee_can)
        while len(coffee_can) > 1:
            bean1 = coffee_can[0]
            bean2 = coffee_can[1]
            coffee_can = coffee_can[2:]
            coffee_can.append(judge_tow_beans(bean1, bean2))
            random.shuffle(coffee_can)
        return coffee_can[0]


for i in range(0,10):
    print (coffee_beans_game (14, i*2+1))