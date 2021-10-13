from flask import Flask, request, jsonify
from blood_calc import hdl_eval

app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_status():
    return "Server is on"


@app.route("/info", methods=["GET"])
def info():
    my_output = "This server is for BME 547"
    return my_output


@app.route("/hdl/<hdl_value>", methods=["GET"])
def hdl_analysis(hdl_value):
    """
    Input should look like {"hdl": 50, "patient_id": 200}

    :return:
    :rtype:
    """

    hdl_val = int(hdl_value)
    answer = "the hdl value is " + hdl_eval(hdl_val)
    return jsonify(answer), 201


@app.route("/say_hello/<input_name>", methods=["GET"])
def say_hello(input_name):
    return "Hello {}".format(input_name)


if __name__ == "__main__":
    app.run()
