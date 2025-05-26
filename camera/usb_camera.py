import cv2
from camera.base import BaseCamera

class UsbCamera(BaseCamera):
    def __init__(self, index):
        self.index = index

    def get_capture(self):
        return cv2.VideoCapture(self.index)