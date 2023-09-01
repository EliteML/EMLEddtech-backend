from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Configure CORS to allow requests from your React app's domain
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# Your Flask routes and endpoints go here
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"message": "Hello from Flask backend!"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)