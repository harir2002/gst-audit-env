import subprocess, sys

subprocess.check_call([
    sys.executable, "-m", "pip", "install",
    "requests>=2.28.0", "openai>=1.0.0", "python-dotenv>=1.0.0",
    "openenv-core>=0.2.0",
    "--quiet"
])

import os
from openai import OpenAI

API_BASE_URL = os.environ["API_BASE_URL"]
API_KEY = os.environ["API_KEY"]
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
ENV_URL = os.getenv("ENV_URL", "http://localhost:8000")
BENCHMARK = "gst-audit-env"

os.environ["OPENAI_API_KEY"] = API_KEY
client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)

TASKS = ["gstr_mismatch", "itc_eligibility", "fraud_detection"]

SYSTEM_PROMPT = """You are an expert Indian GST compliance auditor with 15 years of experience.
You know all GST rules including Section 17(5) blocked credits, GSTR-1/3B reconciliation,
ITC eligibility, fake invoice detection, and enforcement under CGST Act 2017.
Always give specific rupee amounts, section numbers, and clear recommendations."""

def call_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.1
    )
    return (response.choices[0].message.content or "").strip()

def run_task(task_id: str) -> float:
    print(f"[START] task={task_id} env={BENCHMARK} model={MODEL_NAME}", flush=True)

    rewards = []
    step_num = 1
    success = False

    try:
        action_text = call_llm(
            f"Task: {task_id}\n\nAnalyze this GST audit task and provide detailed findings with rupee amounts and section references."
        )
    except Exception as e:
        print(f"[STEP] step=1 action=null reward=0.00 done=true error={str(e)[:100]}", flush=True)
        print(f"[END] success=false steps=1 score=0.00 rewards=0.00", flush=True)
        print("", flush=True)
        return 0.0

    reward = 0.0
    done = True
    error = "null"

    try:
        import requests
        obs_resp = requests.post(f"{ENV_URL}/reset", params={"task_id": task_id}, timeout=15)
        obs = obs_resp.json()

        case_text = obs.get("data", {}).get("case", "")
        question = obs.get("data", {}).get("question", "")
        instructions = obs.get("instructions", "")

        if case_text or question:
            full_prompt = f"""{instructions}

CASE:
{case_text}

QUESTION: {question}

Provide detailed analysis with specific rupee amounts, section references, and recommendations."""
            action_text = call_llm(full_prompt)

        step_resp = requests.post(f"{ENV_URL}/step", json={"content": action_text}, timeout=15)
        result = step_resp.json()

        reward = round(result.get("reward", 0.0), 2)
        done = result.get("done", True)
        success = reward >= 0.5

    except Exception as e:
        error = str(e)[:100]

    rewards.append(reward)
    action_log = action_text[:80].replace("\n", " ").replace("\r", "")
    print(f"[STEP] step=1 action={action_log!r} reward={reward:.2f} done={str(done).lower()} error={error}", flush=True)

    score = sum(rewards)
    print(f"[END] success={str(success).lower()} steps={step_num} score={score:.2f} rewards={','.join(f'{r:.2f}' for r in rewards)}", flush=True)
    print("", flush=True)
    return score

total = 0.0
for task in TASKS:
    total += run_task(task)

print(f"TOTAL_SCORE={total:.2f}", flush=True)
