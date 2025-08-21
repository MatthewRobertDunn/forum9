from flask import Flask, request, jsonify
from .middleware.simple_json_provider import SimpleJSONProvider
from .middleware.caching_decorator import cache_json_response
from .questions import questions as api_questions
from .question import question as api_question
from .submit import submit as api_submit
from .config import PUBLISH_TOKEN
from . import events as api
app = Flask(__name__)
app.json = SimpleJSONProvider(app)

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route("/questions")
def questions():
    """
    Retrieve a list of questions from the forum.
    :param date: The start date for the retrieved questions, in ISO 8601 format.
        If not provided, the most recent questions will be retrieved.
    :type date: str
    :param reverse: Whether to sort the questions in reverse chronological order.
        If not provided, the questions will be sorted in ascending chronological order.
    :type reverse: str
    :return: A JSON array of questions
    """
    return api_questions(request.args.get("date"), request.args.get("reverse"))


@app.route("/questions/<id>")
@cache_json_response(lambda x: str(len(x.get("post", []))), lambda id: f"question-{id}")
def question(id: str):
    """
    Retrieve a single question by id.
    :return: A JSON response containing the question
    """
    return api_question(id)


@app.route("/questions", methods=["POST"])
def submit():
    """
    Submit a new question to the forum.
    :return: A JSON response containing the id of the new question
    """
    return jsonify(api_submit(request.get_json()))


@app.route("/questions/<id>/events", methods=["GET"])
def events(id: str):
    """
    Stream events from a given question id.

    This endpoint uses Server-Sent Events (SSE) to stream new posts
    as they are created. Clients should set the Accept header to
    "text/event-stream" to receive events.

    :param id: The id of the question to watch
    :return: An SSE stream of new posts
    """
    return api.events(id)


@app.route("/questions/<id>/events", methods=["POST"])
def event_post(id: str):
    """
    Publish a new event to a given question id.

    This endpoint allows authorized clients to publish new events to a given
    question id. The event should be a JSON payload in the body of the request.

    :param id: The id of the question to publish to
    :return: A JSON response containing the published event
    """
    auth = request.headers.get("Authorization")
    if auth != f"Bearer {PUBLISH_TOKEN}":
        return "Unauthorized", 401
    return api.publish(id, request.get_json())
