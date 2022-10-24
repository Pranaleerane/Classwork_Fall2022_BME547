
#%%
from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route("/", methods = ["GET"])
def server_status():
    return "server is on."


@app.route("/info", methods = ["GET"])
def information():
    x = "hi there."
    return x


@app.route("/hdl_check",methods = ["POST"])
def hdl_check_from_interet():
    """
        incoming_json = {"name": <name_str>,
                          "hdl_value": <hdl_value_int>}
    """
    from Blood_calculator import check_HDL
    in_data = request.get_json()
    hdl_value = in_data["hdl_value"]
    answer = check_HDL(hdl_value)
    return answer


@app.route("/add",methods = ["POST"])
def add_number():
    in_data = request.get_json()
    a = in_data["a"]
    b = in_data["b"]
    answer = a + b
    print("The answer is {}".format(answer))
    return jsonify(answer)


@app.route("/add/<a>/<b>", methods = ["GET"])
def add_variable_url(a, b):
    answer = int(a) + int(b)
    return jsonify(answer)



if __name__ == "__main__":
    app.run()
#%%