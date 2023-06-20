import cv2


class cameraUtils:
    def list_ports():
        is_working = True
        dev_port, working_ports = 0, []
        while is_working:
            try:
                camera = cv2.VideoCapture(dev_port)
                if not camera.isOpened():
                    is_working = False
                    print("Port %s is not working." % dev_port)
                else:
                    is_reading, img = camera.read()
                    if is_reading:
                        print(f"Port {dev_port} is working and reads images")
                        working_ports.append(dev_port)
                    else:
                        print(f"Port {dev_port} for camera is present but does not read.")
                camera.release()
                dev_port += 1
            except cv2.error as e:
                print(f"Camera {dev_port} could not be opened:", str(e))
                dev_port += 1
                continue
        return working_ports


    def get_valid_input(valid_options):
        while True:
            user_input = int(input("Enter the video index you would like to use: "))
            if user_input in valid_options:
                return user_input
            else:
                print(f"Invalid input. Please select a valid input from the available indexes. \
                      \n\n  The available indexes are {valid_options}\n")