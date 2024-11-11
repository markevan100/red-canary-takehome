# Use an Ubuntu-based Python image as the base
FROM python:3.9-bullseye

# Set the working directory
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install necessary dependencies
RUN apt-get update && \
    apt-get install -y curl && \
    pip install --upgrade pip

# Default to starting a shell, the program to be run manually
CMD ["bash"]
