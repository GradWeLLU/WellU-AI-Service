from fastapi import FastAPI
from app.routes import workout

app = FastAPI()

app.include_router(workout.router)


@app.get("/")
def root():
    return {"message": "Workout Generator API running"}