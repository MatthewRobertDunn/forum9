# publisher.py
from dataclasses import asdict, is_dataclass
import json
from typing import Any
import zmq
from . import topics
from .notifications import NewPostNotification
from ..config import ZMQ_BINDING
from ..scopes.thread_scope import current_thread_id
# Create a ZMQ context
context = zmq.Context()
# Create a PUB socket
print(f"Starting ZMQ Binding to {ZMQ_BINDING}")
socket = context.socket(zmq.PUB)
for binding in ZMQ_BINDING:
    print(f"Binding to {binding}")
    socket.bind(binding)


def publish(topic: str, message: Any):
    if isinstance(message, str):
        payload = message
    elif is_dataclass(message):
        payload = json.dumps(asdict(message))
    else:
        payload = json.dumps(message, default=str)

    socket.send_multipart([topic.encode(), payload.encode()])
