from datetime import date      #built in module

def add_entry():
    today = str(date.today())       #same data type
    thoughts = input("How was your day? ")

    file = open("diary.txt", "a")    #opening dairy for append/add
    file.write(f"{today}: {thoughts}/n")       
    file.close()

    print("Entry saved successfully")

def view_entries():
    setup_file = open("diary.txt", "a")
    setup_file.close()

    file = open("diary.txt", "r")
    contents = file.read()
    file.close()

    print("Your Diary Entries")
    if contents == "":
        print("No diary entries found yet.")
    else:
        print(contents)

def main():
    print("1. Add a new entry")
    print("2. View all entries")

    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        add_entry()
    elif choice == "2":
        view_entries()
    else:
        print("Invalid choice!")

main()