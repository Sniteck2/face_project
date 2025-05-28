
from fastapi import APIRouter, HTTPException, status

from src.core.camera_manager import camera_manager
from src.models.dto.camera_dtos import CameraDTO, CameraStartResponseDTO, CameraStopResponseDTO, CameraListResponseDTO

router = APIRouter()

@router.post("/cameras/start", response_model=CameraStartResponseDTO, status_code=status.HTTP_200_OK)
def start_cameras():
    try:
        started = camera_manager.start_all()
        if not started:
            raise HTTPException(status_code=400, detail="No se pudieron iniciar las cámaras")
        return CameraStartResponseDTO(started_cameras=started)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/cameras/stop", response_model=CameraStopResponseDTO, status_code=status.HTTP_200_OK)
def stop_cameras():
    try:
        if not hasattr(camera_manager, "stop_all"):
            raise HTTPException(status_code=500, detail="Función de stop no implementada correctamente")
        stopped = camera_manager.stop_all()
        return CameraStopResponseDTO(stopped_cameras=stopped)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/cameras", response_model=CameraListResponseDTO, status_code=status.HTTP_200_OK)
def list_cameras():
    try:
        status_info = camera_manager.get_status()
        cameras_info = status_info.get("cameras")
        if cameras_info is None:
            raise HTTPException(status_code=404, detail="No se encontró información de cámaras")

        detailed_info = [
            CameraDTO(
                id=cam.get("id", "unknown"),
                name=cam.get("name", "N/A"),
                type=cam.get("type", "unknown"),
                source=cam.get("source", "unknown"),
                running=cam.get("running", False),
            )
            for cam in cameras_info
        ]
        return CameraListResponseDTO(running=status_info.get("running", False), cameras=detailed_info)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))