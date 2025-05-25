
import cv2
from camera.base import BaseCamera

class UsbCamera(BaseCamera):
    def get_capture(self):
        return cv2.VideoCapture(0)