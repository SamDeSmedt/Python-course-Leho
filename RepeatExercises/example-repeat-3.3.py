#!/usr/bin/python3
################################################################################
# while loop
################################################################################
# Python script to get Fibonacci series between 0 to 50
"""
x = 1
y = 0
z = 0

end = int(input("Provide an integer for the series of Fibonacci to end: "))
while x <= end:
    z = x + y
    print("{} + {} = {}".format(x,y,z))
    y = x
    x = z
"""
################################################################################
# Python script to guess a number between 1 to 9
import random

while True:
    randomnr = random.randrange(1,9)
    guessnr = int(input("Guess a number between 1 and 9: "))
    if guessnr > 9:
        print("The number should be between 0 and 9")
        break
    elif randomnr == guessnr:
        print("YES! {} is the number!".format(guessnr))
        break
    else:
        print("The correct number was: {}".format(randomnr))
        answer = input("Do you want to try again? [Y/N] ")
        if answer.upper() == "N": break


    

    



