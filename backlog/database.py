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


#Creates the tables if they don't exist
def create_table():
    #creates a cursor in order to make queries to the database
    cursor = con.cursor()

    #Creates the games table
    cursor.execute(
    """CREATE TABLE IF NOT EXISTS games(
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL
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
       review TEXT,
       FOREIGN KEY(user_id) REFERENCES users(id),
       FOREIGN KEY(game_id) REFERENCES games(id),
       UNIQUE(user_id, game_id)
        )
    """)

    con.commit()

#Inserts a game into the table
def insert_game(title, year, time, rating):
    #creates a cursor in order to make queries to the database
    cursor = con.cursor()

    values = (title, year, time, rating)
    cursor.execute("INSERT INTO games (title, release_year, time_played, rating) VALUES(%s, %s,%s, %s)", values)
    con.commit()

def show_all_games():
    #creates a cursor in order to make queries to the database
    cursor = con.cursor()

    cursor.execute("SELECT * FROM games")
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)

def add_game_to_user(username, game_name, rating, review):
    #creates a cursor in order to make queries to the database
    cursor = con.cursor()
    
    #Grants that the user exists
    cursor.execute("INSERT OR IGNORE INTO users (username) VALUES (%s)", (username,))
    cursor.execute("SELECT id FROM users WHERE username=%s", (username,))
    user_id = cursor.fetchone()[0]

    #Grants that the game exists
    cursor.execute("INSERT OR IGNORE INTO games (name) VALUES (%s)", (game_name))
    cursor.execute("SELECT id FROM games WHERE name = (%s)", (game_name,))
    game_id = cursor.fetchone()[0]

    #Creates the relation on the user_games table
    cursor.execute("INSERT OR REPLACE INTO user_games (user_id, game_id, rating, review) VALUES (%s, %s, %s, %s)",
                   (user_id, game_id, rating, review))
    
    con.commit()
    con.close()

    print("Game added")