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
addressregex = re.compile(r'(?<=\().+(?=\))')
# gets everything after the ()
descregex = re.compile(r'(?<=\) ).+')

with open('restaurants.csv', mode='w', newline='') as restaurants:
  rest_writer = csv.writer(restaurants, delimiter=',', quotechar='"')
  for i, listing in enumerate(soup.find_all('li')):
    name = listing.a.string
    link = listing.a.get('href')
    text = ''
    address = ''
    description = ''
    if len(listing.p.contents) > 1:
      text = listing.p.contents[1]
    addressmatch = addressregex.search(text)
    if addressmatch:
      address = addressmatch.group(0)
    descmatch = descregex.search(text)
    if descmatch:
      description = descmatch.group(0)
    print(description)
    rest_writer.writerow([name, link, address, description])
