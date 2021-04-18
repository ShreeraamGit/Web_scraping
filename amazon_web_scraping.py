#Import Libraries.
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd

s = HTMLSession()
base_url = 'https://www.amazon.in/'
term = input("Enter the search term to collect data.?\n").capitalize()
url = f'https://www.amazon.in/s?k={term}'
url_list = []
asins = []
product_list = []


def getdata(url):

    r = s.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def getnextpage(soup):

    page = soup.find('ul', {'class': 'a-pagination'})  
    if not page.find('li', {'class': 'a-disabled a-last'}):
        pages_url = base_url + str(page.find('li',{'class':'a-last'}).find('a')['href'])
        return pages_url
    else:
        return


def getasin(pages_url):

    '''
    This function is used to
    get the asin of all products
    int he given url

    This function accepts url as an
    arguement.

    this function returns a
    list of asins.
    '''

    r = s.get(pages_url)
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
    df.to_csv("output.csv", index=False)


print(f'The search term is: {term}')
print('\nSession Started.....')
print('\nData Collection is In Process.Please Wait.....')

while True:

    soup = getdata(url)
    url = getnextpage(soup)
    url_list.append(url)
    if not url:
        break
url_list = url_list[:-1]

print('\nTotal pages to naviagte: ', len(url_list))

for items in url_list:
    asin_list = getasin(items)

print(f'\nTotal Products to be scraped:{len(asin_list)}')
print('\nData Collection is In Process.Please Wait.....\n')

data = getproductdetails(asin_list)

output(data)
print('\nSession Complete..Output CSV file is ready and Saved..')
