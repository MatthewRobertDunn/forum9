from threading import Thread
from flask import Flask, request, jsonify

from .middleware import bus
from .middleware.simple_json_provider import SimpleJSONProvider
from .middleware.cache import cache_json_response
from .threads import threads as api_threads
from .thread import thread as api_thread
from .submit import submit as api_submit
from .config import PUBLISH_TOKEN
from . import events as api
from . import handlers
app = Flask(__name__)
app.json = SimpleJSONProvider(app)
bus.start()
handlers.new_post.register()

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route("/threads")
def threads():
    """
    Retrieve a list of threads from the forum.
    :param date: The start date for the retrieved threads, in ISO 8601 format.
        If not provided, the most recent threads will be retrieved.
    :type date: str
    :param reverse: Whether to sort the threads in reverse chronological order.
        If not provided, the threads will be sorted in ascending chronological order.
    :type reverse: str
    :return: A JSON array of threads
    """
    return api_threads(request.args.get("date"), request.args.get("reverse"))


@app.route("/threads/<id>")
# @cache_json_response(lambda x: str(len(x.get("post", []))), lambda id: f"thread-{id}")
def thread(id: str):
    """
    Retrieve a single thread by id.
    :return: A JSON response containing the thread
    """
    return api_thread(id)


@app.route("/threads", methods=["POST"])
def submit():
    """
    Submit a new thread to the forum.
    :return: A JSON response containing the id of the new thread
    """
    return jsonify(api_submit(request.get_json()))


@app.route("/threads/<id>/events", methods=["GET"])
def events(id: str):
    """
    Stream events from a given thread id.

    This endpoint uses Server-Sent Events (SSE) to stream new posts
    as they are created. Clients should set the Accept header to
    "text/event-stream" to receive events.

    :param id: The id of the thread to watch
    :return: An SSE stream of new posts
    """
    return api.events(id)


@app.route("/threads/<id>/events", methods=["POST"])
def event_post(id: str):
    """
    Publish a new event to a given thread id.

    This endpoint allows authorized clients to publish new events to a given
    thread id. The event should be a JSON payload in the body of the request.

    :param id: The id of the thread to publish to
    :return: A JSON response containing the published event
    """
    auth = request.headers.get("Authorization")
    if auth != f"Bearer {PUBLISH_TOKEN}":
        return "Unauthorized", 401
    return api.publish(id, request.get_json())
