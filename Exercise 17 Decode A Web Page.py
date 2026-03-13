# Use the BeautifulSoup and requests Python packages to print out a list of all the
# article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

nyt = requests.get('https://www.nytimes.com/')
soup = BeautifulSoup(nyt.text, 'html.parser')

print(soup.title.string)
for headline in soup.find_all('p'):
    if soup.find_all('h2') or soup.find_all('h3') not in headline:
        print(headline.text)