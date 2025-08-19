from .model import Model
class ModelPool:
    def __init__(self):
        self._models = {}

    def create_model(self, name: str, max_tokens: int = 4096, priority: int = Model.DEFAULT_PRIORITY) -> Model:
        if name not in self._models:
            self._models[name] = Model(
                name, max_tokens=max_tokens, priority=priority)
        return self._models[name]

    def get_model(self, name: str) -> Model:
        if name not in self._models:
            self._models[name] = Model(name)
        return self._models[name]
