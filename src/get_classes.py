import requests


endpoint = "https://sis.rutgers.edu/oldsoc/courses.json?semester=12022&campus=NB&level=UG?coreCode=CC&subject="
response = requests.get("http://api.open-notify.org/astros.json")

print(response)
