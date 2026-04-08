---
title: Email Env AI
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
---

# Email Env AI

## Description
This is a simple real-world inspired OpenEnv environment that simulates email triage.

The agent receives an email and must decide how to act (e.g., reply or ignore).  
The goal is to take the correct action to maximize reward.

## Environment Details

### Observation
- message: Incoming email text

### Action
- action: String (example: "reply")

## Tasks

### Easy Task
- Identify and reply to a basic email  
- Reward: 1.0 for correct action  

### Medium Task
- Handle slightly complex emails  
- Partial rewards based on correctness  

### Hard Task
- Complex decision making with strict grading  

## Reward Logic
- Correct action → reward = 1.0  
- Incorrect action → reward = 0.0  

## How to Run

The environment is deployed using Docker and runs automatically.

API Endpoints:
- POST /reset → Initializes environment  
- POST /step → Takes action and returns result  

## Baseline

A simple baseline agent is included in inference.py.

## Motivation

Email triage is a real-world task commonly performed by humans.  
This environment helps evaluate how well an AI agent can take correct actions.

## Tech Stack
- FastAPI  
- Docker  
- Pydantic  
