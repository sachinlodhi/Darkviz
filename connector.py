import subprocess
import time
import detector
import cv2
import os

temp_directory = "/home/sachin/Personal/Projects/Python/animal_intrusion1/temp_images/"
def retrieve_file():
    cmd = "adb shell ls -lt /sdcard/DCIM/Camera/ | awk 'NR>1 {print $NF; exit}'"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    filename = result.stdout.strip()
    print(filename)
    download_cmd = f"adb pull /sdcard/DCIM/Camera/{filename}  {temp_directory}"
    subprocess.run(download_cmd, shell=True)
    delete_cmd = f"adb shell rm /sdcard/DCIM/Camera/{filename}"
    # subprocess.run(delete_cmd, shell=True)
    return filename

def send_keyevent(keycode):
    command = f"adb shell input keyevent {keycode}"
    subprocess.run(command, shell = True)




cv2.namedWindow("input", cv2.WINDOW_NORMAL)
cv2.namedWindow("Predicted", cv2.WINDOW_NORMAL)

cap =cv2.VideoCapture(2)
ctr = 0
while True:
    imgHolder, detectHolder = 0,0 # image holding variables
    # _,img = cap.read()
    send_keyevent(24)
    # time.sleep(5) # will have to set this according to the S value in the camera
    try:
        filename = temp_directory + retrieve_file()
        img = cv2.imread(filename)
        input_img = img.copy()
        detected_obj = detector.predict(img)
        cv2.imshow("input", input_img)
        cv2.imshow("Predicted", detected_obj)
        cv2.imwrite(temp_directory+"predicted/"+str(ctr)+".jpg", detected_obj)
        imgHolder, detectHolder = input_img, detected_obj
        ctr += 1
        print("try block")
    except:
        cv2.imshow("input", input_img)
        cv2.imshow("Predicted", detected_obj)
        print("except block")

    # os.remove(filename)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()


