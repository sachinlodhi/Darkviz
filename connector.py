import subprocess
import detector
import cv2

temp_directory = "/home/sachin/Personal/Projects/Python/animal_intrusion_1/temp_images/"  # to store clicked file temporarily on machine
def retrieve_file(): # retrieve filename to dump it locally
    cmd = "adb shell ls -lt /sdcard/DCIM/Camera/ | awk 'NR>1 {print $NF; exit}'"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    filename = result.stdout.strip()
    print(filename)
    download_cmd = f"adb pull /sdcard/DCIM/Camera/{filename}  {temp_directory}"
    subprocess.run(download_cmd, shell=True)
    delete_cmd = f"adb shell rm /sdcard/DCIM/Camera/{filename}"
    # subprocess.run(delete_cmd, shell=True)
    return filename

def send_keyevent(keycode): # click picture
    command = f"adb shell input keyevent {keycode}"
    subprocess.run(command, shell = True)

def launch():
    print("In launch")
    cv2.namedWindow("input", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Predicted", cv2.WINDOW_NORMAL)
    font = cv2.FONT_HERSHEY_SIMPLEX

    # fontScale
    fontScale = 10
    # Blue color in BGR
    color = (255, 0, 0)
    # Line thickness of 2 px
    thickness = 5
    ctr = 0
    while True:
        send_keyevent(24)  # clicking ol down key to capture picture
        print("Clicked")
        # cap =cv2.VideoCapture(2) # change it later and provide option in the window layout
        imgHolder, detectHolder = 0, 0  # image holding variables
        try:
            filename = temp_directory + retrieve_file()
            if filename[-3:] != "jpg": # do not retrieve other media files like mp4
                continue

            print("Image retrived")
            img = cv2.imread(filename)
            input_img = img.copy()
            detected_obj = detector.predict(img)
            cv2.imshow("input", input_img)
            detected_obj = cv2.putText(detected_obj, str(ctr), (200,200), font,
                                fontScale, color, thickness)
            cv2.imshow("Predicted", detected_obj)
            cv2.imwrite(temp_directory + "pred_" + str(ctr) + ".jpg", detected_obj)
            imgHolder, detectHolder = input_img, detected_obj
            ctr += 1
            print("try block")
        except:
            cv2.imshow("input", input_img)
            cv2.imshow("Predicted", detected_obj)
            print("except block")
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    # os.remove(filename)
    cv2.destroyAllWindows()
