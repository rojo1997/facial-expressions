from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from routers import (
    gateway
)

from events.event_handlers import (
    start_app_handler,
    stop_app_handler
)

app = FastAPI(
    title = 'Facial Expressions'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"],
    allow_credentials = True
)

app.include_router(gateway.router)

app.add_event_handler("startup", start_app_handler(app))
app.add_event_handler("shutdown", stop_app_handler(app))

if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host = "0.0.0.0", 
        port = 5030, 
        log_level = "debug"
    )