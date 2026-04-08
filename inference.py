import os
from openai import OpenAI
from environment import EmailEnv

API_BASE_URL = os.getenv("API_BASE_URL")
API_KEY = os.getenv("API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")

client = OpenAI(
    base_url=API_BASE_URL,
    api_key=API_KEY
)

env = EmailEnv()

print(f"[START] task=email_task env=email_env model={MODEL_NAME}")

obs = env.reset()
done = False
step = 0
rewards = []

try:
    while not done and step < 3:
        step += 1

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are an email assistant."},
                {"role": "user", "content": obs["message"]}
            ],
            max_tokens=50
        )

        action_text = response.choices[0].message.content.strip()
        action = "reply" if "reply" in action_text.lower() else "ignore"

        result = env.step({"action": action})

        reward = result["reward"]
        done = result["done"]

        rewards.append(reward)

        print(f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error=null")

except Exception as e:
    print(f"[ERROR] {str(e)}")

score = sum(rewards)
success = score > 0

print(f"[END] success={str(success).lower()} steps={step} score={score:.2f} rewards={','.join([str(round(r,2)) for r in rewards])}")
