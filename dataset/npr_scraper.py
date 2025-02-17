"""The following file is used for scraping article titles from text.npr.org

This file was created by Kim Benson, 2025"""


# imports
import csv
from bs4 import BeautifulSoup
import requests

# declare variables
URL = "https://text.npr.org/1001"
CSV_FILENAME = "dataset/nprarticles.csv"

# setup for web scraping
response = requests.get(URL)
NPR_raw_html = response.text

soup = BeautifulSoup(NPR_raw_html, 'html.parser')

# get news titles
if response.status_code == 200:
    NPR_news_titles = soup.find("ul").find_all('li')

    # clean titles and remvoe tags so that it is just the text
    cleaned_NPR_titles = []

    for item in NPR_news_titles:
        a_element = item.find('a')
        cleaned_NPR_titles.append(a_element.text)

    # export titles to csv
    with open(CSV_FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)

        for title in cleaned_NPR_titles:
            writer.writerow([title])