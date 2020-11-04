import requests
from bs4 import BeautifulSoup
import csv
import re
import geocoder

# get web page and parse html into soup object
url = 'https://www.willdrinkfortravel.com/posts/black-owned-restaurants-you-need-to-visit-in-baltimore'
html = requests.get(url)
soup = BeautifulSoup(html.text, "lxml")

token = 'pk.eyJ1IjoidHJldm9yc3BlY2h0IiwiYSI6ImNrYzJoM2t4ODAxNDAycnF0cHo5eHoybDcifQ.-Pw1y6ZbWuUMooRWmJAK1Q'

# gets everything between the ()
addressregex = re.compile(r'(?<=\().+(?=\))')
# gets everything after the ()
descregex = re.compile(r'(?<=\) ).+')

with open('restaurants.csv', mode='w', newline='') as restaurants:
  rest_writer = csv.writer(restaurants, delimiter=',', quotechar='"')
  # iterates over <li> tags
  for i, listing in enumerate(soup.find_all('li')):
    # initialize variables for each iteration
    text = ''
    address = ''
    description = ''
    latitude = ''
    longitude = ''
    # parse name and web page from <a> tags
    name = listing.a.string
    link = listing.a.get('href')
    # isolate text in <p> tags
    if len(listing.p.contents) > 1:
      text = str(listing.p.contents[1])
    # isolate address
    addressmatch = addressregex.search(text)
    if addressmatch:
      address = addressmatch.group(0)
      # forward geocode map coordinates from address
      geocoderesponse = geocoder.mapbox(address, key=token)
      if geocoderesponse:
        latitude = geocoderesponse.latlng[0]
        longitude = geocoderesponse.latlng[1]
    # isolate description
    descmatch = descregex.search(text)
    if descmatch:
      description = descmatch.group(0)
    # write to csv
    rest_writer.writerow([name, address, latitude, longitude, link, description])
