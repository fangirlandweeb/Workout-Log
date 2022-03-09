import requests
from datetime import datetime
import os

API_KEY = os.environ.get("WORKOUTAPI")
APP_ID = os.environ.get("WORKOUT_APPID")
USERNAME = os.environ.get("SHEETY_USERNAME")
PASSWORD = os.environ.get("SHEETY_PWD")
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")

GENDER = "female"
WEIGHT = 111
HEIGHT = 172
AGE = 22

user_input = input("What did you do today? ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY

user_info = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

r = requests.post(url=API_ENDPOINT, json=user_info, headers=headers)
result = r.json()
print(result)

today = datetime.now().strftime("%d/%m/%Y")
when = datetime.now().strftime("%X")

for each in result["exercises"]:
    sheety_params = {
        "workout": {
            "date": today,
            "time": when,
            "exercise": each["name"].title(),
            "duration": each["duration_min"],
            "calories": each["nf_calories"]
        }
    }

'''sheety_r = requests.post(url=SHEETY_ENDPOINT, json=sheety_params)
print(sheety_r.text)'''

#BASIC AUTH
sheety_r = requests.post(url=SHEETY_ENDPOINT, json=sheety_params, auth=(USERNAME, PASSWORD))
print(sheety_r.text)