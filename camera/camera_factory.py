import os
from camera.usb_camera import UsbCamera
from camera.ip_camera import IpCamera

def get_camera():
    camera_type = os.getenv("CAMERA_TYPE", "USB").upper()
    if camera_type == 'IP':
        print("Camara IP cargada...")
        return IpCamera()
    print("Camara USB cargada...")
    return UsbCamera()