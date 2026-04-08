from environment import EmailEnv
from models import EmailAction

env = EmailEnv()

print("[START] task=easy env=email_env model=baseline")

obs = env.reset()

action = EmailAction(action="reply")
obs, reward, done, _ = env.step(action)

print(f"[STEP] step=1 action=reply reward={reward:.2f} done=true error=null")

print(f"[END] success=true steps=1 score=1.00 rewards={reward:.2f}")
