from dotenv import load_dotenv
import os
import psycopg2
from rich.console import Console
from rich.table import Table

load_dotenv()

#create a connection to the database.
con = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
)


#Creates the tables if they don't exist
def create_table():
    #creates a cursor in order to make queries to the database
    cursor = con.cursor()

    #Creates the games table
    cursor.execute(
    """CREATE TABLE IF NOT EXISTS games(
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        release_year INTEGER
        )
    """)

    #Creates the users table 
    cursor.execute(
    """CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        name TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
        )
    """)

    #Creates the USER - GAMES relation table
    cursor.execute(
    """CREATE TABLE IF NOT EXISTS user_games(
       id SERIAL PRIMARY KEY,
       user_id INTEGER NOT NULL,
       game_id INTEGER NOT NULL,
       rating REAL,
       time INTEGER,
       review TEXT,
       FOREIGN KEY(user_id) REFERENCES users(id),
       FOREIGN KEY(game_id) REFERENCES games(id),
       UNIQUE(user_id, game_id)
        )
    """)

    con.commit()


def add_game_to_user(user_id, game_name, rating, time, review, release_year):
    #creates a cursor in order to make queries to the database
    cursor = con.cursor()
    
    #Grants that the game exists
    cursor.execute("INSERT INTO games (name, release_year) VALUES (%s, %s)", (game_name, release_year))
    cursor.execute("SELECT id FROM games WHERE name = (%s)", (game_name,))
    game_id = cursor.fetchone()[0]

    #Creates the relation on the user_games table
    cursor.execute("INSERT INTO user_games (user_id, game_id, rating, time, review) VALUES (%s, %s, %s, %s, %s)",
                   (user_id, game_id, rating, time, review))
    
    con.commit()
    print("Game added")

def show_all_games_from_user(request_id):
    cursor = con.cursor()

    cursor.execute("SELECT games.name, rating FROM games JOIN (SELECT * FROM user_games WHERE user_id = %s) ON games.id = game_id",
                   (request_id,))

    rows = cursor.fetchall()
    columns = ["Title", "Rating"]

    table = Table(title= "Your games")

    for column in columns:
        table.add_column(column)

    for row in rows:
        table.add_row(row[0], str(row[1]))

    console = Console()
    console.print(table)