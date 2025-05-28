from fastapi import FastAPI
from src.api.routes import router

app = FastAPI()
app.include_router(router)

@app.get("/status")
def status():
    return {"status": "ok"}