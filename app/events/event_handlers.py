from typing import Callable
from fastapi import FastAPI

from core.facialExpression import FacialExpression

def _startup_model(app: FastAPI) -> None:
    app.state.FE = FacialExpression()

def start_app_handler(app: FastAPI) -> Callable:
    def startup() -> None:
        _startup_model(app)
    return startup

def _shutdown_model(app: FastAPI) -> None:
    app.state.FE = None

def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        _shutdown_model(app)
    return shutdown