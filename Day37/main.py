import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
PIXELA_USERNAME = "bootbastick"
PIXELA_API_TOKEN = "#=x77o1&845"
GRAPH_ID = "graph1"
user_params = {
    "token": PIXELA_API_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Programming Graph",
    "unit": "hour",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": PIXELA_API_TOKEN
}

# requests.post(url=graph_endpoint, json=graph_config, headers=headers)

graph_fill_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}"

today = datetime.datetime.now()
# print(today.strftime("%Y%m%d"))

graph_fill_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours have you spent programming today? ")
}

response = requests.post(url=graph_fill_endpoint, json=graph_fill_config, headers=headers)
print(response.text)

graph_edit_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

graph_edit_config = {
    "quantity": "2"
}

# response = requests.put(url=graph_edit_endpoint, json=graph_edit_config, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
