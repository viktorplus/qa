import requests


class BookerApi:
    """Client for https://restful-booker.herokuapp.com, methods return the raw response"""

    def __init__(self, base_url="https://restful-booker.herokuapp.com"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})

    def get_token(self, username, password):
        resp = self.session.post(f"{self.base_url}/auth", json={"username": username, "password": password})
        return resp.json()["token"]

    def create_booking(self, booking):
        return self.session.post(f"{self.base_url}/booking", json=booking)

    def get_booking(self, booking_id):
        return self.session.get(f"{self.base_url}/booking/{booking_id}")

    def partial_update_booking(self, booking_id, data, token):
        return self.session.patch(f"{self.base_url}/booking/{booking_id}", json=data, cookies={"token": token})

    def delete_booking(self, booking_id, token):
        return self.session.delete(f"{self.base_url}/booking/{booking_id}", cookies={"token": token})
