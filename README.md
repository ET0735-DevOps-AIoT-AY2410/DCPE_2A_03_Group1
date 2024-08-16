# IoT Smart Fire Alert System | DCPE/FT/2A/03 Group 1
[![IoT Smart Fire Alert System](https://img.youtube.com/vi/4QGPknpGows/0.jpg)](https://youtu.be/4QGPknpGows)
###
(Click to View Demo Video on YouTube)
###
## Overview
### 
The IoT Smart Fire Alert System is designed to enhance fire safety, specifically tailored for the individual living independently. The system continuously monitors the environment for potential fire hazards, alerts residents through an alarm system, and automatically notifies the Singapore Civil Defense Force (SCDF) in case of an emergency. It also features an automatic sprinkler system to suppress fires and manual SOS functionalities for urgent help.

## Features
### 
- **Automatic Fire Detection**:
  - Monitors temperature, light intensity, and smoke levels to detect fires.
  - **Enhanced Detection Logic**: Fire is detected if smoke is sensed in combination with either high light intensity or temperature above a threshold.
- **Manual SOS Switch**: 
  - Allows residents to alert SCDF for urgent help.
- **Fire Alarm Deactivation**: 
  - Allows authorized personnel to deactivate the alarm in case of false activation or fire has been eliminated
- **SCDF Notification System**: 
  - Automatically sends alerts (Telegram and Email) to SCDF when a fire is detected or SOS switch is activated.
  - System configuration file: `notif_config.json` can be modified to change location displayed in notifications and recipient email (SCDF).
- **Sprinkler System**: 
  - Automatically activates sprinkler valve in case of fire to suppress it.
- **Threshold Adjustment Menu**: 
  - Allow users to adjust the threshold of Temperature and Light detection threshold for Fire Detection. 
  - Press '1' on the keypad to adjust the temperature threshold or '2' to adjust the light intensity threshold. 
  - During input, users can press the '#' key on the keypad to backspace and correct their entries.
  - Users can press the '*' key to enter adjustment menu, and to return.
## Hardware Requirements
- Raspberry Pi Development Board
- **Sensors**:
  - Temperature and Humidity Sensor (DHT11)
  - Light-Dependent Resistor (LDR)
- **Actuators**:
  - Servo Motor (for Sprinkler valve control)
  - Buzzer (for Alarm)
  - Light Emitting Diode (LED)
- **Input Devices**:
  - Keypad (for Menu configuration)
  - RFID Reader (for Alarm deactivation)
  - Slide Switch (for SOS activation)
- **Output Devices**:
  - LCD Display (for system status and configuration display)
## Software Requirements
- **Programming Languages**:
  - Python
- **Development Environment**:
  - Raspberry Pi OS 
- **Libraries**:
  - RPi.GPIO (for Raspberry Pi GPIO control)
  - SMBUS (for Raspberry Pi I2C control)
  - SPIDEV (for Raspberry Pi SPI control)
  - Requests (Handles HTTP requests for Telegram Notification) 
## Installation
**1. Pull from dockerhub**
- `docker pull bryrybry/devops_grp1_2a03`
  
**2. Run the container**
- `docker run -d --privileged bryrybry/devops_grp1_2a03`
[Dockerhub Repository](https://hub.docker.com/repository/docker/bryrybry/devops_grp1_2a03)
## Contributors
- **Wong Xian Zhe**:
  - Main, HMI, SOS Switch, Keypad, pytest, Docker Containerisation
- **Bryan Ong Jia Le**:
  - Main, Notification, Hardware Testing, Docker Containerisation
- **Avadhanam Srihari Anirudh**:
  - Main, Detection, Deactivation, Pytest
- **Shune Lai Hlaing Hmee**:
  - Main, Alarm System, Sprinkler System, Deactivation
