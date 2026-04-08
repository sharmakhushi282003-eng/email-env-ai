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


# ✅ REQUIRED MAIN FUNCTION
def main():
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)


# ✅ REQUIRED ENTRY POINT
if __name__ == "__main__":
    main()
