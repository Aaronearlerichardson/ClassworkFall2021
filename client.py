import requests


patient1 = {"name": "Ann Ables", "id": 201, "blood_type": "A+"}
r = requests.post("http://127.0.0.1:5000/new_patient", json=patient1)
print(r.status_code)
print(r.text)

server_name = "http://127.0.0.1:5000"

r = requests.get(server_name+"/info")
print(r.text)

out_data = {"hdl": 50, "patient_id": 200}
r = requests.post(server_name+"/hdl", json=out_data)
print(r.text)

