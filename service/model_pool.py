from model import Model
class ModelPool:
    def __init__(self):
        self._models = {}

    def get_model(self, name: str) -> Model:
        if name not in self._models:
            self._models[name] = Model(name)
        return self._models[name]