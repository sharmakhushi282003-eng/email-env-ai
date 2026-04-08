from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/reset")
def reset():
    return {"message": "New task"}

@app.post("/step")
def step(action: dict):
    return {"reward": 0.5, "done": True}
