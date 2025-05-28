@echo off
echo 🚀 Iniciando el microservicio FastAPI...
uvicorn src.app.main:app --reload --host 127.0.0.1 --port 8000
pause