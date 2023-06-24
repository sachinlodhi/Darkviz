import cv2
import torch

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def predict(img):

    # Image
    # img = cv2.imread("temp_images/person.jpg")
    # Inference
    results = model(img, size=640)  # includes NMS
    # Get the inferred image
    inferred_img = results.render()[0]
    return inferred_img

    # # Display the inferred image
    # cv2.imshow("Inferred Image", inferred_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()