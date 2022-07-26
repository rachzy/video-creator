from flask_restful import Resource, reqparse, abort

courses_post_args = reqparse.RequestParser()
courses_post_args.add_argument(
    "title", type=str, help="Title of the course is required.", required=True)
courses_post_args.add_argument(
    "description", type=str, help="Description of the course is required.", required=True)
courses_post_args.add_argument(
    "teacher", type=str, help="Teacher of the course is required.", required=True)

courses = []


def getCourseById(courseId):
    for course in courses:
        if(str(course["id"]) == str(courseId)):
            return course
    return False


def abortIfCourseDoesNotExist(courseId):
    if (getCourseById(courseId) == False):
        abort(404, message="A course with that ID does not exist...")


def abortIfCourseExists(courseId):
    if(getCourseById(courseId)):
        abort(409, message="A course with that ID already exists...")


class Courses(Resource):
    def get(self, courseId):
        abortIfCourseDoesNotExist(courseId)
        return getCourseById(courseId)

    def post(self, courseId):
        abortIfCourseExists(courseId)

        args = courses_post_args.parse_args()

        newCourse = dict({
            "id": courseId,
            **args
        })
        courses.append(newCourse)
        return {"message": "Course successfully created!"}
