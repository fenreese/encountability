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
    # get your own profile info if you don't provide one
    id = request.args.get("id", default=sample["id"], type=str)
    client = db.query_client(conn, id)
    return {
        "email_address": client[0],
        "id": client[1],
        "name": client[2]
    }

@app.route("/createdrequests", methods=["GET"])
def get_created_requests():
    # get all requests in which you're requester
    # "These people owe you..."
    query_res = db.query_created_reqs(conn, sample["id"])
    broke_people = []

    for entry in query_res:
        broke_people.append({
            "request_id": entry[0],
            "requestee_id": entry[1],
            "amount": entry[2],
            "message": entry[3],
            "paid_amount": entry[4],
            "requestee_name": entry[5],
            "requestee_email": entry[6]
            })

    return broke_people

@app.route("/clientrequests", methods=["GET"])
def get_requests():
    # get all single requests involving you as requestee
    # "You owe these people..."
    query_res = db.query_requestee_reqs(conn, sample["id"])
    mean_people = []

    for entry in query_res:
        mean_people.append({
            "request_id": entry[0],
            "requester_id": entry[1],
            "amount": entry[2],
            "message": entry[3],
            "paid_amount": entry[4],
            "requester_name": entry[5],
            "requester_email": entry[6]
            })

    return mean_people 

@app.route("/clientrequest", methods=["GET"])
def get_request():
    # expects id
    req_json = request.get_json()
    id = req_json["id"]
    
    return rbc.get_request_by_id(id)
    # res = db.query_request(conn, id)

    # return res[0]

@app.route("/requestclient", methods=["POST"])
def create_request():
    # json assumes requestee_id, amount, and message
    req_data = request.get_json(force=True)

    # add to rbc thing
    # i don't wanna do any error checking this is a hackathon
    data = rbc.create_request(
        sample["id"], 
        req_data["requestee_id"],
        req_data["amount"],
        req_data["message"]
    )

    # add to cached database
    return db.insert_request(conn, data)

@app.route("/updateclientrequest", methods=["PUT"])
def update_client_request():
    req_json = request.get_json()

    # get id of request
    transfer_request_id = req_json["id"]
    status = req_json["status"]
    
    # change state on rbc
    rbc.update_request(transfer_request_id, status)
    
    # change state on cache
    return db.update_request(conn, transfer_request_id, status)

# EVERYTHING BELOW HERE IS A WIP

@app.route("/createdgrouprequests", methods=["GET"])
def get_group_requests():
    # get all group requests involving you as requester
    return "not implemented yet"

@app.route("/grouprequest", methods=["GET"])
def get_group_request():
    # get group request by id
    return "not implemented yet"

@app.route("/requestgroup", methods=["POST"])
def create_group_request():
    # expects total amount, list of people's ids, and message
    req_data = request.get_json(force=True)
    total_cost = req_data["amount"]
    people = req_data["friends"]
    message = req_data["message"]
    count = 0

    # TODO: create ids for group purchases
    # NOTE: i'm too lazy to fully implement this

    split_amount = total_cost / len(people)
    # make request for each person in the group
    for person in people:
        # add to rbc
        data = rbc.create_request(
            sample["id"],
            person,
            split_amount,
            message
        )
        # add to cached database
        count += 1 if db.insert_request(conn, data) == "success" else 0

    return "success" if count == people else "failure"
   