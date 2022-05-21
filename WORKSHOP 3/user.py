def login(database={}, username="", password=""):
    for key in database:
        if(key == username and database[key] == password):
            print("Welcome to the dark side", username, "\n")
            return username
        else:
            print("No match for that Username and Password. \n")
            return ""


def register(database, username):
    for key in database:
        if (key == username):
            print("Username already registered \n")
            return ""
        else:
            print(username, "has been registered \n")
            return username
