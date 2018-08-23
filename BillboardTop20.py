import requests
from bs4 import BeautifulSoup as BS

url = 'https://www.billboard.com/charts/hot-100'

url = requests.get(url)

soup = BS(url.content,'html.parser')

#soup = soup.prettify() Causes error with soup.find

no_1_song = soup.find('div',{'class': 'chart-number-one__title'}).text

no_1_artist = soup.find('div',{'class': 'chart-number-one__artist'}).text
#print(soup.find_all('div',{'class':'chart-list-item__title'})) Broader search

top100songs = soup.find_all('span',{'class':'chart-list-item__title-text'})

top100artist = soup.find_all('div',{'class':'chart-list-item__artist'})

number = soup.find_all('div',{'class':'chart-list-item__rank'})

print ("1 " + no_1_song  + no_1_artist )
for i in range(19):

    print (number[i].text + top100songs[i].text  + top100artist[i].text)

