# Python Base Image from https://hub.docker.com/r/arm32v7/python/
FROM arm32v7/python:3
# Set the working directory inside the container
WORKDIR /app

# Copy all files from the current directory into the container
COPY . .

# Install the Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Set the working directory to where main.py is located
WORKDIR /app/src

# Trigger the Python script
CMD ["python3", "main.py"]