import requests
from datetime import datetime

NUTRITIONIX_API_KEY = "04344b313884cb460d12f283f8a2c80adfdsfsdfdsa"
WORKOUT = input("which exercise did you do today: ")
APP_ID = "d3a7cb4fdfkdjfjsd"

data = {
    "query":f" I ran {WORKOUT} mile",
    "weight_kg":64,
    "height_cm":165,
    "age":22
}
headers = {
    "x-app-id":APP_ID,
    "x-app-key":NUTRITIONIX_API_KEY
}

response = requests.post(url = "https://trackapi.nutritionix.com/v2/natural/exercise", json=data, headers=headers)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

response2 = requests.post(url="https://api.sheety.co/8e7cb96a45911ef0ac2bd4e04ed73772/workoutTracks/workouts",json= sheet_inputs)
print(response2.text)