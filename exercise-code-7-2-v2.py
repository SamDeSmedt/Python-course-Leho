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
import csv

# Get content data using urllib and create soup object
# Hardcoded URL
#url = "https://waarnemingen.be/photos/?date_after=2023-04-23&date_before=2023-04-25&species=&species_group=4&country_division=17&rarity=1&page=1"

'''
# Retrieving Get variables

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

'''
date_after = input ("\nGive date after (in YYYY-MM-DD format): ")
date_before = input ("\nGive date before (in YYYY-MM-DD format): ")
species_input = input("\nSpecies groups: [1] Birds | [2] Mammals | [3] reptiles and amphibians | [4] Butterflies\nGive number of species group: ")
provinces_input = input("\nProvinces: [14] Limburg | [15] West-Vlaanderen | [16] Oost-Vlaanderen | [17] Antwerpen\nGive number of province: ")
rarities_input = input("[1] >=common | [2] >=relatively common | [3] >=rare | [4] very rare\nGive number of rarity: ")

base_url = "https://waarnemingen.be"    
params = urllib.parse.urlencode({'date_before': date_before, 'date_after': date_after, 'species_group': species_input, 'country_devision': provinces_input})
url = "https://waarnemingen.be/photos/?%s" % params

print("="*100)
print("Running photo collecotor script\n{}".format(url))
print("="*100)

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"

# Create directory for pictures to store
pic_loc = os.getcwd()+"/Pictures"
# Check if location exists
if os.path.exists(pic_loc):
    os.chdir(pic_loc)
else:
    os.mkdir("Pictures")
    os.chdir(pic_loc)

# Opening csv file to write in
with open("metadata.csv", mode = "w") as md_file:
    md_writer = csv.writer(md_file, 
    delimiter=';', 
    quotechar='"', 
    quoting=csv.QUOTE_MINIMAL)
    # Write heading to csv file
    md_writer.writerow(["id","scientific name", "common name", "location", "photo name"])
    i = 0

    # Get content data using urllib and create soup object
    response = urllib.request.urlopen(url)
    content = response.read()
    soup = BeautifulSoup(content, "html.parser")

    # Tag (figure) contents
    figure_tag = soup.find_all("figure","lightbox-gallery")
    
    for fig in figure_tag:
        # Print the hits for this tag
        #print("[{}] {}".format(i,fig))
        i += 1
        # Look in this tag for the url links
        # Tag (img) contents
        img_tag = fig.find("img",{"loading":"lazy"})
        image_name = img_tag["src"]
        img_url = base_url + image_name.replace("?w=500&h=375","")
        # Download image
        filename = wget.download(img_url)
        print("\nImage: {}".format(img_url))
        # Look in this tag for common name
        name_tag = fig.find("span",{"class":"species-common-name"})
        print("Species common name: {}".format(name_tag.string))
        # Look in this tag for scientific name
        scname_tag = fig.find("i",{"class":"species-scientific-name"})
        print("Sprecies scientific name: {}".format(scname_tag.string))
        # Look for location in the file
        loc = fig.find_all("a", "mod-stealth")[2]
        print("Location: {}".format(loc.text.strip()))
        #for inf in loc:
            #print("[{}] {}".format(i,inf))
            #i += 1
        #Look for person who took the picture
        # Write metadata to a file
        md_writer.writerow([i,name_tag.string, scname_tag.string, loc.text.strip(), filename])
        
# Close csv file
md_file.close()
        


