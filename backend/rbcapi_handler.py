import requests

url = "http://money-request-app.canadacentral.cloudapp.azure.com:8080/api/v1"
actions = {
    "accepted": "ACCEPT",
    "declined": "DECLINE"
}

def create_request(requestor: str, requestee: str, amount: int, message: str):
    data = {
        "amount": str(amount),
        "requesteeId": requestee,
        "message": message
    }

    res = requests.post(url+"/money-request", data=data,
                        headers={"x-signed-on-client": requestor})
    
    return res.json()

def update_request(request_id: str, status: str):
    status = actions.get(status)
    
    res = requests.put(url+"/money-request/"+request_id, data={"Action": status})

    return res.json()

def get_request_by_id(request_id: str):
    res = requests.get(url+"/money-request/"+request_id)

    return res.json()