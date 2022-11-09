from flask import Flask, request
from flask import render_template
from main import app as app
from application.models import Article
from flask_security import login_required, roles_accepted, roles_required
from application import tasks
from flask_sse import sse

print("in controller app", app)

@app.route("/webhook_receiver/hello", methods=["POST"])
def webhook_hello():
    # get headers

    # parse the content
    content = request.json

    return "OK", 200


@app.route("/webhook_receiver/payments", methods=["POST"])
def webhook_payments():
    # get headers

    # parse the content
    content = request.json
    # Validate

    # call async job
    
    return "OK", 200

@app.route("/webhook_receiver/github", methods=["POST"])
def webhook_github():
    # get headers

    # parse the content
    content = request.json
    # Validate
    
    # call async job
    
    return "OK", 200
