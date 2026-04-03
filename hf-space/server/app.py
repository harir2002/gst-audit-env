from fastapi import FastAPI
from models import Action, StepResult, Observation, State
from server.environment import GSTAuditEnv

app = FastAPI(
    title="GST Compliance Audit Environment",
    description="OpenEnv RL environment for Indian GST audit, ITC verification and fraud detection",
    version="1.0.0"
)

env = GSTAuditEnv()

@app.get("/")
def root():
    return {"status": "ok", "name": "gst-audit-env", "version": "1.0.0"}

@app.post("/reset", response_model=Observation)
def reset(task_id: str = "gstr_mismatch"):
    return env.reset(task_id=task_id)

@app.post("/step", response_model=StepResult)
def step(action: Action):
    return env.step(action)

@app.get("/state", response_model=State)
def state():
    return env.get_state()

@app.get("/tasks")
def list_tasks():
    return {
        "tasks": [
            {
                "id": "gstr_mismatch",
                "difficulty": "easy",
                "description": "Detect GSTR-1 vs GSTR-3B mismatch and calculate tax difference",
                "max_score": 1.0
            },
            {
                "id": "itc_eligibility",
                "difficulty": "medium",
                "description": "Calculate eligible ITC after applying Section 17(5) blocked credits",
                "max_score": 1.0
            },
            {
                "id": "fraud_detection",
                "difficulty": "hard",
                "description": "Detect fake invoice fraud, calculate fake ITC, recommend enforcement",
                "max_score": 1.0
            }
        ]
    }