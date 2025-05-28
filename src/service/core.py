import time
import cv2
from deepface import DeepFace
from src.service import load_recognition, preload_recognition
from src.utils import medition
from src.config import settings


class CameraProcessor:
    def __init__(self, camera_id, camera, name, fps=15):
        preload_recognition.analyze_image()
        self.camera_id = camera_id
        self.camera = camera
        self.name = name
        self.fps = fps
        self.frame_delay = 1.0 / fps
        self.faces_db = load_recognition.face_recognition()
        self.face_detector = cv2.CascadeClassifier(settings.HAAR_PATH)
        self.stop = False

    def run(self):
        cap = self.camera.get_capture()
        if not cap.isOpened():
            print(f"❌ Cámara {self.name} no disponible")
            return

        window_name = f"Vista - {self.name}"
        print(f"✅ Iniciando {window_name}")
        try:
            while not self.stop:
                ret, frame = cap.read()
                if not ret:
                    print(f"⚠️ Reintentando cámara {self.name}")
                    time.sleep(1)
                    cap.release()
                    cap = self.camera.get_capture()
                    continue

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = self.face_detector.detectMultiScale(gray, 1.1, 5)

                for (x, y, w, h) in faces:
                    face_roi = frame[y:y + h, x:x + w]
                    try:
                        analysis = DeepFace.analyze(frame, actions=['age','emotion'], enforce_detection=False)
                        embedding = DeepFace.represent(img_path=frame, model_name="Facenet", enforce_detection=False)[0]["embedding"]
                        found = False
                        for cara in self.faces_db:
                            old_embedding = cara["embedding"]
                            distance = medition.cosine_distance(old_embedding, embedding)
                            if distance < 0.4:
                                text = f"{cara['name']}, {analysis[0]['dominant_emotion']}"
                            found = True
                            break
                        if not found:
                            text = "Rostro no reconocido"

                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                                    0.9, (255, 255, 255), 2)
                    except Exception as e:
                        cv2.putText(frame, "No se detectaron rostros", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 100, 1000), 2)

                cv2.imshow(window_name, frame)
                if cv2.waitKey(1) & 0xFF == 27:
                    print(f"🛑 Cerrando {window_name}")
                    break
                time.sleep(self.frame_delay)
        except Exception as e:
            print(f"Ocurrio un error, por favor revisar logs, {e}")
            time.sleep(1)
        finally:
            cap.release()
            cv2.destroyWindow(window_name)