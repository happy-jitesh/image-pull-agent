import requests
from config import MODEL, ALLOWED_ACTIONS

OLLAMA_URL = "http://localhost:11434/api/chat"


def llm_decide(context, prompt):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": [
                {"role": "system", "content": prompt},
                {"role": "user", "content": context}
            ],
            "stream": False
        }
    )

    decision = response.json()["message"]["content"].strip()

    if decision not in ALLOWED_ACTIONS:
        return "ESCALATE_TO_HUMAN"

    return decision