# history.py
import json
from datetime import datetime

HISTORY_FILE = "history.json"

def save_history(username, dna_data):
    try:
        with open(HISTORY_FILE, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    if username not in data:
        data[username] = []

    data[username].append({
        "timestamp": datetime.now().isoformat(),
        "dna": dna_data
    })

    with open(HISTORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_user_history(username):
    try:
        with open(HISTORY_FILE, "r") as f:
            data = json.load(f)
        return data.get(username, [])
    except:
        return []
