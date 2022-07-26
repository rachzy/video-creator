import requests

courseRouter = "http://127.0.0.1:5000/courses/"

course = {"title": "Javascript Course",
          "description": "A complete JS course!", "teacher": "Guanabara"}

response = requests.post(courseRouter + "2", course)
print(response.json())
input()
response = requests.get(courseRouter + "2")
print(response.json())
