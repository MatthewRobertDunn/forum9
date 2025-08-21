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


@app.route("/questions")
def questions():
    """
    Retrieve a list of questions from the forum.

    The endpoint will return a JSON array of questions, with each question
    containing the fields "id", "question", "created_date", and "post".

    :param date: The start date for the retrieved questions, in ISO 8601 format.
        If not provided, the most recent questions will be retrieved.
    :type date: str
    :param reverse: Whether to sort the questions in reverse chronological order.
        If not provided, the questions will be sorted in ascending chronological order.
    :type reverse: str
    :return: A JSON array of questions
    :rtype: list
    """
    return api_questions(request.args.get("date"), request.args.get("reverse"))


@app.route("/questions/<id>")
@cache_json_response(lambda x: str(len(x.get("post", []))), lambda x: f"question-{x}")
def question(id: str):
    """
    Retrieve a single question by id.

    This endpoint will return a JSON payload containing the question with the
    given id. The payload will contain the question text, the id of the question,
    and a list of posts as a list of objects with the keys "content", "persona",
    and "date" corresponding to the content of the post, the name of the persona
    who made the post, and the date the post was made.

    :param id: The id of the question to be retrieved
    :type id: str

    :return: A JSON response containing the question
    """
    return api_question(id)


@app.route("/questions", methods=["POST"])
def submit():
    """
    Submit a new question to the forum.

    This endpoint will accept a JSON payload containing a single field, "message", which
    will be used to generate a new question in the forum.

    :param message: The message to be posted as the new question
    :type message: str

    :return: A JSON response containing the id of the new question
    :rtype: dict
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
