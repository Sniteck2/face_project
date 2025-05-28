import os

def get_camera_config():
    configs = []
    index = 1
    while True:
        cam_type = os.getenv(f"CAMERA_{index}_TYPE")
        if not cam_type:
            break

        config = {"type": cam_type.upper()}
        if config["type"] == "IP":
            config["url"] = os.getenv(f"CAMERA_{index}_URL")
            config["name"] = os.getenv(f"CAMERA_{index}_NAME")
        elif config["type"] == "USB":
            config["index"] = int(os.getenv(f"CAMERA_{index}_INDEX", 0))
            config["name"] = os.getenv(f"CAMERA_{index}_NAME")
        configs.append(config)
        index += 1
    return configs