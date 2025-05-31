from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.api.routes import router
from src.api.websocket_events import router as ws_router
from src.utils.event_loop import init_event_loop
from src.api.stream_routes import router as stream_router

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
app.include_router(stream_router)

@app.get("/status")
def status():
    return {"status": "ok"}