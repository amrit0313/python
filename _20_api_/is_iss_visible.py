
import requests
from datetime import datetime

def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    # if response.status_code == 404:
    #     raise exception("The resources doesnt exists")
    # elif response.status_code == 401:
    #     raise exception("you are not authorized to get it")  #no need to do this all
    #j#ust do
    response.raise_for_status()
    data_long = float(response.json()["iss_position"]["longitude"])
    data_lat = float(response.json()["iss_position"]["latitude"])
    iss_position = (data_lat, data_long)
    if 25 <= data_lat <= 32 and 80 <= data_long <=88:
        return True

def is_night():
    parameters = {
        "lat": 28.394857,
        "lng": 84.124008,
        "formatted": 0
    }

    response = requests.get(" https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = int(datetime.now().hour)
    if sunrise >= time_now  or sunrise <=time_now:
        return  True


if is_night() and is_iss_overhead():
    print("iss is visible")
else:
    print("isn't visible")