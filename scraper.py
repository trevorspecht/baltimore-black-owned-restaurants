import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import csv
import re

# get web page and parse html into soup object
url = 'https://www.willdrinkfortravel.com/posts/black-owned-restaurants-you-need-to-visit-in-baltimore'
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

# gets everything between the ()
addressregex = re.compile(r'(?<=\().+(?=\))')
# gets everything after the ()
descregex = re.compile(r'(?<=\) ).+')

with open('restaurants.csv', mode='w', newline='') as restaurants:
  rest_writer = csv.writer(restaurants, delimiter=',', quotechar='"')
  text = ''
  address = ''
  description = ''
  # iterates over <li> tags
  for i, listing in enumerate(soup.find_all('li')):
    # parse name and link from <a> tags
    name = listing.a.string
    link = listing.a.get('href')
    # isolate text in <p> tags
    if len(listing.p.contents) > 1:
      text = str(listing.p.contents[1])
    # isolate address
    addressmatch = addressregex.search(text)
    if addressmatch:
      address = addressmatch.group(0)
    # isolate description
    descmatch = descregex.search(text)
    if descmatch:
      description = descmatch.group(0)
    rest_writer.writerow([name, link, address, description])
