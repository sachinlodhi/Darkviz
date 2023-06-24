import subprocess
import time
# Function to check if the device is connected using ADB
def verify_connection():
    cmd = "adb devices"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    try:
        # print("hi")
        device = str(result.stdout.rstrip().split("\n")[1]).split("	")[0]
        # print(device)
        print("Connected. OK.")
        print(f"Device Code:", device)
        return True
    except:
        print("Device is not connected!!! Try again.")
    return False

# Function to extract the IP of the connected device
def extract_ip():
    cmd = "adb shell ifconfig"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    error = result.stderr.rstrip()
    if error:
        print("Already conneted over wifi and USB both. Remove USB.")
    else:
        result = result.stdout.rstrip()
        result = result.split("\n")
        ip = [i.strip() for i in result if "inet addr:192.168" in i][0].split(" ")[1][5:]
        # print(ip)
        return ip



# Changing connection mode to wifi
def connect_ip(response_ip):
    cmd = "adb tcpip 5555"
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True) # assigning port
    print(result.stdout.rstrip())
    cmd = f"adb connect {response_ip}:5555"
    result = subprocess.run(cmd, capture_output=True, text= True, shell=True)
    print(result.stdout.rstrip())


# Starting Camera : NEED TO LAUNCH CAMERA MANUALLY. NOT WORKING BY COMMAND
def start_camera():
    print("Starting camera")
    cmd = "adb shell monkey -p com.android.camera -v 1"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    time.sleep(10)
    print(result.stdout.rstrip())

#
# VER_CON = verify_connection()
# # if device is connected
# if VER_CON:
#     try:
#         response_ip = extract_ip()
#         print(response_ip)
#     except:
#         print("Already connected over WiFi. Disconnet from USB.")
#     connect_ip(response_ip)
#     # remove device from USB connection
#     start_camera()





