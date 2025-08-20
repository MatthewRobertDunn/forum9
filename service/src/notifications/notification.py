# notification.py
from dataclasses import dataclass


@dataclass
class Notification:
    evt: str


@dataclass
class NewPostNotification(Notification):
    persona: str
    post: str
    id: int

    def __init__(self, id: int, persona: str, post: str):
        self.id = id
        self.evt = "new"
        self.persona = persona
        self.post = post


@dataclass
class TypingNotification(Notification):
    persona: str
    count: int

    def __init__(self, persona: str, count: int):
        self.evt = "typing"
        self.persona = persona
        self.count = count
