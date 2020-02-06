from bs4 import BeautifulSoup
import os
import pandas as pd
import glob



if not os.path.exists("parsed_files"):
    os.mkdir("parsed_files")

df = pd.DataFrame()

for one_file_name in glob.glob("html_files/coin*.html"):

   print("parsing: " ,one_file_name)

   scrapping_time = os.path.basename(one_file_name).replace("coinmarketcap","").replace(".html","")
   f = open(one_file_name, "r")

   html_content = f.read()

   soup = BeautifulSoup(html_content, 'html.parser')
   f.close()





   currencies_table = soup.find("tbody")

   #print(currencies_table)



   currency_rows = currencies_table.find_all("tr")
   print("***********")
   print(len(currency_rows))
   print("***********")

   for r in currency_rows :
       currency_price = r.find("td",{"class":"cmc-table__cell--sort-by__price"}).find("a").text
       currency_name = r.find("td",{"class":"cmc-table__cell--sort-by__name"}).find("a",{"class":"cmc-link"}).text
       currency_volume = r.find("td",{"class":"cmc-table__cell--sort-by__volume-24-h"}).find("a",{"class":"cmc-link"}).text

       df =df.append({
			'time': scrapping_time,
			'name': currency_name,
			'price': currency_price,
      'volume':currency_volume
			}, ignore_index=True)

   #print(currency_name)
   #print(currency_name)


#currencies_row = currencies_table.find("tr")
#currency_price = currency_row.find("td",{"class":"cmc-table__cell--sort-by__price"}).find("a").text
#currency_name = currency_row.find("td",{"class":"cmc-table__cell--sort-by__name"}).find("a",{"class":"cmc-link"}).text
#currency_marketcap=currency_row.find("td",{"class":"cmc-table__cell--sort-by__market-cap"})
#currency_supply=


# print(currency_price)
# print(currency_name)



df.to_csv("parsed_files/coinmarketcap_dataset.csv")


#print(df)





#print(soup)

#html_content=f.read()
#print(html_content)























