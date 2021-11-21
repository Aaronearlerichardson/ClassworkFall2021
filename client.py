import requests

server_name = "http://127.0.0.1:5000"

r = requests.get(server_name+"/info")
print(r.text)

out_data = {"hdl": 50, "patient_id": 200}
r = requests.post(server_name+"/hdl", json=out_data)
print(r.text)