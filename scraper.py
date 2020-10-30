import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import csv

url = 'https://www.willdrinkfortravel.com/posts/black-owned-restaurants-you-need-to-visit-in-baltimore'
response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")
divs = soup.find_all('div')
links = soup.find_all('a')
listings = soup.find_all('li')

# p = soup.find('p')
# p = soup.p['class']
# a = soup.a['href']
# for div in soup.find_all('div'):
#   if div.get('id') == 'item-5e4184b6e6d48704f1813b9b':
#     listings = div
restaurant = []
with open('restaurants.csv', mode='w', newline='') as restaurants:
  rest_writer = csv.writer(restaurants, delimiter=',', quotechar='"')
  for i, listing in enumerate(soup.find_all('li')):
    # restaurant.append(listing) - makes an array of listings
    tag = listing.a
    name = tag.string
    link = listing.a.get('href')
    rest_writer.writerow([name, link])
