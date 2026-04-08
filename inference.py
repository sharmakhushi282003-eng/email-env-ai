import os
from openai import OpenAI

def run():
    try:
        client = OpenAI(
            base_url=os.environ["API_BASE_URL"],
            api_key=os.environ["API_KEY"]
        )

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": "Reply politely to an email"}
            ]
        )

        return {"action": "reply"}

    except Exception as e:
        return {"action": "ignore"}
