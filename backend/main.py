from flask import Flask, json
from flask import request
from chatbot import respond
from corpus import inicialize_medium_corpus  # Corrected import
from evaluation import evaluate
app = Flask(__name__)

history = [] #this will eitherbe stored on the client side (local sotrage) or db
corpus = inicialize_medium_corpus()
used_question_idx = []

@app.route("/respond")
def respond_route():
    client_response = request.args.get("res")

    if client_response and history:
        print(client_response)
        # Update the last entry in the history with the client's response
        history[-1]["client"] = client_response

    return_response = respond(history, corpus, used_question_idx)
    print(return_response)
    
    return json.dumps({"response":history[-1]["bot"]["Question_Text"], "history":history})
   

@app.route("/eval")
def eval():
    if len(history)>0:
        evaluate(history)
    return json.dumps({"response":"evaluation is done"})

if __name__ =="__main__":
    app.run()
