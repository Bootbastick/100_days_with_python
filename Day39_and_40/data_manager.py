import requests

class DataManager:
    def update_destination_codes(self, sheet_data):
        num = 1
        for city in sheet_data:
            self.sheety_put_endpoint = f"https://api.sheety.co/adfaef3244af72cadb214dff0018b1a8/flightDeals/prices/{num + 1}"
            num += 1
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            # response = requests.put(
            #     url=self.sheety_put_endpoint,
            #     json=new_data
            # )
