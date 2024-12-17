import requests
import json

with open("cookies.json", "r") as file:
    cookies = json.load(file)

cookies_dict = {cookie["name"]: cookie["value"] for cookie in cookies}

url = "https://cedtintern.cp.eng.chula.ac.th/api/sessions/3/openings?search=&page=1&limit=200&onlyBookmarked=false&onlyAvailablePositions=false"

response = requests.get(url, cookies=cookies_dict)

if response.status_code == 200:
    print("Request successful!")
    jsonFile = open("openings.json", "w+")
    jsonFile.write(json.dumps(response.json()))
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)
