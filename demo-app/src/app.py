import os
import socket
from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="demo-app")

START_TIME = datetime.now(timezone.utc)


@app.get("/")
def root():
    return {
        "message": "Hello from demo-app",
        "hostname": socket.gethostname(),
        "version": os.getenv("APP_VERSION", "dev"),
    }


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/readyz")
def readyz():
    return {"status": "ready"}


@app.get("/info")
def info():
    return JSONResponse(
        {
            "hostname": socket.gethostname(),
            "started_at": START_TIME.isoformat(),
            "env": {k: v for k, v in os.environ.items() if k.startswith("APP_")},
        }
    )
