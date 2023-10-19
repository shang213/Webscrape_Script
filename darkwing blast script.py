from bs4 import BeautifulSoup as bs4
import requests as req
from csv import writer

url = "https://shop.tcgplayer.com/price-guide/yugioh/darkwing-blast"
page = req.get(url)

#print(page)                                             #response 200 means it is a successful response. check http resonse status codes.

soup = bs4(page.content, 'html.parser')                     #load HTMLparser from bs4
table_body = soup.find('tbody')                             #find table body
#print(soup)

rows = table_body.find_all('tr')                            #find all tr tags within table body

# for name in rows:                                           #run a for loop to search table body and find div tags in class productdetail and print the a-tag text
#     name = name.find('div', class_="productDetail")
#     #print(name.a.text)
# for rarity in rows:
#     rarity = rarity.find('td', class_="rarity")
#     #print(rarity.text.strip())
# for price in rows:
#     price = price.find('td', class_="marketPrice")
#     print(price.text.strip())
with open('Darkwing Blast.csv', 'w', encoding='utf8', newline='') as f:          #create a csv file that can write
    thewriter = writer(f)
    header = ['Title', 'Rarity', 'Price', 'Quantity']
    thewriter.writerow(header)
    for row in rows:
        name = row.find('div', class_="productDetail").text.strip()
        rarity = row.find('td', class_='rarity').text.strip()
        price = row.find("td", class_="marketPrice").text.strip()
        info = [name, rarity, price]
        thewriter.writerow(info)
        #print(info)

