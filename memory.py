import json
import os

class OmniMemory:
    def __init__(self, filename="agent_memory.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                json.dump({"bits": {}}, f)

    def learn(self, key, value):
        with open(self.filename, 'r+') as f:
            data = json.load(f)
            data["bits"][key] = value
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
        print(f"[Memory] '{key}' successfully saved to {self.filename}.")

    def remember(self, key):
        with open(self.filename, 'r') as f:
            data = json.load(f)
            return data["bits"].get(key, "I haven't learned that bit yet.")