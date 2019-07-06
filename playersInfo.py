from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup
import re

url = "https://www.basketball-reference.com/players/a/abdelal01.html"
html = urlopen(url)
bsObj = BeautifulSoup(html, features='html.parser')

playerList = bsObj.findAll("div",{"itemtype": "https://schema.org/Person"})

for PL in playerList:
     playerName = (playerList.findAll(lambda tag:[a for a in tag.attrs if a[0].startswith('name')]))
                        #playerPosition = (playerList.find("Strong"))
                        playersWeight = (playerList.findAll("span",{"itemprop":"Height"}))
                        playersHeight = (playerList.findAll("span", {"itemprop":"weight"}))
                        playersBirthDate  = (playerList.findAll(link.attrs['data-birth']))
                        playersBirthPlace = (playerList.findAll("span",{"itemprop":"birthPlace"}))
                        print(playerName)