#!/usr/bin/python3

# Script to count the number of strings and check if the first and last character are the same

listWords = ['abc','xyz', 'aba', '1221']
listSorted = []
count = 0

for word in listWords:
    #print("STRING = {}".format(word))
    size = len(word)
    #print("size = {}".format(size))
    #print(word[0] + word[-1])

    if size > 2 and (word[0]== word[-1]):
        listSorted.append(word)
        count = count +1

print("Input words: {}\n\
Number of strings: {}\n\
List of these words: {}".format(listWords, count,listSorted))        
