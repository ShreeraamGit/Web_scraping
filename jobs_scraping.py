from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re
driver = webdriver.Chrome()


def get_data(url):
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content)
    return soup


def get_details(soup):
    listings = soup.find_all('li', {'class': 'ais-Hits-list-item'})
    for i in listings:
        company = i.find(class_="ais-Highlight-nonHighlighted").get_text().strip()
        post = i.find(class_="sc-1kkiv1h-9 sc-7dlxn3-4 ivyJep iXGQr").get_text().strip()
        contract = i.find(class_="sc-1qc42fc-2 bzTNsD").get_text().strip()
        try:
            location = i.find(class_="sc-1qc42fc-2 fHAhLi").get_text().strip()
        except Exception as e:
            #raise e
            b = 0
        job_link = "https://www.welcometothejungle.com" + i.find('a')['href']

        log = {
            "company_name": company,
            "position": post,
            "contract": contract,
            "location": location,
            "job_link": job_link
        }
        listings_list.append(log)


def get_pages(soup):
    try:
        url = 'https://www.welcometothejungle.com/fr/jobs' + soup.find('a',{'aria-label': "Next page"}).get('href')
        return url
    except AttributeError:
        return None


url = "https://www.welcometothejungle.com/fr/jobs?page=1&aroundQuery=&query=data%20engineer%20&refinementList%5Blanguage%5D%5B%5D=en"
listings_list = []
while True:
    soup = get_data(url)
    url = get_pages(soup)
    if not url:
        break
    print(url)
