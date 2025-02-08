from flask import Flask, request, jsonify
from questions import questions as api_questions
from question import question as api_question
from submit import submit as api_submit
app = Flask(__name__)

@app.route("/questions.py")
def questions():
    return api_questions(request.args.get("date"), request.args.get("reverse"))

@app.route("/question.py")
def question():
    return api_question(request.args.get("id"))

@app.route("/submit.py", methods=["POST"])
def submit():
    return  jsonify(api_submit(request.get_json()))