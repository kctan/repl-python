from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

site= "https://www.tabletennis11.com/other_eng/butterfly-viscaria"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page, 'html.parser')

elements = soup.select("#product_addtocart_form > div.price-container.eng > div > div") # 133.25

price = elements[0].text
print("Current Price: " + elements[0].text)


import datetime

x = datetime.datetime.now()
date_time = x.strftime("%m/%d/%Y, %H:%M")

helloFile = open("table-tennis.txt", "a")
helloFile.write(date_time + "\tprice: " + price[1:] + "\n")
helloFile.close()
