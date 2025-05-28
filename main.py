import threading
from dotenv import load_dotenv
from src.service.core import CameraProcessor
from src.camera.config import get_camera_config
from src.camera.camera_factory import create_camera_instance

if __name__ == "__main__":
    load_dotenv()
    threads = []

    for i, config in enumerate(get_camera_config()):
        processor = CameraProcessor(
            camera_id=f"Cam_{i+1}",
            camera=create_camera_instance(config),
            name=config.get("name", f"Cam_{i+1}"),
        )
        t = threading.Thread(target=processor.run, daemon=False)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()