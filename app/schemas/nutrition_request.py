from pydantic import BaseModel


class NutritionRequest(BaseModel):
    goal: str
    weight: str
    height: str
    age: int
    gender: str
    activity_level: str
    budget: str
    diet: str
    meals_per_day: int