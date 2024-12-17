from ultralytics import YOLO
import cv2

# Load the YOLO model
model = YOLO("yolo11n.pt")  # Replace "yolov8n.pt" with your YOLO model path

# Initialize the camera
cap = cv2.VideoCapture(0)  # Change index if multiple cameras are connected (e.g., 1, 2)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Unable to access the camera.")
    exit()

# Process video feed frame by frame
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to fetch frame from the camera.")
        break

    # Run YOLO inference on the frame
    results = model.predict(source=frame, show=False)  # Set show=True for real-time visualizations

    # Draw results on the frame
    annotated_frame = results[0].plot()

    # Display the frame
    cv2.imshow("YOLO Live Detection", annotated_frame)

    # Exit loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the resources
cap.release()
cv2.destroyAllWindows()
