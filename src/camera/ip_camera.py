import cv2
from src.camera.base import BaseCamera

class IpCamera(BaseCamera):
    def __init__(self, url):
        self.camera_type = "IP"
        self.source = url
        self.url = url

    def get_capture(self):
        return cv2.VideoCapture(self.url)