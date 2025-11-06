import database

def show_menu():
    while(True):
        print("===== Main Menu =====")
        print("1- Insert new game")
        print("2- Show all games")
        print("0- Exit")

        option = input("Choose an option: ")

        match option:
            #Exit program
            case "0":
                print("Exiting program... ")
                return
            #Insert a game
            case "1":
                title = input("Game title: ")
                year = int(input("Release year: "))
                time = int(input("Time played: "))
                rating = float(input("Rating: "))
                database.insert_game(title, year, time, rating)
                print("Game added succesfully")
            #Show all games
            case "2":
                database.show_all_games()
            case _:
                print("Invalid option.")