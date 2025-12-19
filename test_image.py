# yolov8_test_image.py

from ultralytics import YOLO
import cv2

# 1️⃣ Load the trained YOLOv8 model
model = YOLO("cigarette_detection.pt")  # path to your best.pt

# 2️⃣ Load an image
image_path = "test.jpg"
image = cv2.imread(image_path)

# 3️⃣ Run prediction
results = model.predict(source=image_path, save=False, conf=0.25)  # conf = confidence threshold

# 4️⃣ Show results with bounding boxes
# results[0] contains predictions for the first image
for box in results[0].boxes:
    x1, y1, x2, y2 = map(int, box.xyxy[0])
    conf = box.conf[0].item()
    cls = int(box.cls[0].item())
    label = f"{model.names[cls]} {conf:.2f}"
    # Draw rectangle and label
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(image, label, (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

# 5️⃣ Display the image
cv2.imshow("YOLOv8 Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 6️⃣ (Optional) Save the result
cv2.imwrite("output.jpg", image)
print("Detection complete. Output saved as output.jpg")
