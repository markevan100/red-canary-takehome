import json
import os
import getpass
from datetime import datetime

SESSION_LOG_DIR = 'activity_logs'
if not os.path.exists(SESSION_LOG_DIR):
    os.makedirs(SESSION_LOG_DIR)

session_log_file = os.path.join(SESSION_LOG_DIR, f'activity_log_{datetime.now().isoformat()}.json')

USERNAME = getpass.getuser()

def log_activity(action, details):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "action": action,
        "username": USERNAME,
        "details": details
    }

    try:
        with open(session_log_file, 'r') as session_file:
            log_entries = json.load(session_file)
    except (FileNotFoundError, json.JSONDecodeError):
        log_entries = []

    log_entries.append(entry)

    with open(session_log_file, 'w') as session_file:
        json.dump(log_entries, session_file, indent=4)

    print(f"\033[92mSuccessfully logged {action}.\033[0m")
