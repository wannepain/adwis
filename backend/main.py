from flask import Flask, json
from flask import request
from flask_cors import CORS, cross_origin
from chatbot import respond
from corpus import inicialize_medium_corpus  # Corrected import
from career import return_career
from evaluation import evaluate

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

corpus = inicialize_medium_corpus()
used_question_idx = []


@app.route("/", methods=["GET"])
@cross_origin()
def home():
    return "Hello, World!"


@app.route("/respond", methods=["POST"])
@cross_origin()
def respond_route():  # need to move the used question idx to the global scope
    request_data = request.get_json()
    history_in_req = request_data["history"]
    print(f"history_in_req:{history_in_req}")
    used_question_idx = request_data["used_question_idx"]
    print(f"used_question_idx:{used_question_idx}")

    return_response = respond(history_in_req, corpus, used_question_idx)
    print(return_response)

    return json.dumps(
        {
            "history": history_in_req,
            "used_question_idx": used_question_idx,
        }
    )


@app.route("/career", methods=["POST"])
def career_route():
    request_data = request.get_json()
    history_in_req = request_data["history"]
    career = return_career(history_in_req)
    return json.dumps({"career": career})


if __name__ == "__main__":
    app.run()
