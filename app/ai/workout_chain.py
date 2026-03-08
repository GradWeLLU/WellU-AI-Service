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
- reps MUST always be a range like "8-10"
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