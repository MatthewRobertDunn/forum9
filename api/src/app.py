from flask import Flask, Response, request, jsonify
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
    return api_questions(request.args.get("date"), request.args.get("reverse"))


@app.route("/question")
@cache_json_response(lambda x: str(len(x.get("post", []))))
def question():
    return api_question(request.args.get("id"))


@app.route("/submit", methods=["POST"])
def submit():
    return jsonify(api_submit(request.get_json()))


@app.route("/events", methods=["GET"])
def events():
    return api.events(request.args.get("id"))


@app.route("/events", methods=["POST"])
def event_post():
    auth = request.headers.get("Authorization")
    if auth != f"Bearer {PUBLISH_TOKEN}":
        return
    return api.publish(request.args.get("id"), request.get_json())
