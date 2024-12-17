from ultralytics import YOLO
import cv2

# Load the YOLO model
model = YOLO("best.pt")  # Replace "best.pt" with the path to your model

# Initialize the webcam
cap = cv2.VideoCapture(0)  # Use 0 for the default webcam

if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

# Process the video frames
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Predict using YOLO model
    results = model(frame)

    # Draw the detections on the frame
    annotated_frame = results[0].plot()

    # Display the frame
    cv2.imshow("YOLOv8 Live Prediction", annotated_frame)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
