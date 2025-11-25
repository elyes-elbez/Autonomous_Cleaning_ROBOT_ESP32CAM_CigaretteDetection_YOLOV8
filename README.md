Autonomous Cleaning Robot Using Cigarette Detection
==================================================


Project Overview
----------------
This project demonstrates an autonomous cleaning robot capable of detecting cigarette butts using computer vision and performing cleaning actions. The system leverages an ESP32-CAM for image streaming, a YOLOv8 model for cigarette detection, and a microcontroller interface for movement commands.

The robot is designed to navigate an environment autonomously and clean detected cigarette butts efficiently, providing a smart solution for public and private spaces.

Features
--------
- Real-time cigarette detection using YOLOv8.
- Autonomous navigation with directional commands: LEFT, RIGHT, FORWARD.
- Wi-Fi communication between ESP32-CAM and Python processing.
- Live video streaming from ESP32-CAM.
- Serial monitor feedback for monitoring robot commands.
- Modular architecture for easy integration of additional sensors or features.

System Architecture
-------------------
Flow:

1. ESP32-CAM streams live video over Wi-Fi.
2. Python script captures frames and runs the YOLOv8 model to detect cigarette butts.
3. Python calculates the position of detected objects and decides navigation commands.
4. Commands (LEFT, RIGHT, FORWARD) are sent via TCP to the ESP32.
5. ESP32 receives commands and prints them on the Serial Monitor (for debugging) and controls motors/actuators.

Diagram:
[ESP32-CAM] --> Video Stream --> [Python YOLOv8] --> Detect Cigarettes --> Compute Commands --> TCP --> [ESP32] --> Motors

Hardware Components
-------------------
- ESP32-CAM AI-Thinker module
- FTDI USB-to-Serial adapter (for programming ESP32-CAM)
- Motors + motor driver (for robot movement)
- Power supply (LiPo battery recommended)
- Chassis with wheels

Software Components
-------------------
- Python 3.11+
- Ultralytics YOLOv8
- OpenCV (cv2) for video capture and visualization
- ESP32 Arduino Core
- Arduino IDE or PlatformIO for ESP32 programming

Setup Instructions
------------------
1. Flash the ESP32-CAM with the camera + TCP server code.
2. Connect ESP32-CAM to Wi-Fi and note its IP address.
3. Install Python packages:
   pip install ultralytics opencv-python
4. Update the Python script with the ESP32-CAM IP address.
5. Run the Python script to start detection and send commands to ESP32.

Usage
-----
1. Start the ESP32-CAM sketch.
2. Run the Python YOLOv8 script.
3. Observe the Serial Monitor for received commands (LEFT, RIGHT, FORWARD).
4. The robot moves autonomously based on detected cigarette positions.

Future Improvements
-------------------
- Integrate obstacle avoidance sensors (ultrasonic/IR) for safe navigation.
- Add automatic cleaning mechanism (brushes or vacuum).
- Improve YOLOv8 model accuracy with more cigarette butt images.
- Mobile or web interface to monitor robot and camera feed in real-time.

