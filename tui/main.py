import os
import requests

backend_url = "http://localhost:5000"

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def check_int_in_bounds(s: str, upper_bound: int):
    try:
        i = int(s)
        return True if (0 < i <= upper_bound) else False
    except ValueError:
        return False
    
def check_int(s: str):
    try:
        i = int(s)
        return i
    except ValueError:
        return -1

def loop_until_valid_int(prompt: str, options: list):
    choice = ""

    while choice == "" or not check_int_in_bounds(choice, len(options)):
        print(prompt + ":")

        for i in range(len(options)):
            print(f"{i + 1}: {options[i]}")

        choice = input(">> ")
        clear()
    
    return int(choice)

def loop_until_valid_amount(prompt: str):
    choice = ""

    while choice == "" or choice < -1:
        print(prompt)

        choice = check_int(input(">> "))
        clear()
    
    return int(choice)

def show_requests_owed():
    res = requests.get(backend_url+"/clientrequests")
    reqs = []
    req_ids = []

    for request in res.json():
        reqs.append(f"${request['amount']} to {request['requester_name']}\n>> Message: {request['message']}")
        req_ids.append(request['request_id'])

    reqs.append("Quit")

    choice = loop_until_valid_int("Choose the quest you want to undertake", reqs)       

    if int(choice) == len(reqs):
        return
    else:
        manage_request(req_ids[choice - 1], reqs[choice - 1])

def show_requests_made():
    res = requests.get(backend_url+"/createdrequests")

    for request in res.json():
        print(f"> ${request['amount']} from {request['requestee_name']}\n>> Message: {request['message']}\n")

    input("Press ENTER to return to the main menu.")
    clear()

def create_request():
    res = requests.get(backend_url+"/friends")
    friend_ids = []
    friends = []

    for friend in res.json():
        friends.append(f"{friend['name']} ({friend['email_address']})")
        friend_ids.append(friend['id'])

    friends.append("Exit")
    friend_ids.append("")

    done = False

    while not done:
        friends_id = loop_until_valid_int("Choose a friend to send a quest to", friends)

        if friends_id == len(friends):
            return

        id = friend_ids[friends_id - 1]

        amount = loop_until_valid_amount(f"How much does {res.json()[friends_id - 1]['name']} owe you?")

        message = input("Want to send a message? It's okay to leave it blank.\n>> ")

        answer = "a"
        while answer.lower() not in ["y", "yes", "n", "no"]:
            print(f"Request to {res.json()[friends_id - 1]['name']}")
            print(f"Amount: ${amount}")
            if message != "":
                print(f"Message: {message}")
            

            answer = input("Would you like to make this request? [Y]es, [N]o\n>> ")
            clear()

        if answer.lower() in ["y", "yes"]:
            data = {
                "requestee_id": id,
                "amount": int(amount),
                "message": message
            }
            res = requests.post(backend_url+"/requestclient", data=data)
            done = True

    return

def manage_request(req_id: str, req_data: str):
    answer = "p"
    while answer.lower() not in ["a", "accept", "d", "decline"]:
        print(req_data)
        answer = input("Would you like to accept this quest? [A]ccept, [D]ecline\n>> ")
        clear()

    data = {
            "id": req_id
    }

    if answer.lower() in ["a", "accept"]:
        data["status"] = "accepted"   
    else:
        data["status"] = "declined"

    requests.put(backend_url+"/updateclientrequest", data=data)

def main():
    print("WELCOME")
    print("=======")
    while True:
        submenu = loop_until_valid_int(
            "Choose an option",
            ["Your quests", "Quests from you", "New quest", "Exit"]
        )

        match submenu:
            case 1:
                show_requests_owed()
            case 2:
                show_requests_made()
            case 3:
                create_request()
            case 4:
                break


main()