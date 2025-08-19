from flask import Flask, request, jsonify
from .questions import questions as api_questions
from .question import question as api_question
from .submit import submit as api_submit
from .config import PUBLISH_TOKEN
from . import events as api

app = Flask(__name__)

@app.route("/questions")
def questions():
    return api_questions(request.args.get("date"), request.args.get("reverse"))

@app.route("/question")
def question():
    return api_question(request.args.get("id"))

@app.route("/submit", methods=["POST"])
def submit():
    return  jsonify(api_submit(request.get_json()))


@app.route("/events", methods=["GET"])
def events():
    return api.events(request.args.get("id"))

@app.route("/events", methods=["POST"])
def event_post():
    auth = request.headers.get("Authorization")
    if auth != f"Bearer {PUBLISH_TOKEN}":
        return 
    return api.publish(request.args.get("id"), request.get_json())