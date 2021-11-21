from flask import Flask, request, jsonify
from blood_calc import hdl_eval

app = Flask(__name__)
db = []
test = []


@app.route("/", methods=["GET"])
def server_status():
    return "Server is on"


@app.route("/new_patient", methods=["POST"])
def get_blood():
    data = request.get_json()
    error_str, status_code = validate_input(data)
    if error_str is not True:
        return error_str, status_code
    new_patient = add_database_entry(data["name"], data["id"],
                                     data["blood_type"])
    return "Added patient {}".format(new_patient)


@app.route("/add_test", methods=["POST"])
def get_test():
    data = request.get_json()
    error_str, status_code = validate_input(data,
                                            ["id", "test_name", "test_result"],
                                            [int, str, str])
    if error_str is not True:
        return error_str, status_code
    for entry in db:
        if entry["id"] == data["id"]:
            entry["tests"] = (data["test_name"], data["test_result"])
            return "added {} to id number {}".format((data["test_name"],
                                                      data["test_result"]),
                                                     data["id"]), 200
    return "no ID numbers matched id_no {}".format(data["id"])


def validate_input(in_data, expected_keys=None,
                   expected_types=None):
    if not isinstance(in_data, dict):
        return "The input was not a dictionary.", 400
    if expected_keys is None:
        expected_keys = ["name", "id", "blood_type"]
    if expected_types is None:
        expected_types = [str, int, str]
    for key in expected_keys:
        if key not in in_data:
            return "the key {} is missing from the input".format(key), 400
    for i, my_type in enumerate(expected_types):
        key = list(in_data.keys())[i]
        if type(in_data[key]) is not expected_types[i]:
            return "the key {} is not the expected " \
                   "type {}".format(key, expected_types[i]), 400
    return True, 200


def add_database_entry(patient_name, id_no, blood_type):
    new_patient = {"name": patient_name,
                   "id": id_no,
                   "blood_type": blood_type
                   }
    db.append(new_patient)
    return new_patient


if __name__ == "__main__":
    app.run()
