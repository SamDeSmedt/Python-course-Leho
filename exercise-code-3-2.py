#!/usr/bin/python3
# Python script that returns the astrological sign for a given date

day = int(input("What is your day of birth (e.g. 26): "))
month = input("What is your month of birth (e.g. june): ")

if ((month.lower() == "january") and (20 <= day <= 31)) or (month.lower() == "february" and (1 <= day <= 18)):
    print("Your astrological sign is Aquarius")
elif ((month.lower() == "february") and (19 <= day <= 29)) or (month.lower() == "march" and (1 <= day <= 20)):
    print("Your astrological sign is Pisces")
elif ((month.lower() == "march") and (21 <= day <= 31)) or (month.lower() == "april" and (1 <= day <= 19)):
    print("Your astrological sign is Aries")
elif ((month.lower() == "april") and (20 <= day <= 31)) or (month.lower() == "may" and (1 <= day <= 20)):
    print("Your astrological sign is Taurus")
elif ((month.lower() == "may") and (21 <= day <= 31)) or (month.lower() == "june" and (1 <= day <= 20)):
    print("Your astrological sign is Gemini")
elif ((month.lower() == "june") and (21 <= day <= 31)) or (month.lower() == "july" and (1 <= day <= 22)):
    print("Your astrological sign is Cancer")
elif ((month.lower() == "july") and (23 <= day <= 31)) or (month.lower() == "august" and (1 <= day <= 22)):
    print("Your astrological sign is Leo")
elif ((month.lower() == "august") and (23 <= day <= 31)) or (month.lower() == "september" and (1 <= day <= 22)):
    print("Your astrological sign is Virgo")
elif ((month.lower() == "september") and (23 <= day <= 31)) or (month.lower() == "october" and (1 <= day <= 22)):
    print("Your astrological sign is Libra")
elif ((month.lower() == "october") and (23 <= day <= 31)) or (month.lower() == "november" and (1 <= day <= 21)):
    print("Your astrological sign is Scorpio")
elif ((month.lower() == "november") and (22 <= day <= 31)) or (month.lower() == "december" and (1 <= day <= 21)):
    print("Your astrological sign is Sagittarius")
elif ((month.lower() == "december") and (22 <= day <= 31)) or (month.lower() == "january" and (1 <= day <= 19)):
    print("Your astrological sign is Capricorn")