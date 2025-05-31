import threading

_last_frames = {}
_lock = threading.Lock()

def update_last_frame(camera_id, frame):
    with _lock:
        _last_frames[camera_id] = frame

def get_last_frame(camera_id):
    with _lock:
        return _last_frames.get(camera_id)