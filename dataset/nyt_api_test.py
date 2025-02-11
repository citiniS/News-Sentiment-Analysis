"""The following file is used for scraping article titles from The New York Times
using the official New York Times API.

*** Important Information About File Usage ***

    -- Article Count --
    KEYWORDS and PAGES_NEEDED have a direct relationship.
    The longer kEYWORDS is, the smaller PAGES_NEEDED
    should be. Each page is 10 articles. So, for example
    two keywords and 2 pages would give you 40 titles.
    The NYT API limits the amount of articles you can
    get per call and minute, so, keep calls short
    and if needed ,spread them across multiple
    runs of this file.

This file was created by Kim Benson, 2025"""

# import
import requests
import csv


# variables
API_KEY = 'yuYr5EzTg0M9KB7TJ2g6xqUqyKizH80G' # api key
KEYWORDS = ['transgender', 'electon'] # keywords to get articles for
CSV_FILENAME = 'nytarticles.csv' # file data is exported to
PAGES_NEEDED = 2 # pages to scrape through. 1 page = 10 articles
URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

# open a csv to export the data
with open(CSV_FILENAME, 'a', newline='') as file:
    writer = csv.writer(file)

    # loops through for specified page count
    for keyword in KEYWORDS:
        for page in range(PAGES_NEEDED):
            params = {
                'q': keyword,
                'api-key': API_KEY,
                'page': page,
            }

            # get articles from server
            response = requests.get(URL, params=params)

            # if api call works, export to csv
            # otherwise, print status code
            if response.status_code == 200:
                data = response.json()

                for article in data['response']['docs']:
                    headline = article['headline']['main']
                    writer.writerow([headline])

            else:
                print(f"Status code: {response.status_code}")