from flask import Flask, Response, request, jsonify
from .simple_json_provider import SimpleJSONProvider
from .questions import questions as api_questions
from .question import question as api_question
from .submit import submit as api_submit
from .config import PUBLISH_TOKEN
from . import events as api

app = Flask(__name__)
app.json = SimpleJSONProvider(app)

@app.after_request
def auto_jsonify(response):
    # If the view already returned a Response, don't touch it
    if isinstance(response, Response):
        return response
    # If it returned a dict or list, jsonify it
    if isinstance(response, (dict, list)):
        return jsonify(response)
    return response


@app.route("/questions")
def questions():
    return api_questions(request.args.get("date"), request.args.get("reverse"))


@app.route("/question")
def question():
    return api_question(request.args.get("id"))


@app.route("/submit", methods=["POST"])
def submit():
    return api_submit(request.get_json())


@app.route("/events", methods=["GET"])
def events():
    return api.events(request.args.get("id"))


@app.route("/events", methods=["POST"])
def event_post():
    auth = request.headers.get("Authorization")
    if auth != f"Bearer {PUBLISH_TOKEN}":
        return
    return api.publish(request.args.get("id"), request.get_json())
