from bs4 import BeautifulSoup
import requests
import wget

url = input('Enter the url: ')
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

#get all the pdf files
links = soup.find_all('a')
for link in links:
    if 'pdf' in link.get('href'):
        print(link.get('href'))
        wget.download(link.get('href'))