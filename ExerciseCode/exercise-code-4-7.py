#!/usr/bin/python3
# Script to shuffle deck of cards

import itertools as it
import random as r
i = 0
input = input("We have an other contender!\n\
Please, whick suit will be picked the most?: ")

ranks = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
suits = ["hearts", "diamonds", "clubs", "spades"]

# All combinations of ranks and suits form a deck
deck = list(it.product(ranks, suits))
#print("Deck of cards using itertools:\n{}\n{}".format("="*30,deck))
#for n in deck: print(n)

#shuffle the deck 2 times
while i < 2: 
    i += 1
    #print("Shuffeled DECK{}:\n{}\n{}".format(i,"="*30, deck))
    r.shuffle(deck)

#create dictionary to keep track of chosen values
choiced = []

i = 0 
while i < 10:
    #Select a random card from the shuffeled deck
    card = r.choice(deck)
    #print(card)
    choiced.append(card)
    del card
    i += 1

#have a list with default counts
countd = {"hearts":0, "diamonds":0, "clubs":0, "spades":0}

#count all the suits of the cards
for value in choiced:
    countd[value[1]]+=1
print(max(countd, key=countd.get))

if input == max(countd, key=countd.get):
    print("You guessed the right winner!")
else:
    print("You should better stop guessing!")


