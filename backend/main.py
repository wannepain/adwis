from flask import Flask
from flask import request
from chatbot import respond
from corpus import small_corpus
app = Flask(__name__)
@app.route("/")
def home():
    latest_response = request.args.get("res")
    print(latest_response)
    #implement response processing funcionalities inside this code
    return "<h1>Flask is working</h1>"
   
app.run()