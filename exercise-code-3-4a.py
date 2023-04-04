#!/usr/bin/python3
# Script to print Capital for each country in a dictionary
capital = {
    "Belgium": "Brussels", 
    "United Kingdom": "London", 
    "France": "Paris", 
    "Spain": "Madrid"
    }

print("List of capitals: \n" + "="*20)

for capital in capital.values():
    print(capital)
