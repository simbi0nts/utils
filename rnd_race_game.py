# -*- coding: utf-8 -*-

from datetime import datetime
import os, time
import random


def randInit(x):
    x = -1
    for t in range(random.randint(10,100)):
        #x = (int(datetime.strftime(datetime.now(), "%f"))//10000%10)
        x = random.randint(0,99)
    return x%10

def game():
    winNum = 0
    sep = '- '
    t = []
    rnd = -1
    for x in range(10):
        t.append('')
    while 50 not in list(map(len, t)):
        rnd = randInit(rnd)
        t[rnd] += sep
        os.system('cls')
        for x in t:
            print(x + "\n")
        time.sleep(1/10)
    os.system('cls')
    for x in t:
        if len(x) == 50:
            print(x + " - ИГРОК НОМЕР [" + str(winNum+1) + "] ПОБЕДИЛ \n")
        else:
            print(x + "\n")
            winNum += 1

if __name__ == "__main__":
    game()
    while 1:
        print ("\n Play again?(Y/N)")
        ans = input()
        if ans.lower() == "y" or ans.lower() == "yes":
            game()
        elif ans.lower() == "n" or ans.lower() == "no":
            break
        else:
            print("Wrong answer")


