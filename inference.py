import subprocess, sys
subprocess.check_call([
    sys.executable, "-m", "pip", "install",
    "requests>=2.28.0", "openai>=1.0.0", "python-dotenv>=1.0.0",
    "--quiet"
])

import os
import requests
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME   = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
HF_TOKEN     = os.getenv("HF_TOKEN", "")
ENV_URL      = os.getenv("ENV_URL", "http://localhost:8000")
BENCHMARK    = "gst-audit-env"

client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

TASKS = ["gstr_mismatch", "itc_eligibility", "fraud_detection"]

SYSTEM_PROMPT = """You are an expert Indian GST compliance auditor with 15 years of experience.
You know all GST rules including Section 17(5) blocked credits, GSTR-1/3B reconciliation,
ITC eligibility, fake invoice detection, and enforcement under CGST Act 2017.
Always give specific rupee amounts, section numbers, and clear recommendations."""


def run_task(task_id: str):
    try:
        obs_resp = requests.post(
            f"{ENV_URL}/reset",
            params={"task_id": task_id},
            timeout=30
        )
        obs_resp.raise_for_status()
        obs = obs_resp.json()
    except requests.exceptions.ConnectionError as e:
        print(f"[ERROR] Could not connect to ENV server: {e}", flush=True)
        print(f"[END] success=false steps=0 rewards=0.00", flush=True)
        print("", flush=True)
        return 0.0
    except Exception as e:
        print(f"[ERROR] Reset failed: {e}", flush=True)
        print(f"[END] success=false steps=0 rewards=0.00", flush=True)
        print("", flush=True)
        return 0.0

    case_text    = obs.get("data", {}).get("case", "")
    question     = obs.get("data", {}).get("question", "")
    instructions = obs.get("instructions", "")

    prompt = f"""{instructions}

CASE:
{case_text}

QUESTION: {question}

Provide detailed analysis with specific rupee amounts, section references, and recommendations."""

    print(f"[START] task={task_id} env={BENCHMARK} model={MODEL_NAME}", flush=True)

    step_num   = 0
    rewards    = []
    last_error = "null"
    success    = False

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": prompt}
            ],
            max_tokens=500,
            temperature=0.1
        )
        action_text = response.choices[0].message.content.strip()
        action_log  = action_text[:80].replace("\n", " ").replace("\r", "")
        print(f"FULL ANSWER: {action_text[:500]}", flush=True)

        step_resp = requests.post(
            f"{ENV_URL}/step",
            json={"content": action_text},
            timeout=30
        )
        step_resp.raise_for_status()
        result = step_resp.json()

        step_num = 1
        reward   = round(result["reward"], 2)
        done     = result["done"]
        rewards.append(reward)
        success  = reward >= 0.5

        print(
            f"[STEP] step={step_num} action={action_log!r} "
            f"reward={reward:.2f} done={str(done).lower()} error={last_error}",
            flush=True
        )

    except requests.exceptions.ConnectionError as e:
        last_error = f"ConnectionError: {str(e)[:80]}"
        rewards.append(0.00)
        print(f"[STEP] step=1 action=null reward=0.00 done=true error={last_error}", flush=True)
    except Exception as e:
        last_error = str(e)[:100]
        rewards.append(0.00)
        print(f"[STEP] step=1 action=null reward=0.00 done=true error={last_error}", flush=True)

    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(f"[END] success={str(success).lower()} steps={step_num} rewards={rewards_str}", flush=True)
    print("", flush=True)

    return sum(rewards)


total = 0.0
for task in TASKS:
    total += run_task(task)

print(f"TOTAL_SCORE={total:.2f}", flush=True)
