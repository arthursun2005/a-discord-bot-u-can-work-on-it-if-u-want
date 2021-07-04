import json

class Manager:
    def __init__(self):
        with open('data.json', 'r') as f:
            self.data = json.load(f)

    def update(self):
        with open('data.json', 'w') as f:
            json.dump(self.data, f)

