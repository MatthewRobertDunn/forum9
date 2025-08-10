class Model:
    def __init__(self, name: str):
        self.name = name
        self.score = 0

    def add_score(self, delta: int):
        self.score = max(-10, min(10, self.score + delta))