from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin
from Routers import Videos, Courses

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

api.add_resource(Videos.Videos, "/video/<int:videoId>")
api.add_resource(Courses.Courses, "/courses/<int:courseId>")

class Status(Resource):
    def get(self):
        return {"message": "Server is online!"}, 200

api.add_resource(Status, '/')

if __name__ == "__main__":
    app.run(debug=True)
