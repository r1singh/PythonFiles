import requests
from bs4 import BeautifulSoup
# global variable declared 
count=1  

def requestcall(url='https://scrapingclub.com/exercise/list_basic/'):
    global count #global vairbale is beig used in local scope 
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'lxml')
    tags= soup.find_all('div', class_='p-4')
    
    for tag in tags:
        price= tag.find('h5',class_='')
        articalname=tag.find('h4')
        if articalname != None:
            print(str(count)+") "+articalname.text.strip('\n')+' '+price.text)
            count+=1
    page=allpagesurl(url)
def allpagesurl(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'lxml')
    page=soup.find('nav',class_='pagination')
    links=page.find_all('a')
    urls=[]
    for link in links:
        pageno= int(link.text) if link.text.isdigit() else None
        
        if pageno !=None:
            urls.append('https://scrapingclub.com'+link.get('href'))
    return urls
requestcall()
lst=allpagesurl('https://scrapingclub.com/exercise/list_basic/')
for i in lst:
    requestcall(i)
