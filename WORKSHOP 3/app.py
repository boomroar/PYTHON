from Donations_pkg.homepage import show_homepage, donate, show_donations
from Donations_pkg.user import login, register

database = {"admin": "password123"}
donations = []
authorized_user = ""

appOpen = True
while (appOpen):
    show_homepage()
    if (authorized_user == ""):
        print("You must be logged in to donate")
    else:
        print("Logged in as: ", authorized_user)

    menu_choice = input("Choose an option: ")

    if menu_choice == "1":
        username = input("Enter username: ")
        password = input("Enter Password: ")
        authorized_user = login(database, username, password)

    elif menu_choice == "2":
        username = input("Enter the username you would like to register: ")
        password = input(
            "Enter the new password associated with that username: ")
        authorized_user = register(database, username)
        if (authorized_user != ""):
            database[username] = password
            #dict1 = {username: password}
            #database.update({username: password})

    elif menu_choice == "3":
        if authorized_user == "":
            print("You are not logged in")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)

    elif menu_choice == "4":
        show_donations(donations)

    elif menu_choice == "5":
        print("Leaving DonateMe...")
        appOpen = False
    else:
        print("Invalid Option")
