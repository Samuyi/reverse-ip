import sqlite3
import datetime
from contextlib import closing

def create_table():
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS ip_conn (ip TEXT, date TEXT)")


def insert_ip_addr(ip):
    with sqlite3.connect("ip.db", check_same_thread=False) as conn:
        cursor = conn.cursor()
        now = datetime.datetime.now().strftime('%A, %d. %B %Y %I:%M%p')
        statement= "INSERT INTO ip_conn VALUES (?, ?)"
        cursor.execute(statement, (ip, now))
        conn.commit()

def get_ip_addr():
    with sqlite3.connect("ip.db", check_same_thread=False) as conn:
        cursor = conn.cursor()
        rows = cursor.execute("SELECT * from ip_conn").fetchall()
        return rows


db_file_name = 'ip.db'
conn = sqlite3.connect(db_file_name, check_same_thread=False)
create_table()
