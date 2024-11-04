import subprocess
import os
import signal
from logger import log_activity

def handle_process_action():
    print("Enter the command to start the process.")
    print("For example: 'echo Hello'.")
    command = input("Command: ").strip()

    try:
        process = subprocess.Popen(command, shell=True)
        pid = process.pid
        process_name = command.split()[0]

        print(f"Process started with command: {command}, PID: {pid}")
        
        log_activity("process_start", {
            "command": command,
            "process_id": pid,
            "process_name": process_name,
        })

        if process.poll() is None:
            os.kill(pid, signal.SIGTERM)

    except Exception as e:
        print(f"Failed to start process: {e}")