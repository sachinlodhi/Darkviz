
import PySimpleGUI as sg
import initial_setup as setup
import temp
import threading
import multiprocessing
import connector
ip=""
def main():
    global ip
    layout = [
        [sg.Text('Connect the android by the USB cable and click Verify button')],
        [sg.Button('Verify'),sg.Text('Disconnected', key='-STATUS-')],
        [sg.Button('Switch Connection'), sg.Text('USB', key='-SWITCH-')],
        # [sg.Input(key='_IN_')],             # input field where you'll type command
        [sg.Text("Logs")],
        [sg.Output(size=(60,15))],          # an output area where all print output will go
        [sg.Button('Start Detection'), sg.Button('Exit')],

                ]
    # a couple of buttons
    window = sg.Window('Yolov5', layout)
    while True:             # Event Loop
        event, values = window.Read()
        if event in (None, 'Exit'):         # checks if user wants to
            exit
            break
        if event == 'Run':                  # the two lines of code needed to get button and run command
            pass
            # runCommand(cmd=values['_IN_'], window=window)

        # Connection Verify
        if event == "Verify":
            connection = setup.verify_connection()
            if connection:
                window['-STATUS-'].update('Connected.')
                ip = setup.extract_ip()
                print(ip)

        # Switching from USB to wifi
        if event == "Switch Connection":
            setup.connect_ip(ip)
            window['-SWITCH-'].update('Over Wifi')
            print("Please launch the camera manually and then setup the configuration in camera manually.")

        # Start detection
        if event == "Start Detection":
            cam_num = 0
            # t1 = threading.Thread(target=temp.feed, args=(cam_num,), daemon=True)
            t1 = threading.Thread(target=connector.launch, args=(), daemon=True)
            t1.start()
            # t1.join(1)
    window.Close()

main()



# This function does the actual "running" of the command.  Also watches for any output. If found output is printed
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


