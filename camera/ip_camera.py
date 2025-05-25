import cv2
import os
from camera.usb_camera import UsbCamera

class IpCamera(UsbCamera):
    def get_capture(self):
        ip_url = os.getenv('IP_CAMERA_URL')
        return cv2.VideoCapture(ip_url)