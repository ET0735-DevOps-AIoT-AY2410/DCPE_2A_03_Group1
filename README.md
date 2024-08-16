[![IoT Smart Fire Alert System](https://img.youtube.com/vi/4QGPknpGows/0.jpg)](https://youtu.be/4QGPknpGows)

# IoT Smart Fire Alert System | DCPE/FT/2A/03 Group 1
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
  - Automatically sends alerts to SCDF when a fire is detected or SOS switch is activated.
- **Sprinkler System**: 
  - Automatically activates in case of fire to suppress it.
- **Threshold Adjustment**: 
  - Allow users to adjust the threshold of Temperature and Light threshold to Fire Detection. 
  - Press '1' on the keypad to adjust the temperature threshold or '2' to adjust the light intensity threshold. 
  - During input, users can press the '#' key on the keypad to backspace and correct their entries.
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
## Demo Video
- https://youtu.be/4QGPknpGows
## Installation
**1. Build the Docker Image**
- `docker build -t username/app .`
  
**2. Push to Dockerhub**
- `docker push username/app`
  
**3. Pull from dockerhub**
- `docker pull username/app`
  
**4. Run the container**
- `docker run -d --privileged username/app`

## Contributors
- **Wong Xian Zhe**:
  - Main, Hmi, SOS Switch, Keypad, pytest
- **Bryan Ong Jia Le**:
  - Main, Notification, Keypad, test
- **Avadhanam Srihari Anirudh**:
  - Main, Detection, Deactivation, pytest
- **Shune Lai Hlaing Hmee**:
  - Main, Alarm System, Sprinkler System, Deactivation
