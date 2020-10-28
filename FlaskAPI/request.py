import requests
from data_input import data_in

URL = "http://127.0.0.1:5000/predict"
HEADERS = {"Content-Type": "application/json"}
DATA = {'input': data_in}

r = requests.get(url = URL, headers = HEADERS, json = DATA)
print(r.json())
