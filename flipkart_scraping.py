# import Important libraries
from time import sleep
from tqdm import tnrange, tqdm_notebook
from tqdm import tqdm
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re
driver = webdriver.Chrome()


def pages_url():

    '''
    this funtion takes no arguement
    and it returns the urls whihc is
    used for pagination.
    '''
    pages_url = []
    for x in tqdm(range(1, 11), desc='Loading: Pages_URL'):
        sleep(1)
        url = f"https://www.flipkart.com/search?q=spirulina&page={x}"
        pages_url.append(url)
    return pages_url


def product_links(pages_url):

    '''
    this function takes pages_url as
    an arguement from the previous funtion and traverse
    through each link to get each links of the
    products.
    '''
    product_links_list = []
    for items in tqdm(pages_url, desc='Loading: Product_links'):
        sleep(1)
        driver.get(items)
        content = driver.page_source
        soup = BeautifulSoup(content)
        base_url = 'https://www.flipkart.com'
        for item in soup.select('[data-id]'):
            product_url = base_url + item.select('a')[0]['href']
            product_links_list.append(product_url)
    return product_links_list


def get_product_details(product_links_list):

    '''
    this function takes products links
    from the prevuois funtion
    and return the dict of product
    detials whihc has the following
    information,
    name,price,offer,sellername,
    sellerrating,kind,form,qty
    containertype etc.
    '''

    product_details = []
    for item in tqdm(product_links_list, desc='Loading: Collecting Product_details'):
        sleep(.1)
        driver.get(item)
        content = driver.page_source
        soup = BeautifulSoup(content)
        try:
            pr_name_ = soup.p.text.strip()
        except Exception as e:
            #raise e
            b = 0
        try:
            pr_prices_ = soup.find_all(text=re.compile('₹'))[0].strip().replace('₹', '')
        except Exception as e:
            #raise e
            b = 0
        try:
            pr_offer_ = soup.find_all(text=re.compile('off'))[0].split()[0].replace('%', '')
        except Exception as e:
            #raise e
            b = 0
        try:
            rating_1 = soup.select('div._3LWZlK')[0].get_text().strip()
        except Exception as e:
            #raise e
            b = 0
        try:
            seller_name_ = soup.select('div._1RLviY')[0].get_text().strip()[:-3]
        except Exception as e:
            #raise e
            b = 0
        try:
            seller_rating_ = soup.select('div._3LWZlK')[1].get_text().strip()
        except Exception as e:
            #raise e
            b = 0
        try:
            kind_ = soup.select('li._21Ahn-')[0].get_text().strip()
        except Exception as e:
            #raise e
            b = 0
        try:
            form_ = soup.select('li._21Ahn-')[1].get_text().split()[0].strip()
        except Exception as e:
            #raise e
            b = 0
        try:
            qty_ = soup.select('li._21lJbe')[3].get_text().strip()
        except Exception as e:
            #raise e
            b = 0
        try:
            container_type_ = soup.select('li._21lJbe')[9].get_text()
        except Exception as e:
            #raise e
            b = 0
        try:
            ratings_count = soup.select('span._2_R_DZ')[0].get_text().split()[0]
        except Exception as e:
            #raise e
            b = 0
        try:
            reviews_count = soup.select('span._2_R_DZ')[0].get_text().split()[3]
        except Exception as e:
            #raise e
            b = 0

        log = {
            'name': pr_name_,
            'price': pr_prices_,
            'offer_%': pr_offer_,
            'rating': rating_1,
            'seller_name': seller_name_,
            'seller_rating': seller_rating_,
            'qty': qty_,
            'form': form_,
            'package': container_type_,
            'kind': kind_,
            'ratings_count': ratings_count,
            'reviews_count': reviews_count
        }
        product_details.append(log)
    return product_details


def ouput(dict):

    '''
    this function takes the products details
    from the previous funtion as a list and
    return a dataframe.
    '''
    df = pd.DataFrame(products)
    print(df.shape)
    print('----------------------------')
    df.to_csv('output.csv'index=False)
