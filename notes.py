# built out menu
# view_notes() works
# adding a check path to notes directory to be reusable


import os

def check_path():
    notes_path = os.path.join(os.getcwd(), "notes")  # relative path
    if not os.path.exists(notes_path):
        os.makedirs(notes_path)
        print(f"Created 'notes' folder at: {notes_path}")
    return notes_path


notes_path = check_path()


def view_notes():
    if not os.listdir(notes_path):
        print("No notes found.")
        return
    
    for filename in sorted(os.listdir(notes_path)):
        file_path = os.path.join(notes_path, filename)
        with open(file_path, "r") as file:
            content = file.read().strip()
            print(f"{filename[:-4]}: {content}")

def main():
    username = "user1"
    
    while True:
        print(f"\n. KeepNotes Menu — Welcome, {username}")
        print("1. View Notes")
        print("2. Add a New Note")
        print("3. Edit a Note")
        print("4. Delete a Note")
        print("5. Exit")

        choice = input("Select a numbered option: ")

        if choice == "1":
            print("\n" + "=" * 30)
            print("       VIEWING NOTES")
            print("=" * 30 + "\n")
            view_notes()

        elif choice == "2":
            print("\n" + "=" * 30)
            print("       ADDING NOTE")
            print("=" * 30 + "\n")
            print("Adding a note... (not yet implemented)")

        elif choice == "3":
            print("\n" + "=" * 30)
            print("       EDITING NOTE")
            print("=" * 30 + "\n")
            print("Editing a note... (not yet implemented)")

        elif choice == "4":
            print("\n" + "=" * 30)
            print("       DELETING NOTE")
            print("=" * 30 + "\n")
            print("Deleting a note... (not yet implemented)")

        elif choice == "5":
            print("\nThanks for using KeepNotes. Goodbye!\n")
            break

        else:
            print("\nInvalid option. Please choose 1 through 5.\n")




    # Add()


    # Edit()


    # Delete()


if __name__ == "__main__":
    main()
