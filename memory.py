import json
import os

MEMORY_FILE = "memory.json"

def save_memory(fact):
    memory = []
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            try:
                memory = json.load(f)
            except:
                memory = []

    memory.append(fact)

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

def recall_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)
