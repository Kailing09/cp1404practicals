name = input("Enter name: ")
MENU_OPTIONS = "(H)ello\n(G)oodbye\n(Q)uit\n"

print(MENU_OPTIONS)

choice = input(">>> ").upper()

while choice != 'Q':
    if choice == 'H':
        print(f"Hello {name}")
    elif choice == 'G':
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    print(MENU_OPTIONS)
    choice = input(">>> ").upper()

print("Finished.")
