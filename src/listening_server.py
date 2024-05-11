from flask import Flask, request, jsonify


# instance of flask application
app = Flask(__name__)


@app.route("/")
def index():
    return "<p>Hello, World!</p>"



def start_server():
    print("Starting server...")
    app.run(port=5000)