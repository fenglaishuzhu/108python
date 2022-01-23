import requests
from bs4 import  BeautifulSoup
import pandas as pd
import  numpy as np
response=requests.get('https://ah.huatu.com/zw/liaoning/shenyangshi/2021.html')
response.status_code
soup=BeautifulSoup(response,'html.parser')

soup.decode

table=soup.find_all('table')

row_names=[th.text for th in soup.find_all('th')]
pd1=pd.DataFrame(row_names)



data_rows=[]

for  tr in soup.tbody.find('tr'):

  row=[tr.text for td in soup.tbody.find_all('tr')]


  data_rows.append(row2)

data_rows

df=pd.DataFrame(data_rows,columns=row_names)
