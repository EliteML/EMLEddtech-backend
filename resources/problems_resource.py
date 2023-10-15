from flask_restful import Resource, reqparse
from models import db, Problem

parser = reqparse.RequestParser()
parser.add_argument('statement', type=str, required=True, help='Statement is required')
parser.add_argument('content', type=str, required=True, help='Content is required')

class ProblemsResource(Resource):
    def get(self):
        problems = Problem.query.all()
        return {'problems': [{'id': problem.id, 'statement': problem.statement, 'content': problem.content} for problem in problems]}

    def post(self):
        args = parser.parse_args()

        problem = Problem(statement=args['statement'], content=args['content'])
        db.session.add(problem)
        db.session.commit()

        return {'problem_id': problem.id, 'statement': problem.statement, '': problem.content}, 201