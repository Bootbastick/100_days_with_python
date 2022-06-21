import requests

class FlightSearch:
    def city_name_to_iata_code(self, city_name):
        code_dict = {}
        headers = {
            "apikey": "ZO6Cl0bMmjEO4Ft-GiHsCvz1julcBfAj"
        }
        params = {
            "term": city_name,
            "location_types": "city"
        }
        self.kiwi_tequila_flight_search_api = "https://tequila-api.kiwi.com/locations/query"
        response = requests.get(url=self.kiwi_tequila_flight_search_api, params=params, headers=headers)
        # print(response.json())
        return response.json()["locations"][0]["code"]
