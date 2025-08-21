# notification.py
from dataclasses import dataclass

@dataclass
class NewPostNotification:
    thread_id: str
    post: dict


@dataclass
class TypingNotification:
    persona: str
    count: int
