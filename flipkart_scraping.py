from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re
driver = webdriver.Chrome()


def pages_url():
    pages_url = []
    for x in range(1, 11):
        url = f"https://www.flipkart.com/search?q=spirulina&page={x}"
        pages_url.append(url)
    return pages_url


def product_links(pages_url):

    product_links_list = []
    for items in pages_url:
        driver.get(items)
        content = driver.page_source
        soup = BeautifulSoup(content)
        base_url = 'https://www.flipkart.com'
        for item in soup.select('[data-id]'):
            product_url = base_url + item.select('a')[0]['href']
            product_links_list.append(product_url)
    return product_links_list


def get_product_details(product_links_list):

    product_details = []
    for item in product_link_list:
        driver.get(item)
        content = driver.page_source
        soup = BeautifulSoup(content)
        try:
            name = soup.p.text.strip()
            prices = soup.find_all(text=re.compile('₹'))[0].strip().replace('₹', '')
            original_price = soup.find_all(text=re.compile('₹'))[2].replace('₹', '').strip()
            offer = soup.find_all(text=re.compile('off'))[0].split()[0]
            ratings = soup.select('[id*=productRating]')[0].get_text().strip()
            seller_name = soup.select('[id*=sellerName]')[0].get_text().strip()[:-3]
            seller_rating = soup.select('[id*=sellerName]')[0].get_text().strip()[-3:]
            brand = soup.select('li._21lJbe')[0].get_text().strip()
            model_name = soup.select('li._21lJbe')[1].get_text().strip()
            model_number = soup.select('li._21lJbe')[2].get_text().strip()
            qty = soup.select('li._21lJbe')[3].get_text().strip()
            type_ = soup.select('li._21lJbe')[4].get_text().strip()
            form = soup.select('li._21lJbe')[5].get_text().strip()
            package = soup.select('li._21lJbe')[9].get_text().strip()
            self_life = soup.select('li._21lJbe')[8].get_text().strip()
            serving_size = soup.select('li._21lJbe')[10].get_text().strip()
            rating_count = soup.select('span._2_R_DZ')[0].get_text().strip()[0]
        except Exception as e:
                #raise e
                b = 0
        log = { 
            'name': name,
            'price': prices,
            'original_price': original_price,
            'offer': offer,
            'rating': ratings,
            'rating_count': rating_count,
            'seller_name': seller_name,
            'seller_rating': seller_rating,
            'brand': brand,
            'model_name': model_name,
            'model_number': model_number,
            'qty': qty,
            'type': type_,
            'form': form,
            'package': package,
            'self_life': self_life,
            'serving_size': serving_size
        
        }
        product_details.append(log)
