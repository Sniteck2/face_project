
import os
from src.config import settings
from deepface import DeepFace

def analyze_image():
    print("Analizando imagenes....")
    for filename in os.listdir(settings.KNOWN_DIR):
        path = os.path.join(settings.KNOWN_DIR, filename)
        try:
            print(f"🔍 Analizando rostro de '{filename}'...")
            DeepFace.represent(img_path=path, enforce_detection=True)
            print(f"✅ Rostro detectado en '{filename}'.")
        except Exception as e:
            print(f" No se detectaron rostros en la imagen '{filename}' .\n Detalles: {e}")