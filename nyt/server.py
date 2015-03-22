import os
from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

from models import articles

# def abort_if_todo_doesnt_exist(todo_id):
#     if todo_id not in TODOS:
#         abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)

# Todo
#   show a single todo item and lets you delete them
class Article(Resource):
    def get(self, article_id):
        # abort_if_todo_doesnt_exist(article_id)
        return articles.find_one(article_id)

    # def delete(self, todo_id):
    #     abort_if_todo_doesnt_exist(todo_id)
    #     del TODOS[todo_id]
    #     return '', 204

    # def put(self, todo_id):
    #     args = parser.parse_args()
    #     task = {'task': args['task']}
    #     TODOS[todo_id] = task
    #     return task, 201


# TodoList
#   shows a list of all todos, and lets you POST to add new tasks
class ArticleList(Resource):
    def get(self):
        return [x for x in articles.find()]

    # def post(self):
    #     args = parser.parse_args()
    #     todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
    #     todo_id = 'todo%i' % todo_id
    #     TODOS[todo_id] = {'task': args['task']}
    #     return TODOS[todo_id], 201

class SentenceList(Resource):
    def get(self):
        return [y for y in [x['sentences'] for x in articles.find()]]

api.add_resource(SentenceList, '/sentences')
api.add_resource(ArticleList, '/articles')
api.add_resource(Article, '/articles/<article_id>')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.getenv('PORT', 5000)))
