from database import create_database
from scraper import scrape_books
from export import export_to_csv
from scheduler import run_scheduler


def main():

    create_database()

    print("1. Scrape Now")
    print("2. Export CSV")
    print("3. Start Scheduler")

    choice = input("Enter Choice: ")

    if choice == "1":

        scrape_books()

    elif choice == "2":

        export_to_csv()

    elif choice == "3":

        run_scheduler()

    else:

        print("Invalid Choice")


if __name__ == "__main__":
    main()