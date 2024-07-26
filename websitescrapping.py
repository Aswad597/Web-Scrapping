import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import os
import sys




response = requests.get("https://saamaan.pk/collections/gaming")


soup = BeautifulSoup(response.content, "html.parser")


products = soup.find_all("div", class_="product-item__info-inner")


D = []
for product in products:
    productname = product.find("a", class_="product-item__title")
    productprice = product.find("span", class_="price")
    
   
    if productname:

      name = productname.get_text(strip=True)

    else:
      
          name = "No name found"
    
    if productprice:
        price_text = productprice.get_text(strip=True)


        #for removing text in Price column like: Sales Rs;3343,43
       
        price = re.sub(r'[^\d]', '', price_text)
    else:
        price = "No price found"
    
    D.append({"Name": name, "Price": price})


df = pd.DataFrame(D)

if os.path.isfile(r'C:\Users\kk\GamingProductsfrom.csv'):
   print("File exists")  

   sys.exit()

else: 
 df.to_csv("GamingProductsfrom.csv", index=False)

print("File saved to GamingProductsfrom.csv!!!")
