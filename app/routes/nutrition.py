from fastapi import APIRouter
from app.schemas.nutrition_request import NutritionRequest
from app.services.nutrition_service import generate_nutrition

router = APIRouter()


@router.post("/generate-nutrition")
async def create_nutrition(request: NutritionRequest):
    print("Received:", request.dict())

    nutrition_plan = generate_nutrition(request)

    return {
        "goal": request.goal,
        "meals_per_day": request.meals_per_day,
        "nutrition_plan": nutrition_plan
    }