from dotenv import load_dotenv
from flask import Flask, request
import os
import psycopg2

load_dotenv()

app = Flask(__name__)
conn = psycopg2.connect(os.environ["DATABASE_URL"])

sample = {
    "id": "asdf",
    "name": "name here",
    "email_address": "a@a.com"
}

@app.route("/friends", method=["GET"])
def get_friends():
    # query from database
    # return all friends in a nice json format
    pass

@app.route("/profile", method=["GET"])
def get_profile():
    # get your own profile info
    pass

@app.route("/createdrequests", method=["GET"])
def get_created_requests():
    # get all requests in which you're requester
    pass

@app.route("/clientrequests", method=["GET"])
def get_requests():
    # get all single requests involving you as requestee
    pass

@app.route("/grouprequests", method=["GET"])
def get_group_requests():
    # get all group requests involving you as requestee
    pass

@app.route("/requestclient", method=["POST"])
def create_request():
    # add to rbc thing
    # add to cached database
    pass

@app.route("/requestgroup", method=["POST"])
def create_group_request():
    # make request for each person in the group
    # add to rbc
    # add to cached database
    pass

@app.route("/debug/createclient", methods=["POST"])
def create_client_account():
    # creates a client on both the RBC and cache side
    client_info = request.get_json()

@app.route("/updateclientrequest", method=["PUT"])
def update_client_request():
    # get id of request
    # change to accepted on rbc
    # change to paid as full on site
    pass