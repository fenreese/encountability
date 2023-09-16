import requests

url = "http://money-request-app.canadacentral.cloudapp.azure.com:8080/api/v1"

def create_request(requestor: str, requestee: str, amount: int, message: str):
    data = {
        "amount": str(amount),
        "requesteeId": requestee,
        "message": message
    }

    res = requests.post(url+"/money-request", data=data,
                        headers={"x-signed-on-client": requestor})
    
    return res.json()