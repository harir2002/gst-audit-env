import uuid
import random
from models import Action, Observation, StepResult, State
from data.gst_cases import TASK1_CASES, TASK2_CASES, TASK3_CASES


class GSTAuditEnv:
    def __init__(self):
        self._episode_id = None
        self._current_task = None
        self._steps = 0
        self._total_reward = 0.0
        self._current_case = None

    def reset(self, task_id: str = "gstr_mismatch") -> Observation:
        self._episode_id = str(uuid.uuid4())
        self._steps = 0
        self._total_reward = 0.0
        self._current_task = task_id

        if task_id == "gstr_mismatch":
            case = random.choice(TASK1_CASES)
            self._current_case = case
            return Observation(
                task_id=task_id,
                instructions="You are a GST compliance auditor. Analyze the following case and answer precisely with rupee amounts and legal sections.",
                data={"case": case["description"], "question": case["question"]},
                step=0
            )
        elif task_id == "itc_eligibility":
            case = random.choice(TASK2_CASES)
            self._current_case = case
            return Observation(
                task_id=task_id,
                instructions="You are a GST ITC specialist. Calculate eligible Input Tax Credit under Section 17(5) blocked credits rules of CGST Act 2017.",
                data={"case": case["description"], "question": case["question"]},
                step=0
            )
        elif task_id == "fraud_detection":
            case = random.choice(TASK3_CASES)
            self._current_case = case
            return Observation(
                task_id=task_id,
                instructions="You are a GST fraud investigator. Analyze transaction patterns, identify fraud type, calculate revenue loss, and recommend enforcement.",
                data={"case": case["description"], "question": case["question"]},
                step=0
            )
        else:
            return Observation(task_id=task_id, instructions="Unknown task.", data={}, step=0)

    def _normalize(self, text: str) -> str:
        return text.lower().replace(",", "").replace("₹", "").replace(" ", "").replace("rs.", "").replace("rs", "").replace("inr", "")

    def _amount_in_answer(self, answer: str, amount: int) -> bool:
        """Check if a rupee amount appears in the answer in any common format"""
        if amount == 0:
            return False
        ans_clean = self._normalize(answer)
        checks = [
            str(amount),                          # 127500
            str(round(amount / 100000, 2)),       # 1.27
            str(round(amount / 100000, 1)),       # 1.3
            str(round(amount / 1000, 0))[:-2],    # 127
        ]
        return any(c in ans_clean for c in checks)

    def step(self, action: Action) -> StepResult:
        if self._current_task is None:
            return StepResult(
                observation=Observation(
                    task_id="error", instructions="",
                    data={}, feedback="Please call /reset first before /step", step=0
                ),
                reward=0.0, done=True, info={}
            )

        self._steps += 1
        answer = action.content.lower().strip()
        reward = 0.0
        feedback_parts = []
        correct = self._current_case.get("correct_answer", {})

        # ══════════════════════════════════════════
        # TASK 1: GSTR Mismatch
        # ══════════════════════════════════════════
        if self._current_task == "gstr_mismatch":
            is_mismatch = correct.get("mismatch", True)
            gst_diff = correct.get("gst_difference", 0)

            # 1. Mismatch detection (35 pts)
            mismatch_words = ["mismatch", "difference", "discrepancy", "short", "underpaid", "shortfall", "gap", "wrong"]
            no_mismatch_words = ["no mismatch", "match", "correct", "reconciled", "same", "equal", "no difference", "nil difference"]

            if is_mismatch:
                if any(x in answer for x in mismatch_words):
                    reward += 0.35
                    feedback_parts.append("✅ Mismatch correctly identified (+0.35)")
                else:
                    feedback_parts.append("❌ Should identify a mismatch exists")
            else:
                if any(x in answer for x in no_mismatch_words):
                    reward += 0.35
                    feedback_parts.append("✅ No mismatch correctly identified (+0.35)")
                else:
                    feedback_parts.append("❌ Should identify there is NO mismatch")

            # 2. Correct amount (40 pts)
            if gst_diff == 0:
                if any(x in answer for x in ["nil", "zero", "no difference", "0", "nothing"]):
                    reward += 0.40
                    feedback_parts.append("✅ Zero difference correctly identified (+0.40)")
                else:
                    feedback_parts.append("❌ Difference is zero/nil")
            else:
                if self._amount_in_answer(answer, abs(gst_diff)):
                    reward += 0.40
                    feedback_parts.append(f"✅ Correct amount ₹{abs(gst_diff):,} identified (+0.40)")
                else:
                    feedback_parts.append(f"❌ Amount wrong. Expected ₹{abs(gst_diff):,}")

            # 3. Legal section (25 pts)
            legal_words = ["section 73", "section 74", "section 75", "section 76",
                           "section 50", "section 47", "scn", "show cause", "notice",
                           "recovery", "demand", "penalty", "interest", "cgst act"]
            if any(x in answer for x in legal_words):
                reward += 0.25
                feedback_parts.append("✅ Legal section/action referenced (+0.25)")
            else:
                feedback_parts.append("❌ Reference CGST Act sections (73/74/75/50)")

        # ══════════════════════════════════════════
        # TASK 2: ITC Eligibility
        # ══════════════════════════════════════════
        elif self._current_task == "itc_eligibility":
            eligible_itc = correct.get("eligible_itc", 0)
            ineligible_itc = correct.get("ineligible_itc", 0)
            blocked_items = [x.lower() for x in correct.get("blocked_items", [])]

            # 1. Correct eligible ITC amount (30 pts)
            if eligible_itc > 0 and self._amount_in_answer(answer, eligible_itc):
                reward += 0.30
                feedback_parts.append(f"✅ Correct eligible ITC ₹{eligible_itc:,} (+0.30)")
            elif any(x in answer for x in ["eligible itc", "itc eligible", "can claim", "allowable"]):
                reward += 0.10
                feedback_parts.append("⚠️ ITC concept mentioned but amount not precise (+0.10)")
            else:
                feedback_parts.append(f"❌ Eligible ITC should be ₹{eligible_itc:,}")

            # 2. Blocked items identified (25 pts)
            # Extract key nouns from blocked_items list
            block_keywords = []
            for item in blocked_items:
                words = item.replace("section 17(5)", "").replace("blocked", "").strip().split()
                block_keywords.extend([w for w in words if len(w) > 3])

            block_keywords += ["17(5)", "section 17", "blocked credit", "ineligible",
                               "cannot claim", "not eligible", "disallowed", "restricted", "blocked"]

            if any(x in answer for x in block_keywords):
                reward += 0.25
                feedback_parts.append("✅ Blocked/ineligible items correctly identified (+0.25)")
            else:
                feedback_parts.append("❌ Must identify blocked credits under Section 17(5)")

            # 3. Correct ineligible amount (20 pts)
            if ineligible_itc > 0 and self._amount_in_answer(answer, ineligible_itc):
                reward += 0.20
                feedback_parts.append(f"✅ Ineligible ITC ₹{ineligible_itc:,} correctly calculated (+0.20)")
            elif any(x in answer for x in ["reverse", "reversal", "excess", "overclaim", "should not claim"]):
                reward += 0.10
                feedback_parts.append("⚠️ Reversal concept mentioned (+0.10)")
            else:
                feedback_parts.append(f"❌ Ineligible ITC to reverse = ₹{ineligible_itc:,}")

            # 4. Legal basis (25 pts)
            if any(x in answer for x in ["17(5)", "section 17", "cgst", "blocked under",
                                          "not eligible under", "disallowed under", "rule 42"]):
                reward += 0.25
                feedback_parts.append("✅ Legal basis Section 17(5) referenced (+0.25)")
            else:
                feedback_parts.append("❌ Must cite Section 17(5) CGST Act")

        # ══════════════════════════════════════════
        # TASK 3: Fraud Detection
        # ══════════════════════════════════════════
        elif self._current_task == "fraud_detection":
            fraud_type = correct.get("fraud_type", "").lower()
            indicators = [x.lower() for x in correct.get("indicators", correct.get("key_indicators", []))]
            actions = [x.lower() for x in correct.get("actions", correct.get("enforcement_actions", []))]

            # 1. Fraud type (25 pts)
            fraud_keywords = fraud_type.split() + [
                "fake", "fraud", "missing trader", "shell", "bogus",
                "circular", "round trip", "phantom", "double benefit",
                "export fraud", "deemed export", "inflated", "false",
                "forged", "non-existent", "fictitious", "fraudulent"
            ]
            if any(x in answer for x in fraud_keywords):
                reward += 0.25
                feedback_parts.append(f"✅ Fraud type identified (+0.25)")
            else:
                feedback_parts.append(f"❌ Should identify: {correct.get('fraud_type', 'fraud type')}")

            # 2. Indicators found (25 pts — 5 pts each, max 5)
            indicator_score = 0
            found_count = 0
            for indicator in indicators[:5]:
                # Check if key words from indicator appear in answer
                key_words = [w for w in indicator.split() if len(w) > 4]
                if any(w in answer for w in key_words):
                    indicator_score += 0.05
                    found_count += 1
            # Also check generic fraud indicators
            generic_flags = ["zero inward", "no purchase", "residential", "no employee",
                            "no warehouse", "bank", "rapid growth", "disappeared",
                            "no payment", "circular", "double", "collusion", "fictitious"]
            generic_found = sum(1 for x in generic_flags if x in answer)
            bonus = min(generic_found * 0.02, 0.10)
            indicator_score = min(indicator_score + bonus, 0.25)
            reward += indicator_score
            feedback_parts.append(f"✅ Fraud indicators identified (+{indicator_score:.2f})")

            # 3. Revenue/loss amount (20 pts)
            if any(x in answer for x in ["crore", "lakh", "₹", "revenue loss", "tax evaded",
                                          "fake itc", "fraudulent itc", "total loss",
                                          "double benefit", "excess refund", "amount"]):
                reward += 0.20
                feedback_parts.append("✅ Revenue loss/amount discussed (+0.20)")
            else:
                feedback_parts.append("❌ Calculate total revenue loss to government")

            # 4. Enforcement actions (30 pts)
            enforcement = 0
            action_checks = [
                (["cancel", "cancellation", "revoke", "deregister", "suspend gstin"], 0.08),
                (["rule 86a", "86a", "block itc", "deny itc", "reject refund",
                  "stop refund", "withhold refund", "itc block"], 0.08),
                (["section 132", "132", "fir", "arrest", "criminal",
                  "prosecution", "imprison", "penal"], 0.07),
                (["show cause", "scn", "demand notice", "recovery notice",
                  "notice", "investigation", "inquiry", "scrutiny", "audit"], 0.07),
            ]
            for keywords, pts in action_checks:
                if any(x in answer for x in keywords):
                    enforcement += pts
            reward += enforcement
            feedback_parts.append(f"✅ Enforcement actions score: +{enforcement:.2f}")

        # ══════════════════════════════════════════
        self._total_reward += reward

        return StepResult(
            observation=Observation(
                task_id=self._current_task or "unknown",
                instructions="",
                data={},
                feedback="\n".join(feedback_parts),
                step=self._steps
            ),
            reward=round(min(reward, 1.0), 3),
            done=True,
            info={"total_reward": self._total_reward}
        )

    def get_state(self) -> State:
        return State(
            episode_id=self._episode_id or "none",
            step_count=self._steps,
            current_task=self._current_task or "none",
            total_reward=self._total_reward
        )