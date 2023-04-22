#!/usr/bin/python3
################################################################################
# Accessing the internet and use the search function
################################################################################
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
"""
# Data from Human Cell Atlas
# https://data.humancellatlas.org/apis
################################################################################
print("\nSearch on human cell atlas REST web service:")
# Get content data using urllib and create soup object
url = "https://service.azul.data.humancellatlas.org/index/catalogs"
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
try:
    request = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(url)
    content = response.read().decode("utf-8")
    soup = BeautifulSoup(content, 'html.parser')
    # Print parse tree in better format
    print(soup.prettify())
    save_file = open('urllib_hca_api.json','w')
    save_file.write(str(content))
    save_file.close()
except Exception as e:
    print(str(e))
"""
################################################################################
# Data from Pfam
# http://pfam.xfam.org/
################################################################################
print("\nSearch on pfam:")
url = "http://pfam-legacy.xfam.org/search/keyword?query=caspase"
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
try:
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    response_data = response.read().decode("utf-8")
    soup = BeautifulSoup(response_data,"html.parser")
    print(soup)
    save_file = open('urllib_pfam_api.html','w')
    save_file.write(str(response_data))
    save_file.close()
except Exception as e:
    print(str(e))
