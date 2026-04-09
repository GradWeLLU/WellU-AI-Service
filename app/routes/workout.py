from fastapi import APIRouter
from app.schemas.workout_request import WorkoutRequest
from app.services.workout_service import generate_workout

router = APIRouter()


@router.post("/generate-workout")
async def create_workout(request: WorkoutRequest):
    print("Received:", request.dict())

    workout_plan = generate_workout(request)

    return {
        "goal": request.goal,
        "days": request.days,
        "workout_plan": workout_plan
    }