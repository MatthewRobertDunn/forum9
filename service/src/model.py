class Model:
    DEFAULT_PRIORITY = 99999
    def __init__(self, name: str, max_tokens: int = 4096, priority=DEFAULT_PRIORITY):
        self.name = name
        self.score = 0
        self.max_tokens = max_tokens
        self.priority = priority

    def add_score(self, delta: int):
        self.score = max(-10, min(10, self.score + delta))
