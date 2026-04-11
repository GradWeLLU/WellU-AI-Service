from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser

from app.schemas.nutrition_plan import NutritionPlan
from app.prompts.nutrition_prompt import get_nutrition_prompt


def create_nutrition_chain():
    parser = PydanticOutputParser(pydantic_object=NutritionPlan)

    prompt = get_nutrition_prompt()

    chat = ChatOpenAI(
        model_name="gpt-5-mini",
        temperature=0.3
    )

    chain = prompt | chat | parser

    return chain, parser