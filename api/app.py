from flask import Flask, request
from questions import questions as api_questions
from submit import submit as api_submit
app = Flask(__name__)

@app.route("/questions.py")
def list_before():
    return api_questions(request.args.get("date"), request.args.get("reverse"))

@app.route("/submit.py", methods=["POST"])
def submit():
    return api_submit(request.data)