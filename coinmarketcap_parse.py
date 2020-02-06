from bs4 import BeautifulSoup




f = open("html_files/coinmarketcap20200130162810.html", "r")

soup = BeautifulSoup(f.read(), 'html.parser')
f.close()

currencies_table = soup.find("tbody")





currency_rows = currencies_table.find("tr")

currency_price = currency_rows.find("td",{"class":"cmc-table__cell--sort-by__price"}).find("a").text
currency_name = currency_rows.find("td",{"class":"cmc-table__cell--sort-by__name"}).find("a",{"class":"cmc-link"}).text



# currencies_row = currencies_table.find("tr")
# currency_price = currency_row.find("td",{"class":"cmc-table__cell--sort-by__price"}).find("a").text
# currency_name = currency_row.find("td",{"class":"cmc-table__cell--sort-by__name"}).find("a",{"class":"cmc-link"}).text
#currency_marketcap=currency_row.find("td",{"class":"cmc-table__cell--sort-by__market-cap"})
#currency_supply=


print(currency_price)
print(currency_name)

#print(soup)
#html_content=f.read()
#print(html_content)
