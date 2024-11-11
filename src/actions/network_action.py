import subprocess
import os
import socket
from logger import log_activity

def handle_network_action():
    url = input("Enter the destination URL (e.g., http://httpbin.org): ").strip()
    if not url.startswith("http://") and not url.startswith("https://"):
      url = "http://" + url

    port = input("Enter the port (default is 80 for HTTP): ").strip() or "80"
    request_type = input("Enter request type (GET/POST): ").strip().upper()
    data = None
    if request_type == "POST":
        data = input("Enter data to send with POST request (in key=value format): ").strip()

    command = ["curl", "-i", f"{url}:{port}"]
    if request_type == "POST" and data:
        command.extend(["-d", data])

    try:
        subprocess.run(command, capture_output=True, text=True, check=True)
        source_address = socket.gethostbyname('localhost')
        data_size = len(data) if data else 0

        log_activity("network_request", {
            "request_type": request_type,
            "destination_address": url,
            "destination_port": port,
            "protocol": request_type,
            "data_sent": data if data else "N/A",
            "amount_of_data_sent": data_size,
            "source_address": source_address,
            "process_name": "curl",
            "process_id": os.getpid()
        })

        print(f"Network request to {url} completed successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Failed to complete network request: {e}")
