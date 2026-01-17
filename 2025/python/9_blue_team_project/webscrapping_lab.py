import requests
from bs4 import BeautifulSoup

URL = "https://www.projecthoneypot.org/list_of_ips.php"
html_content = requests.get(URL)
soup = BeautifulSoup(html_content.text, 'html.parser')

#inside of the URL that we defined, it will extract information from the table "manmx"
# and inside of that table it will look for each row "tr"
#for each row, it will look for the cell "td" that contains an anchor tag with the class "bnone"
#it will extract the text from that cell, strip any extra whitespace, and add it to the list of ip_addresses
ip_addresses = []
for row in soup.select('table.manmx tr'):
    ip_cell = row.select_one('td a.bnone')
    if ip_cell:
        ip_addresses.append(ip_cell.text.strip())

for ip in ip_addresses:
    print(ip)

