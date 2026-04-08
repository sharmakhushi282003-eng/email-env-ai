from fastapi import FastAPI
from environment import EmailEnv

app = FastAPI()
env = EmailEnv()

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: dict):
    return env.step(action)
