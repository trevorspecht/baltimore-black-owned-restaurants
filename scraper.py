import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import csv

url = 'https://www.willdrinkfortravel.com/posts/black-owned-restaurants-you-need-to-visit-in-baltimore'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
data = soup.find_all('p')
# print(soup.find_all('p'))
# print(soup.get_text())
with open('restaurants.csv', mode='w') as restaurants:
  rest_writer = csv.writer(restaurants, delimiter=',', quotechar='"')
  rest_writer.writerow(data)