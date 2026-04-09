from pydantic import BaseModel
from typing import List

class Exercise(BaseModel):
    name: str
    sets: int
    reps: str
    exercise_type: str
    muscle_group: List[str]
    video_url: str
    difficulty: str
    rest_time: float

class WorkoutDay(BaseModel):
    day: str
    focus: str
    exercises: List[Exercise]

class WorkoutPlan(BaseModel):
    weekly_split: str
    plan_type: str
    difficulty: str
    days: List[WorkoutDay]