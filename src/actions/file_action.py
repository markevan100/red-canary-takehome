def handle_file_action():
    while True:
        action = input("Would you like to create (c), modify (m), or delete (d) a file? ").strip().lower()

        if action in ["create", "c"]:
            print("File create action selected.")

        elif action in ["modify", "m"]:
            print("File modify action selected.")

        elif action in ["delete", "d"]:
            print("File delete action selected.")

        else:
            print("Invalid file action selected. Please choose create (c), modify (m), or delete (d).")
            continue
        break
