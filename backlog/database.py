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

    #Creates the GENRE table
    cursor.execute(
    """CREATE TABLE IF NOT EXISTS genre(
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL
        )
    """)

    #Creates the DEVELOPERS table
    cursor.execute(
    """CREATE TABLE IF NOT EXISTS developers(
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL
        )
    """)

    #Creates the games table
    cursor.execute(
    """CREATE TABLE IF NOT EXISTS games(
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        release_year INTEGER,
        developer_id INTEGER NOT NULL,
        FOREIGN KEY (developer_id) REFERENCES developers(id) ON DELETE CASCADE
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

    #Creates the games-genre relation table
    cursor.execute(
    """CREATE TABLE IF NOT EXISTS game_genres(
        game_id INTEGER NOT NULL,
        genre_id INTEGER NOT NULL,
        PRIMARY KEY (game_id, genre_id),
        FOREIGN KEY (game_id) REFERENCES games(id) ON DELETE CASCADE,
        FOREIGN KEY (genre_id) REFERENCES genre(id) ON DELETE CASCADE
        )
    """)

    #Creates the USER - GAMES relation table
    cursor.execute(
    """CREATE TABLE IF NOT EXISTS user_games(
       user_id INTEGER NOT NULL,
       game_id INTEGER NOT NULL,
       rating REAL,
       time INTEGER,
       status TEXT,
       review TEXT,
       PRIMARY KEY(user_id, game_id),
       FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE,
       FOREIGN KEY(game_id) REFERENCES games(id) ON DELETE CASCADE,
       UNIQUE(user_id, game_id)
        )
    """)
    
    con.commit()


def add_game_to_user(user_id, game_name, rating, time, review, status):
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
    cursor.execute("INSERT INTO user_games (user_id, game_id, rating, time, review, status) VALUES (%s, %s, %s, %s, %s, %s)",
                   (user_id, game_id, rating, time, review, status))
    
    con.commit()


def show_all(type):

    cursor = con.cursor()

    query = f"SELECT name FROM {type}"

    cursor.execute(query)

    rows = cursor.fetchall()

    if not rows:
        print("Don't have any {type} yet.")
    else:
        columns = ["Name"]

        table = Table(title= type.capitalize())

        for column in columns:
            table.add_column(column)

        for row in rows:
            table.add_row(row[0])

        console = Console()
        console.print(table)


def show_all_games():

    cursor = con.cursor()

    cursor.execute("""SELECT games.name, AVG(rating), genre.name, developers.name, games.release_year 
                        FROM games LEFT JOIN game_genres ON games.id = game_genres.game_id
                            LEFT JOIN genre ON game_genres.genre_id = genre.id
                            LEFT JOIN developers ON developers.id = games.developer_id
                            LEFT JOIN user_games ON user_games.game_id = games.id
                            
                            GROUP BY games.name, genre.name, developers.name, games.release_year
                            ORDER BY games.name """)

    rows = cursor.fetchall()

    if not rows:
        print("Don't have any games yet.")
    else:
        columns = ["Title", "Average Rating", "Genre", "Developer", "Release Date"]

        table = Table(title= "Games")

        for column in columns:
            table.add_column(column)

        for row in rows:
            table.add_row(row[0], str(row[1]), str(row[2]), str(row[3]), str(row[4]))

        console = Console()
        console.print(table)


def show_all_games_from_genre(request_genre):

    cursor = con.cursor()

    cursor.execute("""SELECT games.name, AVG(rating), genre.name, developers.name, games.release_year
                        FROM games LEFT JOIN game_genres ON games.id = game_genres.game_id
                            LEFT JOIN genre ON game_genres.genre_id = genre.id
                            LEFT JOIN developers ON developers.id = games.developer_id
                            LEFT JOIN user_games ON user_games.game_id = games.id
                   
                            WHERE genre.name = (%s)
                            
                            GROUP BY games.name, genre.name, developers.name, games.release_year 
                            ORDER BY games.name """, (request_genre,))

    rows = cursor.fetchall()

    if not rows:
        print("Don't have any games yet.")
    else:
        columns = ["Title", "Average Rating", "Genre", "Developer", "Release Date"]

        table = Table(title= "Games")

        for column in columns:
            table.add_column(column)

        for row in rows:
            table.add_row(row[0], str(row[1]), str(row[2]), str(row[3]), str(row[4]))

        console = Console()
        console.print(table)


def show_all_games_from_user(request_user_id):
    cursor = con.cursor()

    cursor.execute("SELECT games.name, rating, time, review, status FROM games JOIN (SELECT * FROM user_games WHERE user_id = %s) ON games.id = game_id",
                   (request_user_id,))

    rows = cursor.fetchall()

    if not rows:
        print("You don't have any games yet.")
    else:
        columns = ["Title", "Rating", "Time played", "Review", "Status"]

        table = Table(title= "Your games")

        for column in columns:
            table.add_column(column)

        for row in rows:
            table.add_row(row[0], str(row[1]), str(row[2]), str(row[3]), str(row[4]))

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
        print("The game doesn't exist for this user") 


def add_genre(name):
    cursor = con.cursor()

    cursor.execute("SELECT id FROM genre WHERE name = (%s)", (name,))
    name_validation = cursor.fetchone()

    if name_validation:
        print("Genre already exists.")
    else:
        cursor.execute("INSERT INTO genre (name) VALUES (%s)", (name,))
        con.commit()
        print(f"{name} was added.")


def add_developer(name):
    cursor = con.cursor()

    cursor.execute("SELECT id FROM developers WHERE name = (%s)", (name,))
    name_validation = cursor.fetchone()

    if name_validation:
        print("Developer already exists.")
    else:
        cursor.execute("INSERT INTO developers (name) VALUES (%s)", (name,))
        con.commit()
        print(f"{name} was added")


def add_user(name):
    cursor = con.cursor()

    cursor.execute("SELECT name FROM users WHERE name = %s", (name,))
    name_validation = cursor.fetchone()
    
    if name_validation:
        print("Username already exists")
    else:
        default_password = 123
        cursor.execute("INSERT INTO users (name, password) VALUES (%s, %s)", (name, default_password))
        con.commit()
        print(f"New user ({name}) was registered")


def add_game_adm(name, year, genres, developer):
    cursor = con.cursor()

    # Obter o ID do developer
    cursor.execute("SELECT id FROM developers WHERE name = %s", (developer,))
    developer_id = cursor.fetchone()

    if not developer_id:
        print("Developer not found.")
        return

    developer_id = developer_id[0]

    # Criar o jogo (SEM genre)
    cursor.execute(
        "INSERT INTO games (name, release_year, developer_id) VALUES (%s, %s, %s) RETURNING id",
        (name, year, developer_id)
    )
    game_id = cursor.fetchone()[0]

    # Associar múltiplos gêneros
    for genre in genres:
        cursor.execute("SELECT id FROM genre WHERE name = %s", (genre,))
        genre_id = cursor.fetchone()

        if not genre_id:
            print(f"Genre '{genre}' not found. Skipping.")
            continue

        genre_id = genre_id[0]

        cursor.execute(
            "INSERT INTO game_genres (game_id, genre_id) VALUES (%s, %s) ON CONFLICT DO NOTHING",
            (game_id, genre_id)
        )

    con.commit()


def search_genre(genre):
    cursor = con.cursor()

    cursor.execute("SELECT id FROM genre WHERE name = %s", (genre,))

    return cursor.fetchone()


def search_dev(dev):
    cursor = con.cursor()

    cursor.execute("SELECT id FROM developers WHERE name = %s", (dev,))

    return cursor.fetchone()


def remove_user(user):
    cursor = con.cursor()

    cursor.execute("SELECT id FROM users WHERE name = (%s)", (user,))
    validation_id = cursor.fetchone()

    if not validation_id:
        return False
    
    cursor.execute("DELETE FROM users WHERE name = (%s)", (user,))
    con.commit()
    return True


def remove_dev(dev):
    cursor = con.cursor()

    cursor.execute("SELECT id FROM developers WHERE name = (%s)", (dev,))
    validation_id = cursor.fetchone()

    if not validation_id:
        return False

    cursor.execute("DELETE FROM developers WHERE name = (%s)", (dev,))
    con.commit()
    return True


def remove_genre(genre):
    cursor = con.cursor()

    cursor.execute("SELECT id FROM genre WHERE name = (%s)", (genre,))
    validation_id = cursor.fetchone()

    if not validation_id:
        return False

    cursor.execute("DELETE FROM genre WHERE name = (%s)", (genre,))
    con.commit()
    return True


def remove_game(title):
    cursor = con.cursor()
    
    cursor.execute("SELECT id FROM games WHERE name = (%s)", (title,))
    validation_id = cursor.fetchone()

    if not validation_id:
        return False

    cursor.execute("DELETE FROM games WHERE name = (%s)", (title,))
    con.commit()
    return True