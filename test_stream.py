# yolov8_webcam_realtime.py

from ultralytics import YOLO
import cv2
import time

# 1️⃣ Load your trained YOLOv8 model
model = YOLO("cigarette_detection.pt")  # replace with your trained model path

# 2️⃣ Open webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Cannot open webcam")
    exit()

print("Starting real-time YOLOv8 detection. Press 'q' to quit.")

prev_time = 0  # for FPS calculation

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # 3️⃣ Run YOLOv8 prediction on the current frame
    results = model.predict(frame, conf=0.55)  # adjust conf as needed

    # 4️⃣ Draw detections
    class_names = model.names
    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = box.conf[0].item()
        cls = int(box.cls[0].item())
        label = f"{class_names[cls]} {conf:.2f}"

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # 5️⃣ Calculate and display FPS
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time
    cv2.putText(frame, f"FPS: {fps:.1f}", (10, frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    # 6️⃣ Display the frame
    cv2.imshow("YOLOv8 Real-Time Detection", frame)

    # 7️⃣ Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 8️⃣ Release resources
cap.release()
cv2.destroyAllWindows()
