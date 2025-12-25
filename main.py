from fastapi import FastAPI
from core.config import init_clients

app = FastAPI()

@app.on_event("startup")
def startup():
    init_clients()

@app.get("/")
def health():
    return {"status": "ok"}

