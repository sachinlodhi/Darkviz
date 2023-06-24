# # import time
# #
# # def testing():
# #     for i in range(10):
# #         time.sleep(2)
# #         print("Hey working")
#
#
import cv2
import detector

def feed(cam_num):
    print("here:", cam_num)
    cap = cv2.VideoCapture(cam_num)
    while True:
        _, img = cap.read()
        input_img = img.copy()
        detected_obj = detector.predict(img)
        cv2.imshow("input", input_img)
        cv2.imshow("Predicted", detected_obj)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()  # Release the camera
    cv2.destroyAllWindows()  # Close any OpenCV windows


#
# import cv2
#
# def create_capture():
#     return cv2.VideoCapture(0)  # Create a new cv2.VideoCapture object
#
# def testing(cap):
#     while True:
#         ret, frame = cap.read()
#         if not ret:  # Check if the frame was successfully captured
#             break
#         cv2.imshow("Live", frame)
#         if cv2.waitKey(10) & 0xFF == ord('q'):
#             break
#     cv2.destroyAllWindows()  # Close any OpenCV windows
