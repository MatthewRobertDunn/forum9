# events.py
import json
from queue import Queue, Full, Empty
import threading
from typing import Dict, List, Set
from boto3.dynamodb.conditions import Key
from flask import Response
from request_handler import handle_request
from dynamodb import table

# Keep track of all client queues
clients: Dict[str, Set[Queue]] = {}
clients_lock = threading.Lock()


def add_client(id: str) -> Queue:
    q = Queue(maxsize=10)
    with clients_lock:
        if id not in clients:
            clients[id] = set()
        clients[id].add(q)
    return q


def remove_client(id: str, queue: Queue):
    with clients_lock:
        if id not in clients:
            return
        clients[id].discard(queue)
        if len(clients[id]) == 0:
            del clients[id]


def events(id: str):
    q = add_client(id)

    def stream():
        try:
            while True:
                # blocks until a message is available
                try:
                    msg = q.get(timeout=15)
                    yield f"data: {json.dumps(msg)}\n\n"
                except Empty:
                    yield f":\n\n"
        finally:  # Remove the client when disconnected
            remove_client(id, q)
    resp = Response(stream(), mimetype="text/event-stream")
    resp.headers["X-Accel-Buffering"] = "no"
    return resp


def publish(id: str, body):
    for q in list(clients.get(id, [])):
        try:
            q.put_nowait(body)
        except Full:
            pass
    return ""
