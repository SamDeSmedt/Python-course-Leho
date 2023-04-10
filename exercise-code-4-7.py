#!/usr/bin/python3
# Script to shuffle deck of cards

import itertools as it
import random as r
i = 0

ranks = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
suits = ["hearts", "diamonds", "clubs", "spades"]

# All combinations of ranks and suits form a deck
deck = list(it.product(ranks, suits))
#print(deck)

while i < 2:
    r.shuffle(deck)
    i += 1

print (deck)