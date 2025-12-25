from telegram.sender import send_text
import requests
from core.config import BACKEND_URL, SERVICE_API_KEY

def handle_text(chat_id: int, text: str):
    user_id = f"tg:{chat_id}"
    headers = {"x-api-key": SERVICE_API_KEY}

    if text.startswith("next"):
        _, skill = text.split(maxsplit=1)
        resp = requests.get(
            f"{BACKEND_URL}/lessons/next",
            params={"user_id": user_id, "skill": skill},
            headers=headers
        ).json()

        if resp.get("status") == "done":
            send_text(chat_id, "🎉 Skill completed!")
            return

        content = resp["content"]
        msg = f"*{resp['title']}*\n\n"
        for s in content["sections"]:
            msg += f"*{s['heading']}*\n{s['content']}\n\n"

        msg += f"\nType `done {resp['id']}` when finished."
        send_text(chat_id, msg)
