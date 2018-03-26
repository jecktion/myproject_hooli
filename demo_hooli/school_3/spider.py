import requests

url = "http://www.international.unsw.edu.au/faculty/art-design-undergraduate-degree-programs"
request = requests.get(url)
print(request.text)
