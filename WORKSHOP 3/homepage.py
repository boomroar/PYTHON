def show_homepage():
    print("     ===  DonateME Homepage  ===      ")
    print("--------------------------------------")
    print("| 1.  Login      | 2. Register       |")
    print("--------------------------------------")
    print("| 3.  Donate     | 4. Show Donations |")
    print("--------------------------------------")
    print("|                5. EXIT             |")
    print("--------------------------------------")


def donate(username):
    donation_amt = input("Enter amount to donate: ")
    donation_string = username + " donated $ " + donation_amt
    print("Thank you for your donation!\n")
    return donation_string


def show_donations(donations):
    print("\n ---ALL DONATIONS---")
    if (donations):
        for entry in donations:
            print(entry, "\n")
    else:
        print("Currently, there are no donations\n")
