from pydantic import BaseModel
from typing import Optional, List

class Action(BaseModel):
    content: str  # Agent's text response/decision

class Observation(BaseModel):
    task_id: str = ""
    instructions: str = ""
    data: dict = {}
    feedback: str = ""
    step: int = 0

class StepResult(BaseModel):
    observation: Observation
    reward: float
    done: bool
    info: dict = {}

class State(BaseModel):
    episode_id: str
    step_count: int
    current_task: str
    total_reward: float