# 🛡️ Face Project - MVP v1

Sistema de seguridad familiar con reconocimiento facial en tiempo real.

---

## ✅ Características del MVP

### 🔍 Procesamiento facial
- Soporte para cámaras USB e IP
- Reconocimiento facial con DeepFace + OpenCV
- Cuadro de detección + nombre en ventana local
- Whitelist de personas conocidas (por imágenes)

### 📡 Backend (FastAPI)
- Microservicio FastAPI estructurado por módulos
- Endpoints REST:
   - `POST /cameras/start`: Iniciar cámaras
   - `GET /cameras`: Obtener estado y fuentes
   - `GET /stream/{camera_id}`: Stream MJPEG en tiempo real
- WebSocket:
   - `ws://localhost:8000/ws/events`: Recibir eventos de reconocimiento facial

### 🖥️ Frontend (HTML + JS)
- Botón para iniciar cámaras
- Visualización en vivo de cada stream
- Recibir eventos reconocidos/no reconocidos por WebSocket

---

## 📁 Estructura del Proyecto

```
face_project/
├── src/
│   ├── app/                 # FastAPI app
│   ├── api/                 # Routers REST + WebSocket + Stream
│   ├── camera/              # Clases de cámaras (USB/IP)
│   ├── core/                # Cámara manager y frame buffer
│   ├── service/             # Procesador facial
│   ├── models/              # DTOs
│   └── utils/               # Loop, métricas, etc
├── images/                  # Whitelist de rostros
├── models/                  # Haarcascade XML
├── logs/                    # Logs locales
├── frontend/                # index.html, style.css, app.js
├── main.py                  # Ejecución local (por hilo)
├── .env                     # Configuración cámaras
├── start.bat / start.sh     # Iniciar microservicio
├── requirements.txt         # Dependencias mínimas
└── README.md                # Documentación
```

---

## 🚀 Cómo levantar el proyecto (MVP v1)

### 1. Clona el repositorio
```bash
git clone https://github.com/Sniteck2/face_project.git
cd face_project
```

### 2. Crea entorno virtual e instala dependencias
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configura el archivo `.env`
Ejemplo:
```
CAMERA_1_TYPE=USB
CAMERA_1_SOURCE=0
CAMERA_1_NAME=camara_usb_pc

CAMERA_2_TYPE=IP
CAMERA_2_SOURCE=http://192.168.1.50:8080/video
CAMERA_2_NAME=camara_ip_sala
```

### 4. Inicia el microservicio
```bash
start.bat     # o ./start.sh en Linux/Mac
```

## 📦 Requisitos
- Python 3.11
- Windows 10 u 11 (ó Linux/macOS)
- Cámara USB y/o IP accesible
- GPU opcional (mejora el rendimiento con DeepFace)

---

## ✅ Estado: MVP funcional v1

✔️ End-to-end probado con múltiples cámaras, detección facial, eventos en tiempo real, y streaming por web.
