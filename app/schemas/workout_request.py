from pydantic import BaseModel
from typing import Literal

class WorkoutRequest(BaseModel):
    goal: str | None = None
    days: int | None = None
    age: int | None = None
    weight: float | None = None
    height: float | None = None
    bmi: float | None = None
    session_duration: int | None = None
    preferred_difficulty_level: Literal["BEGINNER","INTERMEDIATE","ADVANCED"] | None = None
    preferred_equipment: list[str] | None = None
    experience_level: str | None = None
    injuries: list[str] | None = None