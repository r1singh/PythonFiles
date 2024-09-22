import requests
from bs4 import BeautifulSoup 


response = requests.get('https://quotes.toscrape.com/')
soup=BeautifulSoup(response.text,'lxml')
qoutes = soup.find_all('span',class_='text')
author = soup.find_all('small',class_='author')
tags = soup.find_all('div', class_='tags')
tagtext=''
for i in range(0,len(qoutes)):
    print(qoutes[i].text)
    print(author[i].text)
    finaltag= tags[i].find_all('a',class_='tag')
    for j in finaltag:
        tagtext+=j.text+" "
    print(tagtext)
    tagtext=''
    print('--'*50)
