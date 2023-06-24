# 📷 Android Camera Object Detection with YOLOv5

![Android Camera Object Detection](https://example.com/path/to/image.png)

This project aims to provide a solution for object detection in low-light conditions using the Android camera. It utilizes YOLOv5, a state-of-the-art real-time object detection model, to identify objects in the captured images. The project is specifically designed to assist farmers in detecting objects of interest in low-light environments.

## Features

- Capture images from the Android camera using ADB commands
- Apply YOLOv5 for real-time object detection
- Highlight and label detected objects
- Designed for low-light conditions
- Targeted towards farmers and agricultural applications

## Requirements

- Android device with camera
- ADB (Android Debug Bridge) installed on your computer
- YOLOv5 model and weights
- Python environment with the required dependencies

## Setup

1. Clone the repository:

   ```
   git clone https://github.com/sachinlodhi/LL_IntDet.git
   ```

2. Connect your Android device to your computer via USB.



3. Enable USB debugging on your Android device.


## Connecting Android Device using ADB over Wi-Fi

To connect your Android device to your computer using ADB over Wi-Fi, follow these steps:

1. Connect your Android device to your computer via USB.

2. Enable USB debugging on your Android device.

3. Open a terminal or command prompt on your computer.

4. Run the following command to check if your device is recognized:
```shell
adb devices
```
You should see your device listed as a connected device.

5. Run the following command to connect your device over Wi-Fi:
```shell
adb tcpip 5555
```


6. Disconnect your Android device from the computer.

7. Find the IP address of your Android device. You can usually find it in the Settings under "About phone" or "About device."

8. Run the following command to connect to your device over Wi-Fi:

```shell
adb connect <android-device-ip-address>:5555
```
Replace `<device-ip-address>` with the actual IP address of your device.

9. If the connection is successful, you should see a message indicating that the device is connected.

10. You can now disconnect the USB cable from your Android device.

11. Install the required Python dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Launch the application on your computer.

2. Open a terminal and navigate to the project directory.

3. Connect your Android device to your computer via USB.

4. Ensure that USB debugging is enabled on your Android device.

5. Run the application:

   ```
   python connector.py
   ```

6. The application will send ADB commands to the Android device to capture images.

7. YOLOv5 will process the captured images and detect objects.

8. Detected objects will be highlighted and labeled on the images.

9. The results can be accessed and analyzed within the application.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Make your changes and commit them.

4. Push your changes to your forked repository.

5. Submit a pull request to the main repository.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- YOLOv5 - [https://github.com/ultralytics/yolov5](https://github.com/ultralytics/yolov5)
- Android Debug Bridge (ADB) - [https://developer.android.com/studio/command-line/adb](https://developer.android.com/studio/command-line/adb)

## Contact

If you have any questions, suggestions, or feedback, please feel free to contact me at [your-email@example.com](mailto:your-email@example.com).

Happy object detecting! 😊🌱📷