#!/usr/bin/python3
# Script to display functions of the time module

import time

print(
    "Month of the year: {}\n"
    "Week number of the year: {}\n"
    "Day of year: {}\n"
    "Day of month: {}\n"
    "Day of week: {}\n"
    .format(time.strftime("%B",),time.strftime("%W"),time.strftime("%j"),time.strftime("%d"),time.strftime("%A")))

import locale
locale.setlocale(locale.LC_TIME,"nl_NL")

print("Maand van jaar: {}\n"
      "Dag van week: {}\n"
      .format(time.strftime("%B"), time.strftime("%A")))