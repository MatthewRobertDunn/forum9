# notification.py
from dataclasses import dataclass


@dataclass
class Notification:
    evt: str


@dataclass
class NewPostNotification(Notification):
    thread_id: str
    persona: str
    post: str
    post_id: int

@dataclass
class TypingNotification(Notification):
    persona: str
    count: int

    def __init__(self, persona: str, count: int):
        self.evt = "typing"
        self.persona = persona
        self.count = count
