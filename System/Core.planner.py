from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from schemas.workflow import WorkflowPlan
from config.settings import settings

class WorkflowPlanner:

    def __init__(self):
        self.llm = ChatOpenAI(
            model=settings.MODEL_NAME,
            temperature=settings.TEMPERATURE
        )

        self.prompt = ChatPromptTemplate.from_template("""
        You are MediFlow AI Planner.

        Break the clinical request into structured steps.
        For each step define:
        - action
        - tool_name
        - parameters (JSON)

        Return valid JSON matching this schema:
        {format_instructions}

        Request:
        {input}
        """)

    def create_plan(self, user_input: str) -> WorkflowPlan:
        response = self.llm.invoke(self.prompt.format(input=user_input))
        return WorkflowPlan.model_validate_json(response.content)
