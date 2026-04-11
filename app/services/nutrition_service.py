from app.ai.nutrition_chain import create_nutrition_chain

chain, parser = create_nutrition_chain()


def generate_nutrition(request):
    result = chain.invoke({
        "goal": request.goal,
        "weight": request.weight,
        "height": request.height,
        "age": request.age,
        "gender": request.gender,
        "activity_level": request.activity_level,
        "budget": request.budget,
        "diet": request.diet,
        "meals_per_day": request.meals_per_day,
        "format_instructions": parser.get_format_instructions()
    })

    return result