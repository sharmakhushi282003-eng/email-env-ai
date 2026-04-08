from fastapi import FastAPI
from environment import EmailEnv
from models import EmailAction

app = FastAPI()
env = EmailEnv()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/reset")
def reset():
    obs = env.reset()
    return {"message": obs.message}

@app.post("/step")
def step(action: EmailAction):
    obs, reward, done, _ = env.step(action)
    return {
        "message": obs.message,
        "reward": reward,
        "done": done
    }
