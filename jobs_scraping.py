from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re
from dateutil import parser
import pandas as pd
import time
import datetime
import os
driver = webdriver.Chrome()
records = []


def get_search_term():
    print("Please enter your 'Dream Job'. NOTE: Enter not more than two space separated terms: For example - data analyst,data engineer")
    print("-" * 115)
    user_input = input("Enter the search term.").lower()
    user_input = user_input.split()
    first_term = user_input[0]
    second_term = user_input[1]
    return first_term, second_term


def get_url(first_term, second_term):
    url = f"https://www.welcometothejungle.com/fr/jobs?page=1&aroundQuery=&query={first_term}%20{second_term}%20&refinementList%5Blanguage%5D%5B%5D=en"
    return url


def get_data(url):
    driver.get(url)
    time.sleep(4)
    content = driver.page_source
    time.sleep(4)
    soup = BeautifulSoup(content, features="lxml")
    return soup


def get_details(soup):
    global location
    listings = soup.find_all('li', {'class': 'ais-Hits-list-item'})
    for i in listings:
        company = i.find(class_="ais-Highlight-nonHighlighted").get_text().strip()
        post = i.find(class_="sc-1kkiv1h-9 sc-7dlxn3-4 ivyJep iXGQr").get_text().strip()
        contract = i.find(class_="sc-1qc42fc-2 bzTNsD").get_text().strip()
        try:
            location = i.find(class_="sc-1qc42fc-2 fHAhLi").get_text().strip()
        except Exception as e:
            location = "Full Remote/Partial Remote"
        job_link = "https://www.welcometothejungle.com" + i.find('a')['href']
        for j in i.findAll('time'):
            if j.has_attr('datetime'):
                dt = j['datetime']
                date = parser.parse(dt).strftime('%B %d, %Y')
        log = {
            "company_name": company,
            "position": post,
            "contract": contract,
            "location": location,
            "job_link": job_link,
            "post_date": date
            }
        records.append(log)
    return


def get_pages(soup):
    try:
        url = 'https://www.welcometothejungle.com/fr/jobs' + soup.find('a', {'aria-label': "Next page"}).get('href')
        return url
    except AttributeError:
        return


def get_output(records):
    root = "/Users/shreeraamalagarsamysethuraj/Desktop/job_scraping_output_files"
    date = datetime.datetime.today().strftime('%d-%m-%Y')
    final = os.path.join(root, "jobs_extract_wtj_" + first_term + second_term + date +".csv")
    df = pd.DataFrame(records)
    df.to_csv(final, index=False, header=True)
    return df.head()


first_term, second_term = get_search_term()
url = get_url(first_term, second_term)
while True:
    soup = get_data(url)
    get_details(soup)
    url = get_pages(soup)
    if not url:
        break
    else:
        print(url)
get_output(records)
driver.quit()
