from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import Request,urlopen


req = Request('https://steamcommunity.com/market/search?appid=252490#p1_popular_desc' , headers ={'User-Agent':'Mozilla/5.0'})
webpage = urlopen(req).read()


soup = BeautifulSoup(webpage,'html')
skin_name_html = [i for i in soup.find_all(class_ = 'market_listing_item_name')]
skin_name = list()
for i in range(len(skin_name_html)):
    skin_name.append(skin_name_html[i].text)
print(skin_name_html)


skin_price_html = [i for i in soup.find_all(class_ = 'sale_price')]
skin_price = list()
for i in range(len(skin_price_html)):
    skin_price.append(skin_price_html[i].text)
print(skin_price)


dict1 = dict(zip(skin_name, skin_price))
print(dict1)


rate_df = pd.DataFrame.from_dict(dict1, orient='index')
rate_df.to_csv('skins_prices.csv')
