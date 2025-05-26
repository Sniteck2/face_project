import cv2
from camera.base import BaseCamera

class IpCamera(BaseCamera):
    def __init__(self, url):
        self.url = url

    def get_capture(self):
        return cv2.VideoCapture(self.url)