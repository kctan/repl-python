#https://www.fortytwo.sg/dining/dining-tables/landon-regular-dining-table-coffee.html

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

site= "https://www.fortytwo.sg/dining/dining-tables/landon-regular-dining-table-coffee.html"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page, 'html.parser')


elements = soup.select("#product-price-46728") # $69.90 
print(elements)
price = elements[0].text
print("Current Price: " + elements[0].text)

#old-price-46728
elements = soup.select("#old-price-46728")  #  $129.90
print("\nOld Price: " + elements[0].text)


elements = soup.select('div[class="delivery est-date"]')  #  Earliest by Sunday, 31 May 2020
print(elements[0].text)
#print("\nDelivery Date: " + elements[0])


import datetime

x = datetime.datetime.now()

helloFile = open("table.txt", "a")
helloFile.write(str(x) + "\tprice: " + price + "\n")
helloFile.close()
