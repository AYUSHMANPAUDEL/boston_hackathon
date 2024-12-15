from django.shortcuts import render

# Create your views here.
import cv2
import numpy as np
from django.http import JsonResponse
from ultralytics import YOLO
from django.views.decorators.csrf import csrf_exempt
from django.http import StreamingHttpResponse
import base64
import cv2
import numpy as np
from django.http import JsonResponse
from ultralytics import YOLO
from django.views.decorators.csrf import csrf_exempt

# Load the YOLO model
model = YOLO("home/best.pt")  # Replace with your .pt model path

@csrf_exempt
def process_video(request):
    """
    Receive video frame from the frontend, perform YOLO inference, and return results.
    """
    if request.method == 'POST' and request.FILES.get('frame'):
        # Read the uploaded frame
        frame = request.FILES['frame']
        np_frame = np.frombuffer(frame.read(), np.uint8)
        img = cv2.imdecode(np_frame, cv2.IMREAD_COLOR)

        # Perform inference
        results = model.predict(source=img)

        # Prepare a list to store the detections
        detections = []

        # Process detections
        for box in results[0].boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0].cpu().numpy())
            conf = box.conf[0].item()
            cls = int(box.cls[0].item())
            if cls == 1 :
                cls = "No Helmet"
            else:
                cls = "Helmet"
            label = f"Class {cls} ({conf:.2f})"

            # Store detection details
            detections.append({
                'label': label,
                'confidence': conf,
                'x': x1,
                'y': y1,
                'width': x2 - x1,
                'height': y2 - y1
            })

            # Draw the bounding box and label on the frame
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Encode the processed image to base64
        _, buffer = cv2.imencode('.jpg', img)
        img_base64 = base64.b64encode(buffer).decode('utf-8')

        # Send detections and image as base64 in the response
        response = {
            'detections': detections,
            'image': img_base64
        }

        return JsonResponse(response, safe=False)

    return JsonResponse({'error': 'Invalid request'}, status=400)

def traffic_cam(request):
    return render(request,"home/traffic_cam.html")