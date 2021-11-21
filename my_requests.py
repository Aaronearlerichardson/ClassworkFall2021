import requests

server_name = "http://vcm-21170.vm.duke.edu:5000/"

r = requests.get(server_name + "student")
request_json = {
    "name": "Aaron Earle-Richardson",
    "net_id": "ae166",
    "e-mail": "aaron.earlerichardson@duke.edu"
}

s = requests.post(server_name + "student", json=request_json)
print(s.text)