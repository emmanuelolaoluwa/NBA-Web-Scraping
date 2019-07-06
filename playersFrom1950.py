from urllib.request import urlopen
from bs4 import BeautifulSoup

alphabets = ["a","b","c","d","e","f","g","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y","z"]

for x in alphabets:
    print("Players Whose name starts with ", x )
    url = "https://www.basketball-reference.com/players/" + x + "/"
    html = urlopen(url)



    soup = BeautifulSoup(html)

    p = soup.findAll('tr')
    p1 = soup.findAll('th')[8:]

    playerNames = [names.getText() for names in soup.findAll('th')[8:]]    

    data_rows = soup.findAll('tr')[1:]

    careers = [[td.getText() for td in data_rows[i].findAll('td', limit=1)] for i in range(len(data_rows))] 

    for i in range(len(careers)):
        for j in range(len(careers[i])):
            
            if "1950" < careers[i][j]:
                print(playerNames[i], " ", careers[i][j])
        
    