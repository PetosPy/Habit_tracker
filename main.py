import requests
from datetime import datetime as dt

USERNAME = "petos"
TOKEN = "hero4%gsthsggbsj3@&jhgsjj"
GRAPH_ID = "graph-1"

# Current date
time_now = dt.now()
date = time_now.strftime("%Y""%m""%d")

# Create a user account on pixela first. (POST
pixela_endpoint = "https://pixe.la/v1/users"
parameteres = {"token": TOKEN, "username":"petos", "agreeTermsOfService":"yes", "notMinor":"yes"}
# Post request with json=parameteres

# Configuring your graph (POST)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
headers= {"X-USER-TOKEN": TOKEN}
graph_config = {"id": "graph-1", "name": "Coding graph", "unit": "minutes", "type": "int", "color": "momiji"} 
#graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)

# Logging your activity on the pixela graph (POST)
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_params = {"date": date, "quantity": "50"}
# add_pixel = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(add_pixel.text)

# Updating the pixels on pixela (PUT)
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20210321"
headers= {"X-USER-TOKEN": TOKEN}
update_params = {"quantity": "2000"}

# update_response = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(update_response.text)

# Deleting a pixel
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20210501"
headers= {"X-USER-TOKEN": TOKEN}
delete_response = requests.delete(url=delete_endpoint, headers=headers)
print(delete_response.text)

