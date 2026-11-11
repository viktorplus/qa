import os
from pathlib import Path

import pytest
from dotenv import load_dotenv
from hw7.booker_api import BookerApi

# Credentials are read from hw7/.env (not committed to git). Create it with:
#   BOOKER_USERNAME=admin
#   BOOKER_PASSWORD=password123
# These are public demo credentials from https://restful-booker.herokuapp.com/apidoc/
load_dotenv(Path(__file__).parent / ".env")


@pytest.fixture
def api():
    return BookerApi()


@pytest.fixture
def token(api):
    return api.get_token(os.environ["BOOKER_USERNAME"], os.environ["BOOKER_PASSWORD"])


@pytest.fixture
def booking_data():
    return {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-12-01",
            "checkout": "2026-12-10"
        },
        "additionalneeds": "Breakfast"
    }


@pytest.fixture
def booking_id(api, booking_data):
    return api.create_booking(booking_data).json()["bookingid"]
