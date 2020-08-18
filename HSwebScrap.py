import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
import warnings
warnings.filterwarnings('ignore')

#target url
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
url = requests.get('http://www.investing.com/indices/hong-kong-40-futures-historical-data', headers=headers)

#load data into bs4
soup = BeautifulSoup(url.text, 'html.parser' )

#web scaraper
def get_website_data():
    record = []
    head = soup.find('table', { 'id': 'curr_table'})
    tbody = head.find('tbody')
    for tr in tbody.find_all('tr'):
        date = tr.find_all('td')[0].text.strip()
        price = tr.find_all('td')[1].text.strip()
        opn = tr.find_all('td')[2].text.strip()
        high = tr.find_all('td')[3].text.strip()
        low = tr.find_all('td')[4].text.strip()
        vol = tr.find_all('td')[5].text.strip()
        change = tr.find_all('td')[6].text.strip()
        record.append((date,price,opn,high,low,vol,change))
    return record

#into dataframe then excel
record = get_website_data()
df = pd.DataFrame(record, columns=['Date','Price','Open','High','Low','Vol','Change'])
df.to_excel("HangSengHistoricalData.xlsx",index=False, header=True)