from notification_manager import NotificationManager
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
import requests


sheety_flight_tracking_endpoint = "https://api.sheety.co/adfaef3244af72cadb214dff0018b1a8/flightDeals/prices"


sheety_user_tracking_endpoint = "https://api.sheety.co/adfaef3244af72cadb214dff0018b1a8/flightDeals/users"
response = requests.get(url=sheety_user_tracking_endpoint).json()
user_data = {'users': []}
add_a_row_endpoint = "https://api.sheety.co/adfaef3244af72cadb214dff0018b1a8/flightDeals/users"
print(user_data)

print("Welcome to Nick's flight club!")
print("We find the best flight deals and email you.")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
user_email = input("What is your email?\n")
user_email_validation = input("Type your email again.\n")
if user_email_validation == user_email:
    print("You're in the club!")
    text = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": user_email
        }
    }
    # response = requests.post(url=add_a_row_endpoint, json=text)
    # print(response.text)
else:
    print("Your email validation and email don't match.")
# sheet_data = requests.get(url=sheety_flight_tracking_endpoint).json()["prices"]
# print(sheet_data)
sheet_data = [{'city': 'Paris', 'iataCode': '', 'lowestPrice': '62.32', 'id': 2}, {'city': 'Berlin', 'iataCode': '', 'lowestPrice': '48.47', 'id': 3}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': '559.74', 'id': 4}, {'city': 'Sydney', 'iataCode': '', 'lowestPrice': '635.91', 'id': 5}, {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': '109.64', 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': '477.80', 'id': 7}, {'city': 'New York', 'iataCode': '', 'lowestPrice': '276.98', 'id': 8}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': '300.07', 'id': 9}, {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': '436.25', 'id': 10}, {"city": "Bali", "iataCode": "DPS", "lowestPrice": "583.63", "id": 11}]
list_of_cities = []
for i in range(len(sheet_data)):
    list_of_cities.append(sheet_data[i]["city"])
# print(sheet_data)
for a in range(len(sheet_data)):
    if sheet_data[a]["iataCode"] == "":
        fs = FlightSearch()
        for i in range(len(sheet_data)):
            sheet_data[i]["iataCode"] = fs.city_name_to_iata_code(sheet_data[i]["city"])
        # print(sheet_data)

dm = DataManager()
dm.update_destination_codes(sheet_data)

fd = FlightData()
flightFound = False
flight_with_stopover = False
nm = NotificationManager()
for city in sheet_data:
    if fd.search_for_no_stopovers_flights("TIV", city["iataCode"], sheet_data) != None:
        flightFound = True
        flight_with_stopover = False
    if fd.search_for_num_of_stopover_flights("TIV", city["iataCode"], sheet_data) != None:
        flightFound = True
        flight_with_stopover = True
    if flightFound is True and flight_with_stopover is True:
        price = fd.data["price"]
        curr = fd.all_data["currency"]
        text = f"Hello! We found a cheap flight! It's only for {price} {curr}! It's from {fd.data['cityFrom']}-{fd.data['flyFrom']} to {fd.data['cityTo']}-{fd.data['flyTo']}.\n\nFlight has {fd.stopovers} stopovers via {fd.via_city}."
        nm.send_notification(user_email, text)
    elif flightFound is True:
        price = fd.data["price"]
        curr = fd.all_data["currency"]
        text = f"Hello! We found a cheap flight! It's only for {price} {curr}! It's from {fd.data['cityFrom']}-{fd.data['flyFrom']} to {fd.data['cityTo']}-{fd.data['flyTo']}."
        nm.send_notification(user_email, text)
