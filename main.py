import cv2
import threading
from deepface import DeepFace
from services import preload_recognition, load_recognition
from utils import medition
from camera.config import get_camera_config
from camera.camera_factory import create_camera_instance

images_folder = 'images'

preload_recognition.analyze_image()

caras_conocidas = load_recognition.face_recognition()

def process_camera(camera_id, camera):
    cap = camera.get_capture()
    if not cap.isOpened():
        print(f"❌ Cámara {camera_id} no disponible")
        return

    window_name = f"Vista - {camera_id}"
    print(f"✅ Iniciando {window_name}")

    face_casacade = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')

    while True:
        ret, frame = cap.read()
        if not ret:
            print(f"⚠️ No se pudo leer frame de {camera_id}")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_casacade.detectMultiScale(gray, 1.1, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            face_roi = frame[y:y + h, x:x + w]

            try:
                analysis = DeepFace.analyze(frame, actions=['age','emotion'])
                embedding = DeepFace.represent(img_path=frame, model_name="Facenet")[0]["embedding"]
                found=False
                for cara in caras_conocidas:
                    old_embedding = cara["embedding"]
                    distance = medition.cosine_distance(old_embedding, embedding)
                    if distance < 0.4:
                        text = f"{cara['name']}, {analysis[0]['dominant_emotion']}"
                        found=True
                        break

                if not found:
                    text = " Rostro no reconocido"

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                            0.9, (255, 255, 255), 2)
            except Exception as e:
                cv2.putText(frame, "No se detectaron rostros", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 100, 1000), 2)

        cv2.imshow(window_name, frame)

        if cv2.waitKey(1) & 0xFF == 27:
            print(f"🛑 Cerrando {window_name}")
            break

    cap.release()
    cv2.destroyWindow(window_name)
if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()

    camera_configs = get_camera_config()

    threads = []

    for i, config in enumerate(camera_configs):
        camera = create_camera_instance(config)
        t = threading.Thread(target=process_camera, args=(f"Cam_{i+1}", camera), daemon=False)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()