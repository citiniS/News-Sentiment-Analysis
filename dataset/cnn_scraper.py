"""The following file is used for scraping article titles from text.npr.org

This file was created by Kim Benson, 2025"""


# imports
import csv
from bs4 import BeautifulSoup
import requests

# declare variables
URL = "https://lite.cnn.com/"
CSV_FILENAME = "dataset/cnnarticles.csv"

# setup for web scraping
response = requests.get(URL)
CNN_raw_html = response.text

soup = BeautifulSoup(CNN_raw_html, 'html.parser')

# get news titles
if response.status_code == 200:
    CNN_news_titles = soup.find("ul").find_all('li')

    # clean titles and remvoe tags so that it is just the text
    cleaned_CNN_titles = []

    for item in CNN_news_titles:
        a_element = item.find('a')

        if a_element:
            cleaned_title = a_element.get_text(strip=True)
            cleaned_title.strip().replace('"', '')
            cleaned_CNN_titles.append(cleaned_title)

    # export titles to csv
    with open(CSV_FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)

        for title in cleaned_CNN_titles:
            writer.writerow([title])