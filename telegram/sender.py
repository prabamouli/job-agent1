import requests
from core.config import TELEGRAM_BOT_TOKEN

API = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

def send_text(chat_id: int, text: str):
    requests.post(f"{API}/sendMessage", json={
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    })
