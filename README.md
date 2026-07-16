# 🤖 Automated Web Scraper with Scheduler

An automated web scraping tool that extracts data from dynamic websites, stores the collected information in a database, and runs scraping jobs on a scheduled basis. The project uses Selenium for handling JavaScript-rendered pages, BeautifulSoup for HTML parsing, Celery for task scheduling, and SQLite for data storage.

## 📌 Project Overview

This application automates the process of collecting data from websites without manual intervention. It can scrape dynamic web pages, save the extracted information to a database, and export data to CSV files for further analysis.

## 🚀 Features

* 🌐 Scrape static and dynamic websites
* 🤖 Browser automation using Selenium
* 🔍 HTML parsing with BeautifulSoup
* ⏰ Scheduled scraping tasks with Celery
* 💾 Store scraped data in SQLite database
* 📊 Export collected data to CSV files
* 📝 Logging and error handling
* 🔄 Automatic retry for failed scraping jobs
* ⚙️ Configurable scraping intervals
* 📈 Easy data management and retrieval

## 🛠️ Technologies Used

* Python 3.x
* Selenium
* BeautifulSoup4
* Celery
* SQLite
* Pandas
* Requests
* ChromeDriver / WebDriver Manager

## 📂 Project Structure

```text
automated-web-scraper/
│
├── app.py
├── scraper.py
├── scheduler.py
├── database.py
├── exporter.py
├── config.py
├── requirements.txt
├── celery_worker.py
├── logs/
│   └── scraper.log
├── data/
│   ├── scraper.db
│   └── exports/
│       └── scraped_data.csv
├── templates/
│   └── sample_config.json
└── README.md
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/automated-web-scraper.git
cd automated-web-scraper
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔧 Configuration

Edit the `config.py` file to configure:

```python
TARGET_URL = "https://example.com"
SCRAPE_INTERVAL = 60
DATABASE_NAME = "scraper.db"
EXPORT_PATH = "data/exports/"
```

### Sample Configuration

```python
SCRAPER_CONFIG = {
    "url": "https://example.com",
    "interval_minutes": 30,
    "export_csv": True,
    "headless_browser": True
}
```

## ▶️ Running the Application

### Start the Main Application

```bash
python app.py
```

### Start Celery Worker

```bash
celery -A celery_worker worker --loglevel=info
```

### Start Celery Beat Scheduler

```bash
celery -A celery_worker beat --loglevel=info
```

## 📊 Workflow

1. Scheduler triggers scraping task.
2. Selenium loads the target webpage.
3. BeautifulSoup extracts required data.
4. Data is validated and cleaned.
5. Records are stored in SQLite database.
6. Data can be exported to CSV.
7. Logs are generated for monitoring.

## 💾 Database Schema

### Scraped Data Table

| Column     | Type     | Description     |
| ---------- | -------- | --------------- |
| id         | INTEGER  | Primary Key     |
| title      | TEXT     | Extracted Title |
| content    | TEXT     | Scraped Content |
| url        | TEXT     | Source URL      |
| scraped_at | DATETIME | Timestamp       |

## 📤 Exporting Data

Export data to CSV:

```bash
python exporter.py
```

Generated file:

```text
data/exports/scraped_data.csv
```

## 📝 Logging

Logs are stored in:

```text
logs/scraper.log
```

Example log entry:

```text
2026-07-16 10:00:01 - INFO - Scraping task started
2026-07-16 10:00:15 - INFO - 150 records collected
2026-07-16 10:00:16 - INFO - Data stored successfully
```

## 🔄 Scheduling Example

Run scraper every 30 minutes:

```python
from celery.schedules import crontab

beat_schedule = {
    'scrape-every-30-minutes': {
        'task': 'scheduler.run_scraper',
        'schedule': crontab(minute='*/30'),
    },
}
```

## 📈 Future Enhancements

* Proxy rotation support
* CAPTCHA handling
* Email notifications
* Multi-site scraping support
* REST API integration
* Cloud database support
* Dashboard for monitoring jobs
* Docker deployment

## 🧪 Example Use Cases

* Product price monitoring
* News aggregation
* Job listing collection
* Real estate tracking
* Competitor analysis
* Market research
* Data collection for analytics

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Submit a Pull Request

## 📄 License

This project is licensed under the MIT License.

## ⚠️ Disclaimer

Ensure that you comply with the target website's Terms of Service and robots.txt policies before scraping any website. Use this project responsibly and ethically.

## 👨‍💻 Author

**Your Name**

GitHub: https://github.com/yourusername

Email: [your.email@example.com](mailto:your.email@example.com)

---

⭐ If you find this project useful, consider starring the repository on GitHub.
