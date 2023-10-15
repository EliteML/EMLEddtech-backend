from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    cards = db.relationship('Card', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

class Problem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    statement = db.Column(db.String(200)) #Problem statement
    content = db.Column(db.String(300))  #Problem answer and/or explanation

    def __repr__(self):
        return f'Problem {self.id}: {self.statement} "->" {self.content}'

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    front = db.Column(db.String(300), nullable=False)
    back = db.Column(db.String(300), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Card, Front: {self.front}, Back: {self.back}'

# Inserts records into a mapping table
#db.session.add (model object)

# delete records from a table
#db.session.delete (model object)

# retrieves all records (corresponding to SELECT queries) from the table.
#model.query.all ()