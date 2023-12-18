'''
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
## In the following segment, I show how you can get a list of news article URLs based on a keyword search.
## I use CNN as an example but news source would work.

base_url = u'https://www.cnn.com/search?q=politics&size=200'

browser.get(base_url)
time.sleep(1)

#Finds the container that contains every news article.
main_news_container = browser.find_element(By.CLASS_NAME, 'Search CNN - Videos, Pictures, and News - CNN.com | CNN')
# main_news_container = browser.find_element(By.CLASS_NAME, 'cnn-search__results-list')
# main_news_container = browser.find_element_by_class_name('cnn-search__results-list')

#In main container get 'a'
text_sections = main_news_container.find_elements(By.XPATH, "//a[@href]")
# text_sections = main_news_container.find_elements_by_xpath("//a[@href]")

for elem in text_sections:
    if "/2020/" in elem.get_attribute("href"):
        #this is printing the link
        print(elem.get_attribute("href"))
        #this is printing the Headline
        print(elem.text)

#Find the text body_elements inside the main_news_container
body_elements = main_news_container.find_elements(By.CLASS_NAME, "cnn-search__result-body")

#this is how you get the body body_elements text
print(body_elements[1].text)

'''



import requests
from bs4 import BeautifulSoup
import pandas as pd

    

def url_is_article(url, current_year='2023'):
    if url:
        if 'cnn.com/{}/'.format(current_year) in url and '/gallery/' not in url:
            return True
    return False

# def parse(html):
#     ...
#     author = soup.find('span', {'class': 'byline__name'})
#     if not author:
#         author = soup.find('span', {'class': 'byline__names'})
#     author = return_text_if_not_none(author)
#     return author



def parse(html):
    soup = BeautifulSoup(html, features="html.parser")
    title = return_text_if_not_none(soup.find('h1', {'class': 'headline__text'}))
    article_content = return_text_if_not_none(soup.find('div', {'class': 'article__content'}))
    author = soup.find('span', {'class': 'byline__name'})
    if not author:
        author = soup.find('span', {'class': 'byline__names'})
    author = return_text_if_not_none(author)
    return title, author, article_content


def return_text_if_not_none(element):
    if element:
        return element.text.strip()
    else:
        return ''
    
all_urls = []
url = 'https://www.cnn.com'
data = requests.get(url).text
soup = BeautifulSoup(data, features="html.parser")
for a in soup.find_all('a', href=True):
    if a['href'] and a['href'][0] == '/' and a['href'] != '#':
        a['href'] = url + a['href']
    all_urls.append(a['href'])
    

article_urls = [url for url in all_urls if url_is_article(url)]

print(len(article_urls))

parse_data_list = []
for article_url in (article_urls):
    data = requests.get(article_url).text
    parse_data_list.append(parse(data))

print(len(parse_data_list))
