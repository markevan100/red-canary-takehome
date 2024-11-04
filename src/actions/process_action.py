import subprocess
import getpass
import os
import signal

def handle_process_action():
    print("Enter the command to start the process.")
    print("For example: 'echo Hello'.")
    command = input("Command: ").strip()

    try:
        process = subprocess.Popen(command, shell=True)
        pid = process.pid
        username = getpass.getuser()
        print(f"\033[92mProcess started with command: {command}, PID: {pid}, User: {username}\033[0m")

        process.poll()
        if process.returncode is None:
            os.kill(pid, signal.SIGTERM)
            print(f"Process with PID {pid} was terminated.")

    except Exception as e:
        print(f"Failed to start process: {e}")
