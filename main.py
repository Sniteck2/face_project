import cv2
from deepface import DeepFace
from services import preload_recognition, load_recognition
from utils import medition
from camera.camera_factory import get_camera
from dotenv import load_dotenv
load_dotenv()

images_folder = 'images'

preload_recognition.analyze_image()

caras_conocidas = load_recognition.face_recognition()

camera = get_camera()
cap = camera.get_capture()

if not cap.isOpened():
    print("❌ No se pudo abrir la cámara")
    exit()

face_casacade = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')

print("Iniciando cámara")
while True:
    ret, frame = cap.read()
    if not ret:
        print("X No se pudo acceder a la cámara")
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

    cv2.imshow("Reconocimiento facial", frame)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()