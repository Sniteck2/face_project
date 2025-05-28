import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_NAME = "Facenet"
DISTANCE_METRIC = "cosine"
THRESHOLD = 0.4

KNOWN_DIR = os.path.join(BASE_DIR, "images")
HAAR_PATH = os.path.join(BASE_DIR, "models", "haarcascade_frontalface_default.xml")
LOG_PATH = os.path.join(BASE_DIR, "logs")