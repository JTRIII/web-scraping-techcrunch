# Web Scraper for TechCrunch AI Articles

This program scrapes TechCrunch's AI articles and puts their information into an Excel file. 

## Features

- Retrieves title, publication date, athor, main image, and content from article
- Automaticlly goes to the next page to scrape more articles (currently limited to 10)
- The data collected is outputed to an Excel spreadsheet named `techcrunch_ai_articles.xlsx`

## Installation

### Clone the Repository
```
git clone https://github.com/JTRIII/web-scraping-techcrunch.git
```

### Install Required Dependencies
```
pip install pandas beautifulsoup4 requests
```
or 
```
pip3 install pandas beautifulsoup4 requests
```
for Mac or Linux

### Run the Program
```
python webScraper.py
```
or 
```
python3 webScraper.py
```
for Mac or Linux




# Explanation of Code

## Import Dependencies

First, we need to import Requests, BeautifulSoup, and Pandas

The requests module allows us to to send HTTP requests using Python.

BeautifulSoup allows us to parse HTML and XML documents.

Pandas allows us to create and manipulate the data in a spreadsheet format.

```
import requests
from bs4 import BeautifulSoup
import pandas as pd
```

## Initilize the Scraper

The program defines the starting/base url for the TechCrunch AI category. Then it creates an empty Pandas DataFrame to store the article data. 

```
url = "https://techcrunch.com/category/artificial-intelligence/"
bfDataFrame = pd.DataFrame()
```

## Scraping the Articles

The script then enters a loop that scrapes the articles from the first 10 pages of the Techcrunch AI category. For each page:

1. It sends a request to the URL and parses the HTML content using BeautifulSoup.

2. It finds all the links to the individual article pages.

3. For each article link, it sends a request to that page and parses the HTML to extract the following information:
    - Title
    - Publication date
    - Author
    - Featured image URL
    - Content summary

4. It stores this information in a dictionary and appends it to the Pandas DataFrame.

5. It checks if there is a "next page" link and updates the URL accordingly.

```
for page in range(0, 10):
    document = requests.get(url)
    mainbs4Object = BeautifulSoup(document.text, 'html.parser')

    posts = mainbs4Object.select(".loop-card--default a.loop-card__title-link")

    for post in posts:
        link = post['href']
        doc = requests.get(link)
        bs4Object = BeautifulSoup(doc.text, 'html.parser')
        
        # Check for title
        title = bs4Object.select_one('h1').text.strip()

        # Check for both possible date selectors
        date_element = bs4Object.select_one('.wp-block-post-date time') or bs4Object.select_one('span:nth-of-type(3)')
        date = date_element.text.strip() if date_element else "N/A"
        
        # Check for both possible author selectors
        author_element = bs4Object.select_one('a.wp-block-tc23-author-card-name__link') or bs4Object.select_one('a.post-authors-list__author') or bs4Object.select_one('a.wp-block-tc23-author-card-name__link')
        author = author_element.text.strip() if author_element else "N/A"
        
        # Check for Image
        image = bs4Object.select_one('img.attachment-post-thumbnail')['src'] if bs4Object.select_one('img.attachment-post-thumbnail') else "N/A"

        # Check for content
        content = bs4Object.select_one('.entry-content p').text.strip() if bs4Object.select_one('.entry-content p') else "N/A"
        
        print("*******************************")
        print("Title:", title)
        # print("Date:", date)
        # print("Author:", author)
        # print("Image URL:", image)
        # print("Content:", content)
        
        dict1 = {"Title": title, "Date": date, "Author": author, "Image": image, "Content": content}
        bfDataFrame = bfDataFrame._append(dict1, ignore_index=True)

    next_page = mainbs4Object.select_one('a.wp-block-query-pagination-next')
    if next_page:
        url = next_page['href']
    else:
        break  # Stop if there's no next page
```

## Saving the Data

After the scraping process is complete, the script saves the Pandas DataFrame to an Excel file named `techcrunch_ai_articles.xlsx`.

```
bfDataFrame.to_excel("techcrunch_ai_articles.xlsx", index=False)
```