from flask import Flask
from requests import request
from flask import jsonify


app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()  # Get JSON data from the request
    if 'first' in data and 'second' in data:
        result = data['first'] + data['second']
        return jsonify({"result": result})
    else:
        return jsonify({"error": "Invalid input format"}), 400

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()  # Get JSON data from the request
    if 'first' in data and 'second' in data:
        result = data['first'] - data['second']
        return jsonify({"result": result})
    else:
        return jsonify({"error": "Invalid input format"}), 400

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
