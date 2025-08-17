from flask import Flask, Response, request, jsonify
import time
from questions import questions as api_questions
from question import question as api_question
from submit import submit as api_submit
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


@app.route("/events")
def time_stream():
    def generate():
        while True:
            yield f"data: {time.ctime()}\n\n"
            time.sleep(1)
    resp = Response(generate(), mimetype="text/event-stream")
    resp.headers["X-Accel-Buffering"] = "no"
    return resp