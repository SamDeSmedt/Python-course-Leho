#!/usr/bin/python3

# Script that seperates string by a character, orders the strings and join them

def StringSort(input,varchar):
    # Seperate the strings using the split() function
    split = input.split(varchar)
    #print(split)
    split.sort()
    #print(split)
    join = varchar.join(split)
    return join

varchar = input("Type a character to separate a sequence of words: \n")
input = input("Type a character separated sequence to sort and join again: \n")
print(StringSort(input, varchar))