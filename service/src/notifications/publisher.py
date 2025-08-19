# publisher.py
from dataclasses import asdict, is_dataclass
import json
from typing import Any
import zmq
from .notification import Notification
from ..config import ZMQ_BINDING
from ..scopes.thread_scope import current_thread_id
# Create an asyncio-aware context
context = zmq.Context()
# Create a PUB socket
print(f"Starting ZMQ Binding to {ZMQ_BINDING}")
socket = context.socket(zmq.PUB)
socket.bind(ZMQ_BINDING)  # Bind to all interfaces on port 5555


def publish_thread_notification(notification: Notification):
    tid = current_thread_id()
    if tid is None:
        raise RuntimeError(
            "publish_thread_notification called outside thread_scope")
    publish(tid, notification)


def publish(topic: str, message: Any):
    if isinstance(message, str):
        payload = message
    elif is_dataclass(message):
        payload = json.dumps(asdict(message))
    else:
        payload = json.dumps(message, default=str)

    socket.send_multipart([topic.encode(), payload.encode()])
