import database

def show_menu(login_id):
    while(True):
        print(f"===== Main Menu =====")
        print("1- Insert new game")
        print("2- Show all games")
        print("0- Log out")

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