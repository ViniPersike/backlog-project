import database

def show_menu():
    while(True):
        print("===== Main Menu =====")
        print("1- Insert new game")
        print("2- Show all games")
        print("0- Exit")

        option = int(input("Choose an option: "))

        match option:
            case 0:
                print("Exiting program... ")
                return
            case 1:
                title = input("Game title: ")
                year = int(input("Release year: "))
                time = int(input("Time played: "))
                rating = float(input("Rating: "))
                database.insert_game(title, year, time, rating)
                return
            case _:
                return "Invalid option"
                
