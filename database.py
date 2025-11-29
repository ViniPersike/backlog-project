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
       user_id INTEGER NOT NULL,
       game_id INTEGER NOT NULL,
       rating REAL,
       time INTEGER,
       review TEXT,
       PRIMARY KEY(user_id, game_id),
       FOREIGN KEY(user_id) REFERENCES users(id),
       FOREIGN KEY(game_id) REFERENCES games(id),
       UNIQUE(user_id, game_id)
        )
    """)
    
    #Creates the DEVELOPERS table
    cursor.execute(
    """CREATE TABLE IF NOT EXISTS developers(
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL
        )
    """)

    #Creates the GAMES - DEVELOPERS relation table
    cursor.execute(
    """CREATE TABLE IF NOT EXISTS developed(
        developer_id INTEGER NOT NULL,
        game_id INTEGER NOT NULL,
        PRIMARY KEY(developer_id, game_id),
        FOREIGN KEY(developer_id) REFERENCES developers(id),
        FOREIGN KEY(game_id) REFERENCES games(id)
        )
    """)

    #Creates the GENRE table
    cursor.execute(
    """CREATE TABLE IF NOT EXISTS genre(
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL
        )
    """)

    con.commit()


def add_game_to_user(user_id, game_name, rating, time, review):
    #creates a cursor in order to make queries to the database
    cursor = con.cursor()
    
    #Checks if the game already exists
    cursor.execute("SELECT id FROM games WHERE name = (%s)", (game_name,))
    query = cursor.fetchone()
    
    #If the game already exists, gets it's id, if it doesn't, adds it to the database and gets the id
    if query:
        game_id = query[0]
    else:
        cursor.execute("INSERT INTO games (name) VALUES (%s)", (game_name,))
        cursor.execute("SELECT id FROM games WHERE name = (%s)", (game_name,))
        game_id = cursor.fetchone()[0]

    #Creates the relation on the user_games table
    cursor.execute("INSERT INTO user_games (user_id, game_id, rating, time, review) VALUES (%s, %s, %s, %s, %s)",
                   (user_id, game_id, rating, time, review))
    
    con.commit()

def show_all_games():

    cursor = con.cursor()

    cursor.execute("SELECT name FROM games")

    rows = cursor.fetchall()

    if not rows:
        print("Don't have any games yet.")
    else:
        columns = ["Title"]

        table = Table(title= "Games")

        for column in columns:
            table.add_column(column)

        for row in rows:
            table.add_row(row[0])

        console = Console()
        console.print(table)

def show_all_games_from_user(request_user_id):
    cursor = con.cursor()

    cursor.execute("SELECT games.name, rating FROM games JOIN (SELECT * FROM user_games WHERE user_id = %s) ON games.id = game_id",
                   (request_user_id,))

    rows = cursor.fetchall()

    if not rows:
        print("You don't have any games yet.")
    else:
        columns = ["Title", "Rating"]

        table = Table(title= "Your games")

        for column in columns:
            table.add_column(column)

        for row in rows:
            table.add_row(row[0], str(row[1]))

        console = Console()
        console.print(table)

def search_game(title):

    cursor = con.cursor()

    cursor.execute("SELECT name FROM games WHERE name = (%s)", (title,))

    return cursor.fetchone()

def search_game_user(title, login_id):

    cursor = con.cursor()

    cursor.execute("SELECT name FROM user_games JOIN games ON id = game_id WHERE user_id = (%s) AND name = (%s)", (login_id, title))

    return cursor.fetchone()

def remover_jogo(title, login_id):

    cursor = con.cursor()

    validation_game_user = search_game_user(title, login_id)

    if validation_game_user:
        cursor.execute("DELETE FROM user_games WHERE game_id = (SELECT id FROM games WHERE name = (%s) AND user_id = (%s))", (title, login_id))
        con.commit()
    else:
        print("The game not exists for this user") 
