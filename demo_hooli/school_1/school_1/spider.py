import requests

url = "http://www.lboro.ac.uk/study/undergraduate/courses/aeronautical-engineering/"
request = requests.get(url)
print(request.text)
