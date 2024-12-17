from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt")

# Train the model
train_results = model.train(
    data="data.yaml",  # path to dataset YAML
    epochs=100,  # number of training epochs
    imgsz=416,  # training image size
    patience=10,  # stop if no improvement for 10 epochs
    device='cpu',  # device to run on, i.e. device=0 or device=0,1,2,3 or device=cpu
)

# Evaluate model performance on the validation set
metrics = model.val()

# Perform object detection on an image
results = model("test/images/images_267-2-_jpg.rf.f53291f28f321074c5229e6f7f7728e2.jpg")
results[0].show()

# Export the model to ONNX format
path = model.export(format="onnx")  # return path to exported model