# Use an official Python runtime as the base image
FROM balenalib/raspberrypi3-debian-python:latest

# Set the working directory in the container
WORKDIR /App

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose a port (if needed)
EXPOSE 8000

# Define the command to run  your application
CMD [ "python", "App.py" ]