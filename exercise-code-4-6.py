#!/usr/bin/python3
# Script to check password validity

import re

while True:
    passwd = input("Give a valid password: ")
    if (6 <= len(passwd) <= 16)\
        and (any(c.islower() for c in passwd)\
        and any(c.isupper() for c in passwd)\
        and any(c.isdigit() for c in passwd)\
        and any(c in "$#@" for c in passwd)):

        print("Valid password")
        break
    else:
        print("NOT a valid password!")
