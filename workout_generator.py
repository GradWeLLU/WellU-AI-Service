import os
from typing import List
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser


# -------------------------------
# Models
# -------------------------------

class Exercise(BaseModel):
    name: str
    sets: int
    reps: str


class WorkoutDay(BaseModel):
    day: str
    focus: str
    exercises: List[Exercise]


class WorkoutPlan(BaseModel):
    weekly_split: str
    days: List[WorkoutDay]


# -------------------------------
# LLM Setup
# -------------------------------

chat = ChatOpenAI(
    model_name="gpt-5-mini",
    temperature=0.3,
)

parser = PydanticOutputParser(pydantic_object=WorkoutPlan)


# -------------------------------
# Prompt
# -------------------------------

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
- If unsure, repeat a valid exercise

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


chain = prompt | chat | parser


# -------------------------------
# Main function used by API
# -------------------------------

def generate_workout_plan(user_data: dict) -> dict:
    """
    Generate workout plan for a user.

    This function will be called by the FastAPI endpoint.
    """

    result = chain.invoke({
        "age": user_data.get("age"),
        "gender": user_data.get("gender"),
        "experience": user_data.get("experience"),
        "goal": user_data.get("goal"),
        "gym_days": user_data.get("gym_days"),
        "split": user_data.get("split"),
        "duration": user_data.get("duration"),
        "format_instructions": parser.get_format_instructions()
    })

    return result.dict()