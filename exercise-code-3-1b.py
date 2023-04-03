#!/usr/bin/python3
# Script that returns ages for a given list of birth years

yob = [1990, 1995, 1990, 1991, 1992, 1991]

# importing date class from datetime module
from datetime import date

# creating the date object of today's date
todays_date = date.today()

# printing current year
#print("Current date: ", todays_date.year)


rangeyob = list(range(0,len(yob),1))
print(rangeyob)

# Iterate over each year to calculate the year
age = [(todays_date.year - yob[i]) for i in rangeyob ]

print("The list of birth years: {} \n"
      "The list of ages to the current year ({}): {}".format(yob, todays_date.year, age))


