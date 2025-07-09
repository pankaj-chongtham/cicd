from flask import Flask, jsonify
import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

app = Flask(__name__)

@app.route('/api/greeting', methods=['GET'])
def greeting():
    return jsonify({"message": "Hello, World!"})

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({
        "status": "online",
        "environment": os.getenv('ENVIRONMENT', 'development'),
        "timestamp": datetime.datetime.now().isoformat(),
        "version": "1.0.0"
    })

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        "health": "healthy",
        "service": "Flask Demo App",
        "uptime": "running"
    })

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to CI/CD Demo Application",
        "endpoints": [
            "/api/greeting",
            "/api/status", 
            "/api/health"
        ]
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('ENVIRONMENT', 'development') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)