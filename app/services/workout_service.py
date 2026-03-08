from app.ai.workout_chain import create_workout_chain
from app.schemas import workout_request


def generate_workout(request: workout_request):

    chain, parser = create_workout_chain()

    user_data = {
        "age": request.age,
        "goal": request.goal,
        "gym_days": request.days,
        "experience": request.experience_level,
        "gender": getattr(request, "gender", "Not specified"),
        "weight": request.weight,
        "height": request.height,
        "bmi": request.bmi,
        "duration": request.session_duration,
        "split": getattr(request, "split", "full-body"),
        "difficulty": request.preferred_difficulty_level,
        "equipment": request.preferred_equipment,
        "injuries": request.injuries,
        "format_instructions": parser.get_format_instructions()
    }
    result = chain.invoke(user_data)

    return result.dict()