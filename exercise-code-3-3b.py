#!/usr/bin/python3
# Script for a guessing game

from random import randrange
randomNo = 0
guessNo = 3

while randomNo != guessNo:
    guessNo = int(input("Guess the number between 1 and 9: "))
    randomNo = (randrange(1,9))
    print(randomNo)
else:
    print("YES! {} is the number!".format(guessNo))
    