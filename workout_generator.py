import os
import openai
from typing import List
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser

# -------------------------------
# Models
# -------------------------------
load_dotenv()

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
# -------------------------------
# Main function used by API
# LLM / prompt / parser are created lazily to avoid heavy work at import
# -------------------------------

def generate_workout(user_goal: str, gym_days: int) -> dict:
    """
    Minimal interface for FastAPI.

    LLM and prompt objects are created on demand to keep module import cheap.
    """
    # Ensure API key is set in case env changed after import
    openai.api_key = os.getenv('OPENAI_API_KEY')

    # Create LLM client and chat model
    client = openai.OpenAI()
    chat = ChatOpenAI(model_name='gpt-5-mini', temperature=0.3)

    # Create parser and prompt
    parser = PydanticOutputParser(pydantic_object=WorkoutPlan)

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

    # Hardcoded example user info; can make dynamic later
    user_data = {
        "age": 22,
        "gender": "male",
        "experience": "1 year consistent training",
        "goal": user_goal,
        "gym_days": gym_days,
        "split": "push pull legs",
        "duration": "60 mins",
        "format_instructions": parser.get_format_instructions()
    }

    result = chain.invoke(user_data)
    return result.dict()