from pydantic import BaseModel
from typing import List


class Meal(BaseModel):
    name: str
    calories: int
    protein: int
    carbs: int
    fats: int
    ingredients: List[str]


class MealDay(BaseModel):
    day: str
    meals: List[Meal]


class NutritionPlan(BaseModel):
    goal: str
    daily_calories: int
    days: List[MealDay]