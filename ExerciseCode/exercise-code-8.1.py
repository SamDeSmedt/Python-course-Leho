#!/usr/bin/python3
################################################################################
# Get information from https://www.rcsb.org/annotations/2BE9
################################################################################
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
#connect to the PDBE website
print("\nPDBE search with modified user-agent:")
url = 'https://www.rcsb.org/annotations/2BE9'
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
request = urllib.request.Request(url, headers = headers)
response = urllib.request.urlopen(request)
response_data = response.read()
soup = BeautifulSoup(response_data, 'html.parser')
#print(soup)
# Extract the SCOP/SCOPe Classification table
tag_table = soup.find("table", {"class":"table table-bordered annotations"})
################################################################################
# Identify each value and save in Excel document
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "PDBE 2BE9"
# Retrieve the heading of the table
header_table = tag_table.find_all("th")
ws.append([header_table[0].text.strip(), header_table[1].text.strip(), header_table[2].text.strip(), header_table[3].text.strip(), header_table[6].text.strip()])

# Retrieve rows of the table
tr_table = tag_table.find_all("tr")

# Iterate over each row
for row in tr_table:
    # Retrieve cells of the row
    td_row = row.find_all("td")
    if len(td_row) > 0:
        # Extract values from cells
        chains = td_row[0].text.strip()
        domain_info = td_row[1].text.strip()
        class_ = td_row[2].text.strip()
        fold = td_row[3].text.strip()
        domain = td_row[6].text.strip()
        # Append to workbook
        ws.append([chains, domain_info, class_, fold, domain])

        # Print values
        print("\nChains: {}".format(chains))
        print("Domain info: {}".format(domain_info))
        print("Class: {}".format(class_))
        print("Fold: {}".format(fold))
        print("Domain: {}".format(domain))
# Save workbook
wb.save("PDBE_annotation.xlsx")




    
