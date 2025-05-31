from fastapi import APIRouter, Response, HTTPException
from starlette.responses import StreamingResponse
import cv2
import threading
import time

from src.core.camera_manager import camera_manager
from src.core.frame_buffer import get_last_frame

router = APIRouter()

# Referencia a los últimos frames capturados por cada cámara
last_frames = {}
lock = threading.Lock()

# Callback que los procesadores deben usar para actualizar el frame actual
def update_last_frame(camera_id, frame):
    with lock:
        last_frames[camera_id] = frame

# Generador MJPEG
def generate_stream(camera_id: str):
    while True:
        with lock:
            frame = get_last_frame(camera_id)
        if frame is not None:
            ret, jpeg = cv2.imencode('.jpg', frame)
            if not ret:
                continue
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
        time.sleep(0.05)  # ~20 fps

@router.get("/stream/{camera_id}")
def stream(camera_id: str):
    if camera_id not in [p.camera_id for p in camera_manager.processors]:
        raise HTTPException(status_code=404, detail="Cámara no encontrada")
    return StreamingResponse(generate_stream(camera_id), media_type="multipart/x-mixed-replace; boundary=frame")
