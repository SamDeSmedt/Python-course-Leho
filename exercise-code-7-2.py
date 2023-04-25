#!/usr/bin/python3
################################################################################
# Accessing the internet and use the search function to collect pictures 
# and collect metedata from https://waarnemingen.be
################################################################################
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import wget
import os

print("\nSearch on waarnemingen.be web service:")
# Get content data using urllib and create soup object
# Hardcoded URL
url = "https://waarnemingen.be/photos/?date_after=2021-08-01&date_before=2021-08-01&species=&species_group=4&country_division=15&rarity=3&search=&likes=&user=&location=&sex=&type=&life_stage=&activity=&method="
base_url = "https://waarnemingen.be/"


# Retrieving Get variables
'''
species = {
    1: "Birds",
    2: "Mammals",
    3: "Reptiles and amphibians",
    4: "Butterflies"
}

Provinces = {
    14: "Limburg",
    15: "West-Vlaanderen",
    16: "Oost-Vlaanderen",
    17: "Antwerpen",
}

Rarities = {
    1: "common",
    2: "relatively common",
    3: "rare",
    4: "very rare"
}


date_after = input ("\nGive date after (in YYYY-MM-DD format): ")
date_before = input ("\nGive date before (in YYYY-MM-DD format): ")
species_input = input("\nSpecies groups: [1] Birds | [2] Mammals | [3] reptiles and amphibians | [4] Butterflies\nGive number of species group: ")
provinces_input = input("\nProvinces: [14] Limburg | [15] West-Vlaanderen | [16] Oost-Vlaanderen | [17] Antwerpen\nGive number of province: ")
rarities_input = input("[1] >=common | [2] >=relatively common | [3] >=rare | [4] very rare\nGive number of rarity: ")

params = urllib.parse.urlencode({'date_before': date_before, 'date_after': date_after, 'species_group': species_input, 'country_devision': provinces_input})
url = "https://waarnemingen.be/photos/?%s" % params
'''
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"

# Get content data using urllib and create soup object
response = urllib.request.urlopen(url)
content = response.read()
soup = BeautifulSoup(content, "html.parser")

# Create directory for pictures to store
pic_loc = os.getcwd()+"/Pictures"
# Check if location exists
if os.path.exists(pic_loc):
    os.chdir(pic_loc)
else:
    os.mkdir("Pictures")
    os.chdir(pic_loc)

# Tag (img) contents
img_tag = soup.find_all("img",{"loading":"lazy"})
for img in img_tag:
    img_url = base_url + img["src"]
    #filename = wget.download(fig_url)
    print(img_url)

# Metadata contents
name_tag = soup.find_all("span",{"class":"species-common-name"})
for name in name_tag:
    print(name.string)

scname_tag = soup.find_all("i",{"class":"species-scientific-name"})
for scname in scname_tag:
    print(scname.string)

loc = soup.find_all("a",{"class":"mod-stealth"})[2]
'''
i = 0
for line in loc:
    #print("[{}] {}".format(i,line))
    i += 1
'''
print(loc.text.strip())


#print(name_tag)
