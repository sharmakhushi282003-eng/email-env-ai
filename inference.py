import os
from environment import EmailEnv

# 🔥 SAFE IMPORT
try:
    from openai import OpenAI
    openai_available = True
except:
    openai_available = False

API_BASE_URL = os.getenv("API_BASE_URL")
API_KEY = os.getenv("API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")

env = EmailEnv()

print(f"[START] task=email_task env=email_env model={MODEL_NAME}")

obs = env.reset()
done = False
step = 0
rewards = []

try:
    while not done and step < 3:
        step += 1

        action = "reply"  # default fallback

        # 🔥 TRY LLM CALL
        if openai_available and API_BASE_URL and API_KEY:
            try:
                client = OpenAI(
                    base_url=API_BASE_URL,
                    api_key=API_KEY
                )

                response = client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=[
                        {"role": "system", "content": "You are an email assistant."},
                        {"role": "user", "content": str(obs)}
                    ],
                    max_tokens=50
                )

                text = response.choices[0].message.content.lower()

                if "ignore" in text:
                    action = "ignore"

            except Exception as e:
                print(f"[LLM ERROR] {e}")

        result = env.step({"action": action})

        reward = result.get("reward", 0)
        done = result.get("done", True)

        rewards.append(reward)

        print(f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error=null")

except Exception as e:
    print(f"[ERROR] {e}")

score = sum(rewards)
success = score > 0

print(f"[END] success={str(success).lower()} steps={step} score={score:.2f} rewards={','.join([str(round(r,2)) for r in rewards])}")
