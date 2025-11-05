from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

#create a connection to the database.
con = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)

#create a cursor in order to make queries to the database
cursor = con.cursor()

#Creates the table if it doesn't exist
def create_table():
    cursor.execute(
    """CREATE TABLE IF NOT EXISTS games(
        id SERIAL PRIMARY KEY,
        title TEXT NOT NULL,
        release_year INTEGER,
        time_played INTEGER,
        rating FLOAT
        )"""
    )
    con.commit()

#Inserts a game into the table
def insert_game(title, year, time, rating):
    values = (title, year, time, rating)
    cursor.execute("INSERT INTO games (title, release_year, time_played, rating) VALUES(%s, %s,%s, %s)", values)
    con.commit()

