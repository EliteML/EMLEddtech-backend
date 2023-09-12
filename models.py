class Problem(db.model):
    id = db.Column(db.Integer, primary_key=True)
    statement = db.Column(db.String(200))
    content = db.Column(db.String(300)) 

    def __repr__(self):
        return f'Problem {self.id}: {self.statement} "->" {self.content}'