from fastapi import FastAPI
from lessons.routes import router as lesson_router

app = FastAPI(title="Job Funnel Agent")

app.include_router(lesson_router)

@app.get("/")
def health():
    return {"status": "ok"}
