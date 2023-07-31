#!/usr/bin/python3
################################################################################
# combined control statements
################################################################################

# Create a list with a fixed set of values
list = [2, 28, 11, 7, 40, 15]
bigint = 0

print("Before: None")
print("-"*20)
for number in list:
    if number > bigint:
        bigint = number
    print("Loop:\t{}\t{}".format(number,bigint))
print("-"*20)
print("Largest: {}".format(bigint))
################################################################################
# Calculate sum and average of n integers number depending on user input
sum = 0
average = 0
i = 0
print("Enter integers to calculate sum and average\nInput 0 to exit")

while number != 0:
    number = int(input())
    sum = sum + number
    i += 1
average = sum / (i - 1)
print("Calculating sum and average for the above numbers:\nsum = {}\naverage = {}".format(sum, average))

################################################################################
# Create a fixed input list and an empty output list
input_words = ["abc", "xyz", "aba", "1221"]
output_words = []

for words in input_words:
    if words[0] == words[-1] and len(words) > 2:
        output_words.append(words)
length = len(output_words)
print("Input words: {}".format(input_words))
print("Number of strings: {}".format(length))
print("List of these words: {}".format(output_words))