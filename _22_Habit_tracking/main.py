#Its like habit tracking, like where we can show what we did with a square pixels
# Its intensity describes how much we did that work
#similar to gitHub repo tracker, the green pixels

from _datetime import datetime
import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "amrithereandthere"
USERNAME = "amritz"

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}


#
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)  # we have now created an account

GRAPH_ENDPOINT = F"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_configs = {
    "id":"graph1",
    "name":"my_days",
    "unit":"Commits",
    "type":"int",
    "color":"ajisai"
}
headers = {
    "X-USER-TOKEN":TOKEN
}

# response2 = requests.post(url=GRAPH_ENDPOINT, json=graph_configs, headers=headers)
# print(response2.text) #Now we have created a graph

PIXEL_ENDPOINT = F"{GRAPH_ENDPOINT}/graph1"

pixel_configs = {
    "date": "20241210",
    "quantity":"9",
    }
# response3 = requests.post(url=PIXEL_ENDPOINT, json=pixel_configs, headers=headers)
# print(response3.text)  #to add pixels #Now we have created a pixel for what we did

today = datetime(year=2024, month=12, day=12)
date = today.strftime("%Y%m%d")
UPDATE_ENDPOINT = F"{PIXEL_ENDPOINT}/{date}"
data ={
    "quantity":"10"
}
# response4 = requests.put(url=UPDATE_ENDPOINT, json=data, headers=headers)
# print(response4.text) #Now we can update the pixel, if we have given wrong quantity of what we did

# response5 = requests.delete(url=UPDATE_ENDPOINT, headers=headers)
# print(response5.text) #Here we can delete the existing pixel