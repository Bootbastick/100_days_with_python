import requests
import datetime
import math
from pprint import pprint

class FlightData:
    def __init__(self):
        self.tequila_endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.headers = {
            "apikey": "ZO6Cl0bMmjEO4Ft-GiHsCvz1julcBfAj"
        }
        self.stopovers = 1
        self.via_city = ""
    def search_for_no_stopovers_flights(self, city_code_from, city_code_to, sheet_data):
        plus_six_month_int = int(datetime.datetime.now().strftime('%m')) + 6
        year_in_date_to = int(datetime.datetime.now().strftime('%Y'))
        if plus_six_month_int > 12:
            plus_six_month_int -= 12
            year_in_date_to += 1
        for city in sheet_data:
            if city["iataCode"] == city_code_to:
                city_to_lowest_price = int(math.floor(float(city["lowestPrice"])))
        self.params = {
            "fly_from": city_code_from,
            "fly_to": city_code_to,
            "date_from": f"{int(datetime.datetime.now().strftime('%d')) + 1}/{datetime.datetime.now().strftime('%m')}/{datetime.datetime.now().strftime('%Y')}",
            "date_to": f"{int(datetime.datetime.now().strftime('%d')) + 1}/{plus_six_month_int}/{year_in_date_to}",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "adults": 1,
            "children": 0,
            "infants": 0,
            "curr": "EUR",
            "price_to": city_to_lowest_price,
            "max_stopovers": 0
        }
        # print(self.params)
        response = requests.get(url=self.tequila_endpoint, params=self.params, headers=self.headers)
        # print(response.text)
        self.all_data = response.json()

        try:
            self.data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {city_code_to}.")
            return None
        else:
            return True

    def search_for_num_of_stopover_flights(self, city_code_from, city_code_to, sheet_data, stopovers=1, via_city=""):
        plus_six_month_int = int(datetime.datetime.now().strftime('%m')) + 6
        year_in_date_to = int(datetime.datetime.now().strftime('%Y'))
        if plus_six_month_int > 12:
            plus_six_month_int -= 12
            year_in_date_to += 1
        for city in sheet_data:
            if city["iataCode"] == city_code_to:
                city_to_lowest_price = int(math.floor(float(city["lowestPrice"])))
        self.params = {
            "fly_from": city_code_from,
            "fly_to": city_code_to,
            "date_from": f"{int(datetime.datetime.now().strftime('%d')) + 1}/{datetime.datetime.now().strftime('%m')}/{datetime.datetime.now().strftime('%Y')}",
            "date_to": f"{int(datetime.datetime.now().strftime('%d')) + 1}/{plus_six_month_int}/{year_in_date_to}",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "adults": 1,
            "children": 0,
            "infants": 0,
            "curr": "EUR",
            "price_to": city_to_lowest_price,
            "max_stopovers": 1
        }
        # print(self.params)
        response = requests.get(url=self.tequila_endpoint, params=self.params, headers=self.headers)
        # print(response.text)
        self.all_data = response.json()

        try:
            self.data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {city_code_to}.")
            return None
        else:
            if stopovers != self.stopovers:
                self.stopovers = stopovers
            if via_city != self.data["route"][0]["cityTo"]:
                via_city = self.data["route"][0]["cityTo"]
                self.via_city = via_city
            else:
                self.via_city = via_city
            self.origin_city = self.data["route"][0]["cityFrom"],
            self.origin_airport = self.data["route"][0]["flyFrom"],
            self.destination_city = self.data["route"][1]["cityTo"],
            self.destination_airport = self.data["route"][1]["flyTo"],
            self.out_date = self.data["route"][0]["local_departure"].split("T")[0],
            self.return_date = self.data["route"][2]["local_departure"].split("T")[0]
            return True
