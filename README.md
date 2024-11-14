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