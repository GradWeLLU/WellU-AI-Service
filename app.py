from fastapi import FastAPI
from pydantic import BaseModel
from workout_generator import generate_workout

app = FastAPI()

class WorkoutRequest(BaseModel):
    goal: str
    days: int

@app.get("/")
def root():
    return {"message": "Workout Generator API is running"}

@app.post("/generate-workout")
def create_workout(request: WorkoutRequest):
    workout_plan = generate_workout(request.goal, request.days)
    return {
        "goal": request.goal,
        "days": request.days,
        "workout_plan": workout_plan
    }