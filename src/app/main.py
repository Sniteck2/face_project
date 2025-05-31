from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.api.routes import router
from src.api.websocket_events import router as ws_router
from src.utils.event_loop import init_event_loop

app = FastAPI()
init_event_loop()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)
app.include_router(ws_router)

@app.get("/status")
def status():
    return {"status": "ok"}