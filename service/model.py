class Model:
    def __init__(self, name: str, max_tokens: int = 4096):
        self.name = name
        self.score = 0
        self.max_tokens = max_tokens

    def add_score(self, delta: float):
        self.score = max(-10, min(10, self.score + delta))