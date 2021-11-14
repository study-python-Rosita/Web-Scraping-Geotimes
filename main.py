from bs4 import BeautifulSoup
import requests

source = requests.get('https://geotimes.id/kanal/kolom/').text

soup =  BeautifulSoup(source, 'lxml')

article = soup.find_all('h3')

print(article)



