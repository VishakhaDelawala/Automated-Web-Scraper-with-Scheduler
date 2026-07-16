import schedule
import time

from scraper import scrape_books
from export import export_to_csv


def run_scheduler():

    schedule.every(1).minutes.do(
        scrape_books
    )

    schedule.every(5).minutes.do(
        export_to_csv
    )

    while True:

        schedule.run_pending()

        time.sleep(1)