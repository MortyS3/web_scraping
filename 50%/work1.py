from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import Request,urlopen
import csv


req = Request('https://steamcommunity.com/market/search?appid=252490#p1_popular_desc' , headers ={'User-Agent':'Mozilla/5.0'})
webpage = urlopen(req).read()


soup = BeautifulSoup(webpage,'html')
skin_name_html = [i for i in soup.find_all(class_ = 'market_listing_item_name')]
skin_name = list()
for i in range(len(skin_name_html)):
    skin_name.append(skin_name_html[i].text)



skin_price_html = [i for i in soup.find_all(class_ = 'sale_price')]
skin_price = list()
for i in range(len(skin_price_html)):
    skin_price.append(skin_price_html[i].text)


df = pd.DataFrame(skin_name, columns=["Name:"])
df.to_csv('skins_prices.csv')

v = open('skins_prices.csv')
r = csv.reader(v)
row0 = r.next()
row0.append(skin_price)
for item in r:
    item.append(item[0])