import requests
import pandas as pd
from bs4 import BeautifulSoup


url = 'https://steamcommunity.com/market/search?appid=252490'

skins_list = {}
skin_no = 0
while True:
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    skins = soup.find_all('div',{'class' : 'market_listing_row market_recent_listing_row market_listing_searchresult'})


    for skin in skins:
        price = skin.find('span', {'class' : 'normal_price'})
        name = skin.find('span', {'class': 'market_listing_item_name'})
        skin_no += 1
        skins_list[skin_no] = [name, price]


df = pd.DataFrame.from_dict(skins_list, orient = 'index', columns = ['Name','Price'])
df.to_csv('npo_jobs.csv')