import database
from rich.console import Console
from rich.table import Table

def show_menu(login_id):
    while(True):
        main_menu_table()

        option = input("Choose an option: ")

        match option:
            #Exit program
            case "0":
                print("Going back to menu...")
                return
            #Insert a game
            case "1":
                title = input("Game title: ")

                validation_title = database.search_game(title)

                validation_game_user = database.search_game_user(title, login_id)

                if not validation_title:
                    print("The game not exists")
                    continue
                elif validation_game_user:
                    print("The game already is in your list")
                    continue

                # year = int(input("Release year: "))
                time = int(input("Time played: "))
                rating = float(input("Rating: "))
                review = input("Write a short review: ")
                database.add_game_to_user(login_id, title, rating, time, review)
                print("Game added succesfully to your list")
            #Show all games
            case "2":
                database.show_all_games_from_user(login_id)
            case "3":
                title = input("Title: ")
                database.remover_jogo(title, login_id)
            case _:
                print("Invalid option.")

def main_menu_table():
    table = Table()
    rows = [
        ["1- Insert new game"],
        ["2- Show all games"],
        ["3- Remove game from own list"],
        ["0- Log out"]
    ]
        
    table.add_column("==== Main Menu ====")

    for row in rows:
        table.add_row(*row)

    console = Console()
    console.print(table)
