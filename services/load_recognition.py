import os
from deepface import DeepFace
from config import settings

def face_recognition():
    model_know = []
    print("Cargando imagenes....")
    for filename in os.listdir(settings.KNOWN_DIR):
        path = os.path.join(settings.KNOWN_DIR, filename)
        try:
            representation = DeepFace.represent(img_path=path, model_name=settings.MODEL_NAME)[0]
            model_know.append({
                "name": filename.split(".")[0],
                "embedding": representation["embedding"],
            })
            print(f" {filename} cargado.")
        except Exception as e:
            print(f" Error cargando {filename}: {e}")
    return model_know