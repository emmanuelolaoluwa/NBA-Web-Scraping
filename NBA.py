from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup

alphabets = ["a"]
#,"b","c","d","e","f","g","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y","z"]

for x in alphabets:
    print("Players Whose name starts with ", x )
    try:
       
        url = "https://www.basketball-reference.com/players/" + x + "/"
        html = urlopen(url)

        soup = BeautifulSoup(html,'html.parser')

        soup.findAll('tr', limit=2)
        headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
        headers = headers[:1]

        rows = soup.findAll('tr')[:1]
        for th in soup.findAll('th')[8:]:
            #print(th.getText()," ")
            #end = '')
            for link in th.findAll("a"):
                if 'href' in link.attrs:
                    Link = "https://www.basketball-reference.com"+link.attrs['href']
                    html = urlopen(Link)
                    
                    bsObj = BeautifulSoup(html,'html.parser')

                    playerList = bsObj.findAll("div",{"id": "meta"})
                    for name in playerList:
                        pictureLink = name.findAll("img")
                        if 'img' in pictureLink.attrs:
                            print("Work on picture link later", pictureLink.attrs['img'])
                        else:
                            print("-----------------------------------------")
                            print(name.getText())
                            print("-----------------------------------------")

    except urllib.HTTPError:
        continue