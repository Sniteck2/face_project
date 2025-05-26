from camera.usb_camera import UsbCamera
from camera.ip_camera import IpCamera

def create_camera_instance(config):
    if config["type"] == "IP":
        return IpCamera(config["url"])
    elif config["type"] == "USB":
        return UsbCamera(config["index"])