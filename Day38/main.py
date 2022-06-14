import requests
import datetime

APP_ID = "application id"
APP_KEY = "application key"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_workout_tracking_endpoint = "https://api.sheety.co/adfaef3244af72cadb214dff0018b1a8/workoutTracking/лист1"
USERNAME = "username"
PASSWORD = "password"
MY_WEIGHT = "weight in kg in ints"
MY_HEIGHT = "height in cm in ints"
MY_AGE = "age in years in ints"


user_data = str(input("Tell me which exercises you did: "))

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

exercise_data = {
    "query": user_data,
    "gender": "male",
    "weight_kg": MY_WEIGHT,
    "height_cm": MY_HEIGHT,
    "age": MY_AGE
}

track_api_response = requests.post(url=exercise_endpoint, json=exercise_data, headers=headers)
track_api_response_json = track_api_response.json()
print(track_api_response_json)

sheet_data = requests.get(url=sheety_workout_tracking_endpoint, auth=(USERNAME, PASSWORD)).json()
num_of_rows = sheet_data["лист1"][0]["id"]
print(sheet_data)

today_date = datetime.datetime.now().strftime("%d/%m/%Y")
time_now = datetime.datetime.now().strftime("%X")
print(today_date, time_now)

new_row_data = {
    "лист1": {
        "date": today_date,
        "time": time_now,
        "exercise": track_api_response_json["exercises"][0]["name"],
        "duration": track_api_response_json["exercises"][0]["duration_min"],
        "calories": track_api_response_json["exercises"][0]["nf_calories"],
        "id": num_of_rows + 1
    }
}

new_row = requests.post(url=sheety_workout_tracking_endpoint, json=new_row_data, auth=(USERNAME, PASSWORD))
print(new_row.text)
