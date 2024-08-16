# Python Base Image from https://hub.docker.com/r/arm32v7/python/
FROM arm32v7/python:3
ENV SPI_PATH /app/SPI-Py

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the current directory into the container
COPY . .

# Install the Python dependencies
RUN pip3 install --no-cache-dir rpi-gpio
RUN pip3 install --no-cache-dir smbus
RUN pip3 install --no-cache-dir spidev
RUN pip3 install --no-cache-dir requests

# Install /app/SPI-Py
WORKDIR $SPI_PATH
RUN python3 setup.py install

# Set the working directory to where main.py is located
WORKDIR /app/src

# Trigger the Python script
CMD ["python3", "main.py"]
