import database_handler as db
import dotenv
from dotenv import load_dotenv
from flask import Flask, request
import os
import psycopg2
import rbcapi_handler as rbc

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
    # i don't wanna do any error checking this is a hackathon
    data = {
    "amount": "5000000",
    "expirationDate": "2023-10-01 21:12:25.642703489 +0000 UTC m=+1387723.671519434",
    "id": "dabc360e-5685-4c1a-98a5-e0a9bcae88fc",
    "invoiceNumber": "",
    "message": "for pizza",
    "requestStatus": "PENDING",
    "requestedDate": "2023-09-16 21:12:25.642697489 +0000 UTC m=+91723.671513434",
    "requesteeId": "57124ec0-eaa9-4b11-b85a-739d1c5bff5d",
    "requesteeName": "Psyduck",
    "requesterId": "5a6c6169-5ebd-41d5-ac4e-d257dde56017",
    "requesterName": "Pikachu"
}

    # request = rbc.create_request(
    #     sample["id"], 
    #     "57124ec0-eaa9-4b11-b85a-739d1c5bff5d",
    #     5000000,
    #     "for pizza"
    # )
    # add to cached database
    return db.insert_request(conn, data)

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