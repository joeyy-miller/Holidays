import requests
import datetime
import json
import apikey

date = datetime.datetime(2018, 6, 1)

day = date.strftime("%d")
month = date.strftime("%m")
year = date.strftime("%Y")

response = requests.get("https://holidays.abstractapi.com/v1/?api_key=" + API_KEY + "&country=US&year=" + year +"&month=" + month + "&day=" + day + "&type=national")
print(response.status_code)
print(response.content)
json_data = response.json() if response and response.status_code == 200 else None

json_dict = json.loads(response.content)

print(json_data[1]["name"])

data_len = len(json_data)
print(data_len)

print("Today is: ", end="")
for i in range(data_len):
    print(json_data[i]["name"], end="")
    if i < data_len - 1:
        print(", ", end="")
print(".")