# THIS IS THE DRIVER FILE. Run it after installing all the requirements.
import PySimpleGUI as sg
import initial_setup as setup
import threading
import connector

ip = ""


def main():
    global ip
    layout = [
        [sg.Text("Connect the android by the USB cable and click Verify button")],
        [sg.Button("Verify"), sg.Text("Disconnected", key="-STATUS-")],
        [sg.Button("Switch Connection"), sg.Text("USB", key="-SWITCH-")],
        [sg.Text("Logs")],
        [sg.Output(size=(60, 15))],  # Log section
        [sg.Button("Start Detection"), sg.Button("Exit")],
    ]

    # a couple of buttons
    window = sg.Window("DarkViz", layout)
    while True:  # Event Loop
        event, values = window.Read()
        if event in (None, "Exit"):  # checks if user wants to
            exit
            break
        # Connection Verify
        if event == "Verify":
            connection = setup.verify_connection()
            if connection:
                window["-STATUS-"].update("Connected.")
                ip = setup.extract_ip()
                print(ip)
        # Switching from USB to wifi
        if event == "Switch Connection":
            setup.connect_ip(ip)
            window["-SWITCH-"].update("Over Wifi")
            print(
                "Please launch the camera manually and then setup the configuration in camera manually."
            )
        # Start detection
        if event == "Start Detection":
            cam_num = 0
            # t1 = threading.Thread(target=temp.feed, args=(cam_num,), daemon=True)
            t1 = threading.Thread(target=connector.launch, args=(), daemon=True)
            t1.start()
            # t1.join(1)
    window.Close()


# Driver function call
main()


# Windwo for the terminal logs. UNCOMMENT IF FACING ANY ERROR OTHERWISE LEAVE AS IT IS.
# def runCommand(cmd, timeout=None, window=None):
#     p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#     output = ''
#     for line in p.stdout:
#         line = line.decode(errors='replace' if (sys.version_info) < (3, 5) else 'backslashreplace').rstrip()
#         output += line
#         print(line)
#         window.Refresh() if window else None        # yes, a 1-line if, so shoot me
#     retval = p.wait(timeout)
#     return (retval, output)                         # also return the output just for fun
