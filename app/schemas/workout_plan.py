from pydantic import BaseModel
from typing import List

class Exercise(BaseModel):
    name: str
    sets: int
    reps: str

class WorkoutDay(BaseModel):
    day: str
    focus: str
    exercises: List[Exercise]

class WorkoutPlan(BaseModel):
    weekly_split: str
    days: List[WorkoutDay]