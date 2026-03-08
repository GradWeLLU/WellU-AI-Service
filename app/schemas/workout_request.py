from pydantic import BaseModel
from typing import Literal

class WorkoutRequest(BaseModel):
    goal: str
    days: int
    age: int
    weight: float
    height: int
    bmi: float
    session_duration: int | None = None
    preferred_difficulty_level: Literal["BEGINNER","INTERMEDIATE","ADVANCED"] | None = None
    preferred_equipment: list[str] | None = None
    experience_level: str
    injuries: list[str] | None = None