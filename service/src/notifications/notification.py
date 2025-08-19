#notification.py
from dataclasses import dataclass

@dataclass
class Notification:
    evt: str

@dataclass
class NewPostNotification(Notification):
    persona: str
    post: str

@dataclass
class TypingNotification(Notification):
    persona: str
    count: int