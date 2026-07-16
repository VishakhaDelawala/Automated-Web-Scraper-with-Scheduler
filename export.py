import os
import sqlite3
import pandas as pd

from config import DATABASE
from config import CSV_FILE


def export_to_csv():

    os.makedirs("exports", exist_ok=True)

    conn = sqlite3.connect(DATABASE)

    df = pd.read_sql_query(
        "SELECT * FROM books",
        conn
    )

    df.to_csv(
        CSV_FILE,
        index=False
    )

    conn.close()

    print("CSV Exported Successfully")