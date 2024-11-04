from actions.process_action import handle_process_action

def main():
    print("Welcome to Modak's EDR Telemetry Test Program")
    
    while True:
        print("\nAvailable actions: process_start (ps), exit")
        action = input("What action would you like to test? ").strip().lower()

        if action in ["ps", "process_start"]:
            print("Process start selected.")
            handle_process_action()

        elif action == "exit":
            print("Exiting the Telemetry Test Program.")
            break

        else:
            print("Invalid action selected. Please choose a valid option.")

if __name__ == "__main__":
    main()