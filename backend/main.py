from flask import Flask, json
from flask import request
from chatbot import respond
from corpus import inicialize_medium_corpus  # Corrected import
from career import return_career
from evaluation import evaluate

app = Flask(__name__)

corpus = inicialize_medium_corpus()
used_question_idx = []


@app.route("/respond", methods=["POST"])
def respond_route():
    request_data = request.get_json()
    history_in_req = request_data["history"]

    return_response = respond(history_in_req, corpus, used_question_idx)
    print(return_response)

    return json.dumps(
        {
            "history": history_in_req,
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
