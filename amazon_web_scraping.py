#Import Libraries.
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd

s = HTMLSession()
product_list = []
asins = []


def getasin(url):

    '''
    This function is used to
    get the asin of all products
    int he given url

    This function accepts url as an
    arguement.

    this function returns a
    list of asins.
    '''

    r = s.get(url)
    r.html.render(sleep=1)
    products = r.html.find('div[data-asin]')
    for product in products:
        asin = product.attrs['data-asin']
        if asin != '':
            asins.append(asin)
    return asins


def getproductdetails(asin_list):

    '''
    This function fetches details
    from the asin which is stored in as
    a list.

    This function takes a list with asins from
    def getasin(url)

    this function returns a dict with
    name,price,rating,review_count,soldby,
    brand
    '''

    for items in asin_list:
        url = f'https://www.amazon.in/dp/{items}'
        r = s.get(url)
        r.html.render(sleep=1)

        try:
            name = r.html.find('#productTitle', first=True).full_text.strip()
        except:
            name = "NA"
        try:
            rating = r.html.find('span.a-icon-alt', first=True).full_text
        except:
            rating = 'NA'
        try:
            review_count = r.html.find('#acrCustomerReviewText', first=True).full_text
        except:
            review_count = 'NA'
        try:
            sold_by = r.html.find('#sellerProfileTriggerId', first=True).full_text.strip()
        except:
            sold_by = 'NA'
        try:
            brand = r.html.find('#bylineInfo', first=True).full_text.strip()
        except:
            brand = "NA"
        try:
            price = r.html.find('#priceblock_ourprice', first=True).full_text.strip()
        except:
            price = "NA"

        log = {

            'product_name': name,
            'product_rating': rating,
            'sold_by': sold_by,
            'product_price': price,
            'product_brand': brand,
            'reviews_count': review_count,

        }

        product_list.append(log)
        print('\nSaving...', log['product_name'])
    return product_list


def output(data):

    '''
    this function is used to
    convert the dict
    from the getproductdetails
    to DataFrame.

    this function accepts the dict as the
    arguement
    '''
    df = pd.DataFrame(data)
    print(df.shape)
    df.to_csv("spirulina_new.csv", index=False)


print('\nSession Started.....')
print('\nData Collection is In Process.Please Wait.....')

for x in range(1, 7):
    url = f'https://www.amazon.in//s?k=spirulina&page={x}&qid=1618395019&ref=sr_pg_1'
    asin_list = getasin(url)

print(f'\nTotal Products to be scraped:{len(asin_list)}')
print('\nData Collection is In Process.Please Wait.....')
data = getproductdetails(asin_list)

output(data)
print('\nSession Complete..Output CSV file is ready and Saved..')
