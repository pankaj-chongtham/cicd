from flask import Flask, jsonify
import datetime
import os

app = Flask(__name__)

@app.route('/api/greeting', methods=['GET'])
def greeting():
    return jsonify({"message": "Hello, World!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0')