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
                    print("The game doesn't existe")
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


def show_menu_admin(login_id):

    while(True):

        main_menu_admin()

        option = input("Choose an option: ")

        match option:
            #Exit
            case "0":
                print("Going back to menu...")
                return
            #Insert
            case "1":
                type = "insert"
                show_insert_and_remove_menu(type)
            #Remove
            case "2":
                type = "remove"
                show_insert_and_remove_menu(type)
            #Show
            case "3":
                show_all_menu()

            case _:
                print("Invalid option.")


def main_menu_table():
    table = Table()
    rows = [
        ["1- Insert new game in my list"],
        ["2- Show all games from my list"],
        ["3- Remove game from own list"],
        ["0- Log out"]
    ]
        
    table.add_column("==== Main Menu ====")

    for row in rows:
        table.add_row(*row)

    console = Console()
    console.print(table)



def show_insert_and_remove_menu(type):

    while(True):

        if type == "insert":

            insert_and_remove_menu()

            option = input("Choose an option: ")

            match option:
                #Exit
                case "0":
                    print("Going back to admin menu...")
                    return
                #Game
                case "1":
                    title = input("Game title: ")
                    year = input("Release year: ")
                    genres_raw = input("Genres (separate by comma): ")
                    genres = [g.strip() for g in genres_raw.split(",")]

                    add = True
                    for g in genres:
                        if not database.search_genre(g):
                            print(f"Invalid genre: {g}")
                            add = False
                            break

                    if not add:
                        continue
                        
                    dev = input("Developer: ")
                    if not database.search_dev(dev):
                        print("Invalid developer")
                        continue

                    database.add_game_adm(title, year, genres, dev)
                    print(f"{title} was added")
                    
                #Gender
                case "2":
                    name = input("What genre: ")
                    database.add_genre(name)
                    print(f"{name} was added.")
                    
                #Developer
                case "3":
                    dev = input("Developers name: ")
                    database.add_developer(dev)
                    print(f"{dev} was added")

                #User
                case "4":    
                    usr = input("User name: ")
                    database.add_user(usr)
                    print(f"New user ({usr}) was registered")

                case _:
                    print("Invalid option.")

        elif type == "remove":

            insert_and_remove_menu()

            option = input("Choose an option: ")

            match option:
                #Exit
                case "0":
                    print("Going back to admin menu...")
                    return
                #Game
                case "1":
                    title = input("Game title: ")

                #Gender
                case "2":
                    type = input("What genre: ")
                    
                #Developer
                case "3":
                    dev = input("Developers name")
                    
                #User
                case "4":    
                    usr = input("User name")

                case _:
                    print("Invalid option.")

def show_all_menu():

    while(True):
        
        all_menu()

        option = input("Choose an option: ")

        match option:
            #Exit
            case "0":
                print("Going back to admin menu...")
                return
            #Game
            case "1":
                
                database.show_all_games()

            #Games with Genre
            case "2":
                type = input("What genre: ")
                
            #Genre
            case "3":
                database.show_all_genres()
               
            #Developers
            case "4":
                database.show_all_dev()

            #User
            case "5":
                database.show_all_usr()

            case _:
                print("Invalid option.")

def main_menu_admin():

    table = Table()
    rows = [
        ["1- Insert"],
        ["2- Remove"],
        ["3- Show"],
        ["0- Log out"]
    ]

    table.add_column("==== Admin Main Menu ====")

    for row in rows:
        table.add_row(*row)

    console = Console()
    console.print(table)

def insert_and_remove_menu():

    table = Table()
    rows = [
        ["1- Game"],
        ["2- Genre"],
        ["3- Developer"],
        ["4- User"],
        ["0- Back"]
    ]

    table.add_column("==== Admin ====")

    for row in rows:
        table.add_row(*row)

    console = Console()
    console.print(table)

def all_menu():

    table = Table()
    rows = [
        ["1- All Games"],
        ["2- All Games from of a specific genre"],
        ["3- All Genres"],
        ["4- All Developers"],
        ["5- All Users"],
        ["0- Back"]
    ]

    table.add_column("==== Show ====")

    for row in rows:
        table.add_row(*row)

    console = Console()
    console.print(table)