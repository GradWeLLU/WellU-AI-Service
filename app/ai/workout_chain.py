import openai
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from app.schemas.workout_plan import WorkoutPlan
from app.core.config import OPENAI_API_KEY


def create_workout_chain():

    openai.api_key = OPENAI_API_KEY

    chat = ChatOpenAI(
        model_name="gpt-5-mini",
        temperature=0.3
    )

    parser = PydanticOutputParser(
        pydantic_object=WorkoutPlan
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", """
You are a professional strength coach.

Create a structured gym workout plan based on the user's details.

STRICT RULES:
- Each workout day MUST contain at least 4 exercises
- Every exercise MUST include:
    name
    sets
    reps
    exercise_type
    muscle_groups
    Difficulty
    video_url
    rest_time
- reps MUST always be a range like "8-10"
- exercise_type must belong to the following ["COMPOUND", "ISOLATION", "ISOMETRIC", "BODYWEIGHT"]
- muscle_groups must be a list and must belong to the following ["CHEST", "BACK", "ARMS", "CORE", "LEGS", "SHOULDERS"]
- Difficulty must belong to the following ["EASY", "INTERMEDIATE", "HARD"]
- video_url must be a short video of that exercise. Make sure the video is available
- plan_type must belong to the following ["HYPERTROPHY", "STRENGTH", "WEIGHT_LOSS", "ENDURANCE", "GENERAL_FITNESS", "REHABILITATION"]
- rest_time must be a float
- NEVER output empty exercises
- NEVER omit fields

{format_instructions}
"""),
        ("human", """
Create a workout plan with these details:

Age: {age}
Gender: {gender}
Experience: {experience}
Goal: {goal}
Gym days per week: {gym_days}
Workout preference: {split}
Session duration: {duration}
""")
    ])

    return prompt | chat | parser, parser