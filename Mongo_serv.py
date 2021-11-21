from flask import Flask, request
import logging
from pymodm import connect, MongoModel, fields
from typing import Union, Tuple, Dict

app = Flask(__name__)

db = []


def initialize_server():
    logging.basicConfig(filename="health_db_server_log", level=logging.DEBUG)
    print("connecting to Mongo db...")
    connect("mongodb+srv://ae166:<password>@cluster0.vuvpj.mongodb.net/"
            "myFirstDatabase?retryWrites=true&w=majority")
    print("connected")


@app.route("/", methods=["GET"])
def get_status():  # no test needed!
    return "Server is on"


@app.route("/api/new_patient", methods=["POST"])
def new_patient():  # no test needed!
    data = request.get_json()
    error_str, status_code = validate_input(data,
                                            {"patient_id": int,
                                             "attending_username": str,
                                             "patient_age": int})
    if error_str is not True:
        return error_str, status_code
    added_patient = add_database_entry(*data)
    return "Added patient {}".format(added_patient), 200


@app.route("/api/new_attending", methods=["POST"])
def new_attending():  # no test needed!
    data_inside = request.get_json()
    expected_keys = {"attending_username": str,
                     "attending_email": str, "attending_phone": str}
    error_str, status_code = validate_input(data_inside, expected_keys)
    if error_str is not True:
        return error_str, status_code
    added_attending = add_database_entry(data_inside["attending_username"],
                                         data_inside["attending_email"],
                                         data_inside["attending_phone"])
    return "Added attending {}".format(added_attending), 200


class Patient(MongoModel):
    name = fields.CharField()
    id = fields.IntegerField()
    blood_type = fields.CharField()
    tests = fields.ListField()


def add_database_entry(patient_name, id_no, blood_type):
    patient_to_add = Patient(name=patient_name, id=id_no,
                             blood_type=blood_type)
    answer = patient_to_add.save()
    return answer


def validate_input(in_data: dict,  # TESTED
                   expected: Dict[str, type]) -> Tuple[Union[str, bool], int]:
    if not isinstance(in_data, dict):
        return "The input was not a dictionary.", 400
    for key, value in expected.items():
        if key not in in_data.keys():
            return "the key {} is missing from the input".format(key), 400
        elif not isinstance(in_data[key], value):
            return "the key '{}' is a {}," \
                   " should be {}".format(key, type(in_data[key]),
                                          expected[key]), 400
    return True, 200


def add_test_result(patient, in_data):
    test_data_to_add = (in_data["test_name"])


if __name__ == "__main__":
    initialize_server()
    app.run()
