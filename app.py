from flask import Flask, jsonify, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from resources.problems_resource import ProblemsResource
from models import db, Problem

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_data.sqlite3'
app.config.from_object('config')
#db = SQLAlchemy(app)
api = Api(app)

#app.app_context().push()

db.init_app(app)

with app.app_context():
    db.create_all()

api.add_resource(ProblemsResource, '/problems')

# Configure CORS to allow requests from your React app's domain
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# Your Flask routes and endpoints go here
#@app.route('/api/data', methods=['GET'])
#def get_data():
#    data = {"message": "Hello from Flask backend!"}
#    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)