import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://techcrunch.com/category/artificial-intelligence/"

bfDataFrame = pd.DataFrame()

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
        content_element = bs4Object.select_one('.entry-content p')
        content = " ".join([p.text.strip() for p in bs4Object.select('.entry-content p')]) if content_element else "N/A"

        
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

bfDataFrame.to_excel("techcrunch_ai_articles.xlsx", index=False)
