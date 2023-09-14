import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
            return response.content  # Use .content to get bytes
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def load_json(self):
        try:
            response = self.get_response_body()
            if response:
                return json.loads(response.decode("utf-8"))
            else:
                return None
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None