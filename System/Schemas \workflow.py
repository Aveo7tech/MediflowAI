from pydantic import BaseModel
from typing import List
from schemas.task import Task

class WorkflowPlan(BaseModel):
    goal: str
    steps: List[Task]
