from fastapi import FastAPI
from app.routes import workout
from app.routes import nutrition

app = FastAPI()

app.include_router(workout.router)
app.include_router(nutrition.router)

@app.get("/")
def root():
    return {"message": "Workout Generator API running"}