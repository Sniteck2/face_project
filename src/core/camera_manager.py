import threading
import os

from dotenv import load_dotenv
from src.camera.config import get_camera_config
from src.camera.camera_factory import create_camera_instance
from src.service.core import CameraProcessor

load_dotenv()

class CameraManager:
    def __init__(self):
        self.threads = []
        self.processors = []
        self.running = False

    def start_all(self):
        if self.running:
            return [p.name for p in self.processors]

        camera_configs = get_camera_config()
        fps = int(os.getenv("CAMERA_FPS", 15))
        for i, config in enumerate(camera_configs):
            camera = create_camera_instance(config)
            name = config.get("name", f"Cam_{i+1}")
            processor = CameraProcessor(camera_id=f"Cam_{i+1}", camera=camera, name=name, fps=fps)
            thread = threading.Thread(target=processor.run, daemon=True)
            thread.start()
            self.threads.append(thread)
            self.processors.append(processor)

        self.running = True
        return [p.name for p in self.processors]

    def stop_all(self):
        for processor in self.processors:
            processor.stop = True
        self.threads = []
        self.processors = []
        self.running = False
        return "ok"

    def get_status(self):
        cameras_info = []
        for processor in self.processors:
            cameras_info.append({
                "id": processor.camera_id,
                "name": processor.name,
                "type": processor.camera.camera_type,
                "source": processor.camera.source,
                "running": not processor.stop
            })
        return {
            "cameras": cameras_info,
            "running": self.running,
        }

camera_manager = CameraManager()