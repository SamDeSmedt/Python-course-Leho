#!/usr/bin/python3
################################################################################
# Comprehensions
################################################################################
# Declare input list and return even numbers
list = [1, 4, 9, 16, 25, 36, 49, 64, 91, 100]
evenlist = []

for x in list:
    if x % 2 == 0:
        evenlist.append(x)
print("Given list: {}".format(list))
print("Even list: {}".format(evenlist))
################################################################################
# Return ages for a given list of years of birth
from time import strftime

yob = [1990, 1995, 1990, 1991, 1992, 1991]
ages = []
cyear = int(strftime("%Y"))

for year in yob:
    ages.append(cyear - year)
print("The current year is: {}".format(cyear))
print("Years of birth: {}".format(yob))
print("Ages: {}".format(ages))
    




