from bs4 import BeautifulSoup
from urllib3 import poolmanager
import requests
import os
import unidecode
import re
import html5lib

connectBuilder = poolmanager.PoolManager()

url='http://www.imdb.com/title/tt0472954/epdate'
r = requests.get(url)
soup = BeautifulSoup(r.content, "html5lib")
soup = soup.findAll("td" , {"align":"right"})


counter=0
temparray=[]
epRatingArray=[]
for td in soup:
    if unidecode.unidecode(td.text) == '- ':
        break
    elif counter == 0:
        temparray+=[str(re.sub(r'\ ','',unidecode.unidecode(td.text)))]
        counter+=1
    elif counter == 1:
        temparray+=[float(unidecode.unidecode(td.text))]
        counter+=1
    else:
        temparray+=[int(unidecode.unidecode(re.sub(r',','',td.text)))]
        epRatingArray+=[temparray]
        temparray=[]
        counter=0
#print(epRatingArray)


f = open("asd-imdb-ratings.txt", "w+")
f.write(str(epRatingArray))
f.close()
