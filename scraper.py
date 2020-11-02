import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import csv
import re

url = 'https://www.willdrinkfortravel.com/posts/black-owned-restaurants-you-need-to-visit-in-baltimore'
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

# gets everything between the ()
addressregx = re.compile(r'(?<=\().+(?=\))')

with open('restaurants.csv', mode='w', newline='') as restaurants:
  rest_writer = csv.writer(restaurants, delimiter=',', quotechar='"')
  for i, listing in enumerate(soup.find_all('li')):
    name = listing.a.string
    link = listing.a.get('href')
    text = ''
    if len(listing.p.contents) > 1:
      text = listing.p.contents[1]
    addressmatch = addressregx.search(text)
    address = addressmatch.group(0)
    print(address)
    rest_writer.writerow([name, link, address])

# [^\(].+(?=\))
# [?<=\w].+(?=\))
# (?<=\().+(?=\))