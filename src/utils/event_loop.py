import asyncio

loop = None

def init_event_loop():
    global loop
    loop = asyncio.get_event_loop()

def get_event_loop():
    return loop