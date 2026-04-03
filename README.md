---
title: GST Audit Environment
emoji: 📊
colorFrom: green
colorTo: blue
sdk: docker
pinned: true
license: mit
short_description: India's first GST Audit RL Environment for AI agent training
---

# GST Audit Environment

**India's first Reinforcement Learning environment for GST compliance auditing**

- **Project:** GST Audit Environment - India's first Reinforcement Learning environment for GST compliance auditing  
- **Framework:** OpenEnv (Meta x PyTorch Hackathon)  
- **Built by:** Hari R

## Overview

The GST Audit Environment is a domain-specific RL benchmark designed to train and evaluate AI agents on real-world Indian indirect tax compliance workflows. It simulates practical GST audit reasoning tasks that tax officers, consultants, and compliance teams face every day, from return mismatches to input tax credit checks and fraud pattern detection.

This matters at national scale: India has **1.4+ crore GST filers** and collects approximately **INR 18 lakh crore in annual GST revenue**. Even small improvements in audit quality, speed, and consistency can translate into significant public finance impact, reduced litigation, and stronger compliance behavior.

## Tasks

| Task ID | Difficulty | Description |
|---|---|---|
| `gstr_mismatch` | Easy | Detect mismatches between GSTR-1 and GSTR-3B filings and calculate tax differences accurately. |
| `itc_eligibility` | Medium | Calculate eligible Input Tax Credit (ITC) under Section 17(5), including blocked credit scenarios. |
| `fraud_detection` | Hard | Detect fake invoice networks, suspicious claim patterns, and missing trader fraud indicators. |

## Action Space

The action space is **free-form text GST audit analysis**.  
Agents generate structured reasoning and conclusions in natural language, including calculations, legal references, and risk findings.

## Observation Space

Each environment observation is a JSON payload containing:

- `task_id`
- `instructions`
- `case_description`
- `question`

This design enables reproducible training while preserving realistic, document-style audit prompts.

## Reward Function

Rewards are continuous in the range **0.0 to 1.0** and support partial credit. Scoring is based on:

- Correctness of computed tax amounts and differences
- Correct citation and application of legal sections
- Coverage and quality of fraud indicators identified

The reward system is intentionally granular so models can improve through iterative RL fine-tuning, not just binary pass/fail outcomes.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/` | Service health and environment metadata |
| `POST` | `/reset?task_id=` | Reset the environment to a selected task instance |
| `POST` | `/step` | Submit an agent action and receive reward/next state |
| `GET` | `/state` | Retrieve current environment state snapshot |

## Setup

Build and run locally with Docker:

```bash
docker build -t gst-audit-env .
docker run -p 7860:7860 gst-audit-env
```

## Baseline Scores

| Task | Baseline Score |
|---|---|
| Task 1 (`gstr_mismatch`) | 1.00 |
| Task 2 (`itc_eligibility`) | 0.80 |
| Task 3 (`fraud_detection`) | 0.70 |
| **Total** | **2.50 / 3.00** |

## Environment Details

- Built on the **CGST Act, 2017** and related GST compliance logic  
- Curated from **100+ real GST audit cases**  
- Covers **6 core audit categories** spanning mismatch analysis, ITC checks, and fraud risk signals  
- Designed for reproducible RL training, benchmark comparison, and policy-relevant evaluation

## Legal Framework

The environment evaluates legal reasoning against key statutory anchors, including:

- **Section 17(5)** - Blocked credits and ITC ineligibility rules
- **Section 73** - Determination of tax not paid/short paid without fraud
- **Section 74** - Determination of tax not paid/short paid due to fraud, wilful misstatement, or suppression
- **Rule 86A** - Restrictions on use of electronic credit ledger in suspicious ITC scenarios

## Why This Matters

India's tax system needs AI that is not only accurate, but legally grounded and enforcement-ready. This environment is purpose-built for that objective and represents a new benchmark category: **India-specific GST audit RL**.

It is designed to be:

- **India-first:** aligned to domestic law, filing behavior, and compliance realities
- **Novel:** a first-of-its-kind RL environment for GST auditing
- **Actionable:** useful for real enforcement workflows, risk scoring, and audit decision support

For Meta and HuggingFace judges, this project demonstrates how frontier agent training can be tightly coupled with high-impact public finance use cases.
