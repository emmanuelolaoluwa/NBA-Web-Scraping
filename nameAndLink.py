from urllib.request import urlopen
from bs4 import BeautifulSoup

alphabets = ["a","b","c","d","e","f","g","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y","z"]

for x in alphabets:
    print("Players Whose name starts with ", x )
    url = "https://www.basketball-reference.com/players/" + x + "/"
    html = urlopen(url)
    
    soup = BeautifulSoup(html,'html.parser')

    headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]       
    headers = headers[:1]

    rows = soup.findAll('tr')[:1]
    for th in soup.findAll('th')[8:]:
        print(th.getText()," ")
        
        for link in th.findAll("a"):
            if 'href' in link.attrs:
                Link = "https://www.basketball-reference.com"+link.attrs['href']
                print(Link)