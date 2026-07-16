from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup

from database import insert_book

from config import URL

import time


def scrape_books():

    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        )
    )

    driver.get(URL)

    time.sleep(3)

    html = driver.page_source

    driver.quit()

    soup = BeautifulSoup(html, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        title = book.h3.a["title"]

        price = book.find(
            "p",
            class_="price_color"
        ).text

        availability = book.find(
            "p",
            class_="instock availability"
        ).text.strip()

        insert_book(
            title,
            price,
            availability
        )

    print("Data Scraped Successfully")