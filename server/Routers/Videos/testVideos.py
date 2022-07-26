import requests

BASE = "http://127.0.0.1:5000/"

videos = [
    {"title": "Video 1", "views": 423, "likes": 19},
    {"title": "Me at the zoo", "views": 28394724829, "likes": 123187},
    {"title": "Come to Brazil", "views": 2584918, "likes": 328572}
]

for pos, video in enumerate(videos):
    response = requests.put(BASE + f"video/{pos}", video)
    print(response.json())

input()

for pos, video in enumerate(videos):
    response = requests.get(BASE + f"video/{pos}")
    print(response.json())

input()
 
response = requests.patch(BASE + "/video/1", {"title": "Video 2"})
print(response.json())
input()
response = requests.get(BASE + "/video/1")
print(response.json())