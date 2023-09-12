from flask import Flask, jsonify, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_data.sqlite3'
db = SQLAlchemy(app)

app.app_context().push()

# Configure CORS to allow requests from your React app's domain
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# Your Flask routes and endpoints go here
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"message": "Hello from Flask backend!"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)