#!/usr/bin/python3
# Script to calculate the sum and average of n integers numbers

# Variables
count = 0
total_sum = 0.0 # Add the dot to create a float variable
number = 1

# input
print("Enter integers to calculate sum and average.\nInput 0 to exit.\n")

while number != 0:
    number = int(input())
    total_sum += number
    count = count + 1 # count += 1
else:
    avg = (total_sum / (count-1))
    print("Calculating sum and average for the above numbers:\nsum = {}\naverage = {}".format(total_sum,avg))