# IoT Smart Fire Alert System | DCPE/FT/2A/03 Group 1
## Overview
### 
The IoT Smart Fire Alert System is designed to enhance fire safety, specifically tailored for the individual living independently. The system continuously monitors the environment for potential fire hazards, alerts residents through an alarm system, and automatically notifies the Singapore Civil Defense Force (SCDF) in case of an emergency. It also features an automatic sprinkler system to suppress fires and manual SOS functionalities for urgent help.
## Features
### 
- **Automatic Fire Detection**:
  - Monitors temperature and light intensity to detect fires.
- **Manual SOS Switch**: 
  - Allows residents to alert SCDF for urgent help.
- **Fire Alarm Deactivation**: 
  - Allows authorized personnel to deactivate the alarm in case of false activation.
- **SCDF Notification System**: 
  - Automatically sends alerts to SCDF when a fire is detected or SOS switch is activated.
- **Sprinkler System**: 
  - Automatically activates in case of fire to suppress it.
- **Threshold Adjustment**: 
  - Allow users to adjust the threshold of Temperature and Light threshold to Fire Detection
## Hardware Requirements
- Raspberry Pi Development Board
- **Sensors**:
  - Temperature and Humidity Sensor
  - Light Dependent Resistor (LDR)
- **Actuators**:
  - Servo Motor (for sprinkler control)
  - Buzzer (for alarm)
  - LED (for visual alerts)
- **Input Devices**:
  - Keypad (for menu configuration)
  - RFID Reader (for alarm deactivation)
  - Slide Switch (for SOS activation)
- **Output Devices**:
  - LCD Display (for system status and configuration display)
## Software Requirements
- **Programming Languages**:
  - Python, HTML
- **Development Environment**:
  - Raspberry Pi OS 
- **Libraries**:
  - RPi.GPIO (for Raspberry Pi GPIO control)
  - SMS API (for SMS notifications)
## Installation
Build the Docker Image: Run the following command in your terminal from the root of your project to build the Docker image.
- docker build -t my-raspi-app .

Run the Docker Container: After building the image, you can run the container with:
- docker run --privileged -it --rm my-raspi-app
## Contributors
- **Wong Xian Zhe**:
  - Main, Hmi, SOS Switch
- **Bryan Ong Jia Le**:
  - Main, Notification
- **Avadhanam Srihari Anirudh**:
  - Main, Fire Detection, Deactivation
- **Shune Lai Hlaing Hmee**:
  - Main, Alarm System, Sprinkler System, Deactivation
