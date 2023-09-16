class Problem(db.model):
    id = db.Column(db.Integer, primary_key=True)
    statement = db.Column(db.String(200)) #Problem statement
    content = db.Column(db.String(300))  #Problem answer and/or explanation

    def __repr__(self):
        return f'Problem {self.id}: {self.statement} "->" {self.content}'

# Inserts records into a mapping table
#db.session.add (model object)

# delete records from a table
#db.session.delete (model object)

# retrieves all records (corresponding to SELECT queries) from the table.
#model.query.all ()