#!/usr/bin/python3
################################################################################
# Beautiful Soup (example-code-7-bs4-2.py)
################################################################################
import urllib.request
from bs4 import BeautifulSoup
# Get content data using urllib and create soup object
url = "http://www.cazy.org/GH100_all.html"
response = urllib.request.urlopen(url)
content = response.read()
soup = BeautifulSoup(content, 'html.parser')

# Tag object 1: example <table>
tag_table = soup.table
print("\nSTRING VALUE table tag --> {}".format(tag_table)) # Retrieve all table information; HTML like
print("\nNAME TAG --> {}".format(tag_table.name)) # Name tag will be "table" for this exercise
print("\nATTRIBUTES TAG --> {}".format(tag_table.attrs)) # Styling applied on the tag
# Tag object 2: example <td>
tag_td = soup.td
print("\nSTRING VALUE td tag --> {}".format(tag_td)) # Retrieve all td information
print("\nNAME TAG --> {}".format(tag_td.name)) # Name tag is "td"
print("\nATTRIBUTES TAG --> {}".format(tag_td.attrs))# Styling applied on the tag
# Tag object 3: multi-valued attributes example <div class>
tag_h1 = soup.h1
print("\nSTRING VALUE h1 tag --> {}".format(tag_h1)) # Retrieve all h1 information
print("\nNAME TAG --> {}".format(tag_h1.name)) # Name tag is "h1
print("\nATTRIBUTES h1 tag --> {}".format(tag_h1.attrs)) # Styling applied on the tag
print("List of values of attribute 'style' in h1 tag --> {}"
    .format(tag_h1['style']))

# NavigableString
tag_title = soup.title # Directly get the string that is between the title tag
print("\nNavigableString --> {}".format(tag_title.string))

# Navigate tag
print("\nFirst 'option tag':\n{}".format(soup.body.option))

# Get list of all occurences of the tag
option_list = soup.find_all("option")
print("\nThree from list of all 'option' tags:\n{}\n{}\n{}"
    .format(option_list[0],option_list[1],option_list[2]))
################################################################################