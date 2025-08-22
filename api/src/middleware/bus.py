from threading import Thread
import traceback
import zmq
from flask import Flask
from ..config import ZMQ_BINDING
from . import topics
app = Flask(__name__)

# Map topic -> handler function
handlers = {}


def start():
    Thread(target=subscriber, daemon=True).start()


def register_handler(topic, func):
    handlers[topic] = func


def subscriber():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    for binding in ZMQ_BINDING:
        print(f"Connecting to {binding}")
        socket.connect(binding)
    socket.setsockopt_string(zmq.SUBSCRIBE, topics.new_post)
    socket.setsockopt_string(zmq.SUBSCRIBE, topics.new_thread)
    while True:
        topic, content = socket.recv_multipart()
        topic = topic.decode()
        content = content.decode()
        handler = handlers.get(topic)

        if handler:
            try:
                handler(content)
            except Exception as e:
                print(f"Error in handler for topic '{topic}': {e}")
                traceback.print_exc()
        else:
            print(f"No handler for topic '{topic}', content: {content}")
