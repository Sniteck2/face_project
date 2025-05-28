
from pydantic import BaseModel
from typing import List

class CameraDTO(BaseModel):
    id: str
    name: str
    type: str
    source: str
    running: bool

class CameraListResponseDTO(BaseModel):
    running: bool
    cameras: List[CameraDTO]

class CameraStartResponseDTO(BaseModel):
    started_cameras: List[str]

class CameraStopResponseDTO(BaseModel):
    stopped_cameras: str