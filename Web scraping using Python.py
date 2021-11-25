from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi"
req = requests.get(url)
content = BeautifulSoup(req.content, 'html.parser')

name = content.find_all("div", {"class": "_4rR01T"})
price = content.find_all("div", {"class": "_30jeq3 _1_WHN1"})
rating = content.find_all("div", {"class": "_3LWZlK"})

nm = []
pr = []
rt = []

for i in name:
    nm.append(i.text)
for i in price:
    pr.append(i.text)
for i in range(len(nm)):
    rt.append(rating[i].text)

data = {"NAME": nm, "PRICE": pr, "RATING": rt}
df = pd.DataFrame(data)
print(df)
