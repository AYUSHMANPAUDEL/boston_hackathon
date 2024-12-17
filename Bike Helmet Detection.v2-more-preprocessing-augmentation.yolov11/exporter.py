# Load the best model
from ultralytics import YOLO
model = YOLO("runs/detect/train/weights/best.pt")

metrics = model.val()

# Perform object detection on an image
results = model("test/images/BikesHelmets150_png_jpg.rf.347400d070a36faf53bd1ace27a3dd43.jpg")
results[0].show()

# Export to ONNX format
path = model.export(format="onnx")
print(f"Best model exported to: {path}")
