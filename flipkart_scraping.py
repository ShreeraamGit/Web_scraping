from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re
driver = webdriver.Chrome()

pages_url = []
for x in range(1, 11):
    url = f"https://www.flipkart.com/search?q=spirulina&page={x}"
    pages_url.append(url)

details = []
for links in pages_url:
    driver.get(links)
    content = driver.page_source
    soup = BeautifulSoup(content, features="lxml")
    for item in soup.select('[data-id]'):
        try:
            name = item.select('a img')[0]['alt']
            prices = item.find_all(text=re.compile('₹'))
            ratings = item.select('[id*=productRating]')[0].get_text().strip()
        except Exception as e:
            #raise e
            b = 0
               
        log = {
            
            'name': name,
            'price': prices[0],
            'rating': ratings
        }
        details.append(log)

df = pd.DataFrame(details)
print(df.shape)
df.to_csv("output.csv", index=False)
