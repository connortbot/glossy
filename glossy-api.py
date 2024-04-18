import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/query', methods=['GET'])
def query():
    return jsonify({"messages": "Hello"})

if __name__ == '__main__':
   app.run(port=5000)

# response = requests.get('http://127.0.0.1:5000/query').json()
# print(response["messages"])