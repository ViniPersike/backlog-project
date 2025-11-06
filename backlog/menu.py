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
                year = int(input("Release year: "))
                time = int(input("Time played: "))
                rating = float(input("Rating: "))
                review = input("Write a short review: ")
                database.add_game_to_user(login_id, title, rating, time, review, year)
                print("Game added succesfully")
            #Show all games
            case "2":
                database.show_all_games_from_user(login_id)
            case _:
                print("Invalid option.")

def main_menu_table():
    table = Table()
    rows = [
        ["1- Insert new game"],
        ["2- Show all games"],
        ["0- Log out"]
    ]
        
    table.add_column("==== Main Menu ====")

    for row in rows:
        table.add_row(*row)

    console = Console()
    console.print(table)