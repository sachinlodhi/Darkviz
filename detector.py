# Actual detection happens here
import torch
import time

# Model
model = torch.hub.load("ultralytics/yolov5", "yolov5s")


def predict(img):
    start = time.time()
    results = model(img, size=640)  # includes NMS
    # Get the inferred image
    inferred_img = results.render()[0]
    end = time.time()
    print(f"\nPrediction time: {(end-start)*10**3:.03f}ms")
    return inferred_img
