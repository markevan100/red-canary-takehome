# Red Canary Take-Home Project

## Overview
This project is a test application built for Red Canary to test EDR telemetry. With this application, a user can perform various actions on a system and log the activity. Those activity logs can then be used to corroborate the telemetry data reported by the EDR system. 

I chose Python for this project because I theorized that some of the built-in libraries that Python provides, like os, subprocess, or socket, would make interaction with the operating system and file system or making network connections easier. Given the smaller scope of this project, I don’t believe that anything was necessarily easier to do in Python compared to Ruby. However, it is possible that, as the project grows, those libraries would be beneficial in the future. 

Given that the team already works with Python projects, I think it was a good language choice but not a necessary one. For me personally, it made the project especially fun as it is a language that I am much less familiar with but have been working on learning. If I were to join the Red Canary team, I'd hope to get a chance to contribute to the Python projects.

For cross system testing, I tested locally on my Mac and created a Docker setup to run Ubuntu Linux and test there. Given that they are both Unix based, I did not find any commands that did not work on both operating systems. There are unit tests in the project, they can be run using `unittest`. 

I opted for a prompt-based system with the intention of making the program as user friendly as possible. When the user starts the program, it will ask them which action they would like to test. Based on their selection, there are follow-up questions. Once that action has been completed, the user is returned to the 'main menu' and can test another action. For now, the logging is done for each User Session into its own, timestamped activity log file. So, for now, each user session will generate its own file, but it would be simple to change that to build a running file for all of the logging. For the purpose of this project, having separate files facilitated manual testing.

### Features
There are three different types of actions, and some actions provide further options. 

- **Process Start**: Simulate the start of a process and log its details, including the process ID and command used.
- **File Actions**: Handle file creation, modification, and deletion while ensuring that only files created during the session can be modified or deleted.
- **Network Connect**: Perform network requests, either GET or POST with data, logging the necessary information such as the destination address, source address, and amount of data sent.

### Future Considerations
With more time to work on this project, these are the things that I would handle next. 

- **Input Validation**: We could add more input validation to ensure that URLs, ports, and request types are correctly formatted and valid. We do have some, like adding an http or https to a url if it isn't provided, but there is a lot more that we could do to validate that urls are formatted correctly, that process commands are valid, etc. 
- **Error Handling**: More advanced error handling could be implemented to retry failed requests or handle different types of network errors. 
- **Cross-Platform Docker Setup**: Adding in a Windows environment to my docker setup

## Requirements
- Python 3.x
- Docker (optional, for containerized testing)
- Docker Compose (optional, for multi-container setup)

## Usage
### 1. Running Tests
You can run the tests locally using `unittest`:
```bash
python3 -m unittest discover tests
```

Alternatively, you can use Docker to run the tests in an Ubuntu Linux environment:
```bash
docker-compose up telemetry_tests
```

### 2. Running the App
To run the telemetry tester app manually, you can use:
```bash
python3 src/telemetry_tester.py
```

Or, using Docker in the Linux setup:
```bash
docker-compose up telemetry_app
```

## Files and Directories
- **`src/`**: Contains the main application code and action logic.
- **`tests/`**: Contains unit tests for process actions, file actions, and network requests.
