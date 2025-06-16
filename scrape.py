# python -m pip install requests
# => get data from web (html, json, xml)
# python -m pip install beautifulsoup4
# parse html

import requests

from bs4 import BeautifulSoup

import json

# import pprint

url = "http://books.toscrape.com/"

def scrape_book(url):
  response = requests.get(url)
  response.encoding = response.apparent_encoding
  if response.status_code != 200:
    return
  
  soup = BeautifulSoup(response.text, "html.parser")
  books = soup.find_all("article", class_ ="product_pod")

  book_data = []

  for book in books:
    title = book.h3.a["title"]
    price_text = book.find("p", class_ = "price_color").text

    currency = price_text[0]
    price = float(price_text[1:])

    book_data.append({
      'title': title,
      'currency': currency,
      'price': price
    })
  
  return book_data

books = scrape_book(url)    


with open("data.json", 'w', encoding= 'utf-8') as f:
  json.dump(books, f, indent=2, ensure_ascii=False)
  
print("Book data saved to data.json")

# pprint.pprint(books)

# go to git bash
# git config --global user.name "Jagadish Bhatta"
# git config --global user.email "jajajjajjaja@gmail.com"

# git init => initialize git
# git status => if you want to chech what are the status of files
# git diff => if you want to check what are the changes
# git add. 
# git commit -m "Your message"
# copy paste git code from github

##########################
# 1. update the code
# 2. git add .
# 3. git commit -m "message"
# 4. git push
###########################