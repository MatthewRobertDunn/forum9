# publisher.py
from dataclasses import asdict
import json
from typing import Any
import zmq
from .notification import Notification
from ..config import ZMQ_BINDING
from ..scopes.thread_scope import current_thread_id
# Create an asyncio-aware context
context = zmq.Context()
# Create a PUB socket
socket = context.socket(zmq.PUB)
socket.bind(ZMQ_BINDING)  # Bind to all interfaces on port 5555


def publish_thread_notification(notification: Notification):
    tid = current_thread_id()
    if tid is None:
        raise RuntimeError(
            "publish_thread_notification called outside thread_scope")
    publish(tid, notification)


def publish(topic: str, message: Any):
    socket.send_multipart(
        [topic.encode(), json.dumps(asdict(message)).encode()])
