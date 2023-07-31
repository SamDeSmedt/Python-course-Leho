#!/usr/bin/python3
################################################################################
# if conditionals
################################################################################
day = int(input("What is your day of birth (e.g. 26): "))
month = input("What is your month of birth (e.g. june): ")

if ((month.lower() == "january") and (20 <= day <= 31)) or (month.lower() == "february" and (1 <= day <= 18)):
    astro_sign = "Aquarius"
elif ((month.lower() == "february") and (19 <= day <= 29)) or (month.lower() == "march" and (1 <= day <= 20)):
    astro_sign = "Pisces"
elif ((month.lower() == "march") and (21 <= day <= 31)) or (month.lower() == "april" and (1 <= day <= 19)):
    astro_sign = "Aries"
elif ((month.lower() == "april") and (20 <= day <= 31)) or (month.lower() == "may" and (1 <= day <= 20)):
    astro_sign = "Taurus"
elif ((month.lower() == "may") and (21 <= day <= 31)) or (month.lower() == "june" and (1 <= day <= 20)):
    astro_sign = "Gemini"
elif ((month.lower() == "june") and (21 <= day <= 31)) or (month.lower() == "july" and (1 <= day <= 22)):
    astro_sign = "Cancer"
elif ((month.lower() == "july") and (23 <= day <= 31)) or (month.lower() == "august" and (1 <= day <= 22)):
    astro_sign = "Leo"
elif ((month.lower() == "august") and (23 <= day <= 31)) or (month.lower() == "september" and (1 <= day <= 22)):
    astro_sign = "Virgo"
elif ((month.lower() == "september") and (23 <= day <= 31)) or (month.lower() == "october" and (1 <= day <= 22)):
    astro_sign = "Libra"
elif ((month.lower() == "october") and (23 <= day <= 31)) or (month.lower() == "november" and (1 <= day <= 21)):
    astro_sign = "Scorpio"
elif ((month.lower() == "november") and (22 <= day <= 31)) or (month.lower() == "december" and (1 <= day <= 21)):
    astro_sign = "Sagittarius"
elif ((month.lower() == "december") and (22 <= day <= 31)) or (month.lower() == "january" and (1 <= day <= 19)):
    astro_sign = "Capricorn"
else:
    astro_sign = "INVALID"

print("Your astrological sign is {}.".format(astro_sign))