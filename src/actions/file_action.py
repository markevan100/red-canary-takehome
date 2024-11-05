import os
from logger import log_activity

USER_FILES_DIR = "user_created_files"

def ensure_user_files_dir():
    os.makedirs(USER_FILES_DIR, exist_ok=True)

def list_user_files():
    return [f for f in os.listdir(USER_FILES_DIR) if os.path.isfile(os.path.join(USER_FILES_DIR, f))]

def handle_file_action():
    print("Select an action: create_file (c), modify_file (m), delete_file (d)")
    action = input("Action: ").strip().lower()

    if action in ['c', 'create_file']:
        create_file()
    elif action in ['m', 'modify_file']:
        modify_file()
    elif action in ['d', 'delete_file']:
        delete_file()
    else:
        print("Invalid action. Please choose a valid option.")

def create_file():
    ensure_user_files_dir()
    filename = input("Enter the name of the file to create: ").strip()
    file_type = input("Enter the file type (e.g., .txt, .log): ").strip()
    if not file_type.startswith("."):
        file_type = "." + file_type
    full_filename = filename + file_type
    file_path = os.path.join(USER_FILES_DIR, full_filename)

    with open(file_path, 'w') as f:
        f.write("")

    log_activity("file_create", {"filepath": file_path, "file_type": file_type})
    print(f"File '{full_filename}' created successfully.")

def modify_file():
    ensure_user_files_dir()
    files = list_user_files()

    if not files:
        print("No files available to modify. Redirecting to file creation...")
        create_file()
        return

    print("Available files to modify:", files)
    filename = input("Enter the name of the file to modify: ").strip()
    if filename not in files:
        print("Invalid selection. Please choose a valid file.")
        return

    file_path = os.path.join(USER_FILES_DIR, filename)
    content = input("Enter the content to append: ").strip()

    with open(file_path, 'a') as f:
        f.write(content + "\n")

    log_activity("file_modify", {"filepath": file_path, "content_appended": content})
    print(f"File '{filename}' modified successfully.")

def delete_file():
    ensure_user_files_dir()
    files = list_user_files()

    if not files:
        print("No files available to delete. Redirecting to file creation...")
        create_file()
        return

    print("Available files to delete:", files)
    filename = input("Enter the name of the file to delete: ").strip()
    if filename not in files:
        print("Invalid selection. Please choose a valid file.")
        return

    file_path = os.path.join(USER_FILES_DIR, filename)
    os.remove(file_path)

    log_activity("file_delete", {"filepath": file_path})
    print(f"File '{filename}' deleted successfully.")
