from dotenv import load_dotenv
from menu import show_menu
import os
import psycopg2
from time import sleep

load_dotenv()

def user_login():
    con = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    cursor = con.cursor()

    while(True):
        print("1- Login")
        print("2- Register")
        print("0- Exit program")
        option = input("")

        match option:
            case "1":
                username = input("Username: ")
                password = input("Password: ")

                cursor.execute("SELECT id FROM users WHERE name = %s AND password = %s", (username, password))
                validation_id = cursor.fetchone()

                if validation_id:
                    print(f"Welcome, {username}!")
                    sleep(0.5)
                    show_menu(validation_id)
                else:
                    print("Invalid username or wrong password.")
            case "2":
                username = input("Username: ")
                cursor.execute("SELECT name FROM users WHERE name = %s", (username,))
                name_validation = cursor.fetchone()
                
                if name_validation:
                    print("Username already exists")
                else:
                    password = input("Password: ")
                    cursor.execute("INSERT INTO users (name, password) VALUES (%s, %s)", (username, password))
                    con.commit()
                    print("Registration complete.")
            case "0":
                print("Finishing program...")
                cursor.close()
                con.close()
                sleep(0.5)
                return
            case _:
                print("Invalid option.")
        

