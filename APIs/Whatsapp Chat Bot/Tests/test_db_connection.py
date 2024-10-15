import psycopg2
from decouple import config

DB_USER = "twiliotutorial"
DB_PASSWORD = "postgre1"
DB_NAME = "twilio_tutorial"

try:
    conn = psycopg2.connect(
        dbname=DB_USER,
        user=DB_NAME,
        password=DB_PASSWORD,
        host='localhost',
        port='5432'
    )
    print("Database connection successful")

except Exception as e:
    print(f"Failed to connect to database: {e}")

finally:

    if conn:
        conn.close()