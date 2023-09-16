import database_handler as db
import dotenv
from dotenv import load_dotenv
from flask import Flask, request
import os
import psycopg2

load_dotenv()

app = Flask(__name__)
conn = psycopg2.connect(os.environ["DATABASE_URL"])

sample = {
    "email_address": "pik@chu.com",
    "id": "5a6c6169-5ebd-41d5-ac4e-d257dde56017",
    "name": "Pikachu"
}

@app.route("/friends", methods=["GET"])
def get_friends():
    # query from database
    res = db.query_friends_list(conn, sample["id"])

    # return all friends in a nice json format
    friends_list = []

    for pair in res:
        friends_list.extend([x for x in pair if x != sample["id"]])

    friends_objects = []

    for client in db.query_profiles(conn, tuple(friends_list)):
        friends_objects.append({
            "email_address": client[0],
            "id": client[1],
            "name": client[2]
        })

    return friends_objects

@app.route("/profile", methods=["GET"])
def get_profile():
    # get your own profile info
    return sample

@app.route("/createdrequests", methods=["GET"])
def get_created_requests():
    # get all requests in which you're requester
    pass

@app.route("/clientrequests", methods=["GET"])
def get_requests():
    # get all single requests involving you as requestee
    pass

@app.route("/clientrequest", methods=["GET"])
def get_request():
    # get request by id 
    pass

@app.route("/grouprequests", methods=["GET"])
def get_group_requests():
    # get all group requests involving you as requestee
    pass

@app.route("/grouprequest", methods=["GET"])
def get_group_request():
    # get group request by id
    pass

@app.route("/requestclient", methods=["POST"])
def create_request():
    # add to rbc thing
    # add to cached database
    pass

@app.route("/requestgroup", methods=["POST"])
def create_group_request():
    # make request for each person in the group
    # add to rbc
    # add to cached database
    pass

@app.route("/updateclientrequest", methods=["PUT"])
def update_client_request():
    # get id of request
    # change to accepted on rbc
    # change to paid as full on site
    pass