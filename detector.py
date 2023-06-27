import cv2
import torch
import  time
# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def predict(img):
    start = time.time()

    # Image
    # img = cv2.imread("temp_images/person.jpg")
    # Inference
    results = model(img, size=640)  # includes NMS
    # Get the inferred image
    inferred_img = results.render()[0]
    end = time.time()
    print(f"\nPrediction time: {(end-start)*10**3:.03f}ms")
    return inferred_img

    # # Display the inferred image
    # cv2.imshow("Inferred Image", inferred_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()