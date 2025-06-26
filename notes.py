# built out menu
# view_notes() works
# adding a check path to notes directory to be reusable (review logic)
# set up add_note()
# setup overwrite protection( check for existing filename)


import os


def check_path():
    notes_path = os.path.join(os.getcwd(), "notes")  # relative path
    if not os.path.exists(notes_path):
        os.makedirs(notes_path)
        print(f"Created 'notes' folder at: {notes_path}")
    return notes_path


notes_path = check_path()


def list_note_titles():
    titles = sorted(os.listdir(notes_path))
    for index, file in enumerate(titles, start=1):
        print(f"{index}. {file[:-4]}")  # removes ".txt"
    return titles


def select_note(titles):
    while True:
        choice = input("Enter the number of the note to view (or press Enter to cancel): ").strip()
        if choice == "":
            print("Cancelled.")
            return None

        if choice.isdigit():
            index = int(choice)
            if 1 <= index <= len(titles):
                return titles[index - 1]
            else:
                print("Invalid number. Try again.")
        else:
            print("Please enter a number.")


def view_notes():
    if not os.listdir(notes_path):
        print("No notes found.")
        return

    print("Saved Notes:")
    titles = list_note_titles()
    selected_file = select_note(titles)

    if selected_file:
        full_path = os.path.join(notes_path, selected_file)
        with open(full_path, "r") as file:
            print("\n" + "=" * 30)
            print(f"--- {selected_file[:-4]} ---")
            print(file.read())
            print("=" * 30)


def add_note():
    while True:
        title = input("Enter a title (or type 'return' to cancel): ").strip()
        if title.lower() == "return":
            print("Returning to main menu...")
            return

        file_name = title.replace(" ", "_").lower() + ".txt"
        full_path = os.path.join(notes_path, file_name)

        if os.path.exists(full_path):
            print(f"A note titled '{title}' already exists.")
            print("Please enter another title.")
        else:
            break  # title is unique, proceed to content

    print("Enter your content. Type 'DONE' on a new line to finish.")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "DONE":
            break
        lines.append(line)

    content = "\n".join(lines)
    with open(full_path, "w") as file:
        file.write(content)

    print(f"Note '{title}' saved successfully!")


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
            add_note()

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
