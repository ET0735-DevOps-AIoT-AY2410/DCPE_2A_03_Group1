# Python Base Image from https://hub.docker.com/r/arm32v7/python/
FROM arm32v7/python:3

WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install --no-cache-dir smbus
RUN pip3 install --no-cache-dir spidev

# Copy the code into the container
COPY main.py ./
COPY hal ./hal

WORKDIR /app
# Define the command to run  your application
CMD [ "python3", "./main.py" ]