import cv2
from ultralytics import YOLO
import socket

# Load the YOLOv8 model
model = YOLO("cigarette_detection.pt")

# ESP32 IP address and port
ESP32_IP = "IP_Adress"  # <-- Change to your ESP32 IP
ESP32_PORT = 5000
url = "http://ip_adress/stream"  # CHANGE THIS TO YOUR IP
# Connect to ESP32 over TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ESP32_IP, ESP32_PORT))
print(f"Connected to ESP32 at {ESP32_IP}:{ESP32_PORT}")

# Use camera (0 = default webcam) url=ESP32-cam
cap = cv2.VideoCapture(url)

# Zones for LEFT / RIGHT / FORWARD
LEFT_ZONE = 0.33
RIGHT_ZONE = 0.66

while True:
    success, frame = cap.read()
    if not success:
        continue

    # Run YOLO inference
    results = model(frame, imgsz=320)
    annotated = results[0].plot()

    if len(results[0].boxes) > 0:
        box = results[0].boxes[0]
        x1, y1, x2, y2 = box.xyxy[0]

        # Calculate center
        cx = int((x1 + x2) / 2)
        cy = int((y1 + y2) / 2)
        h, w, _ = frame.shape
        center_norm = cx / w

        # Decide command
        if center_norm < LEFT_ZONE:
            command = "LEFT\n"
        elif center_norm > RIGHT_ZONE:
            command = "RIGHT\n"
        else:
            command = "FORWARD\n"

        # Send command over TCP to ESP32
        sock.sendall(command.encode())
        print("Sent:", command.strip())

        # Draw center point
        cv2.circle(annotated, (cx, cy), 5, (255, 0, 0), -1)

    cv2.imshow("YOLOv8 + ESP32-CAM", annotated)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC key to exit
        break

cap.release()
cv2.destroyAllWindows()
sock.close()
