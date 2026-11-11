def test_create_booking(api, booking_data):
    resp = api.create_booking(booking_data)

    assert resp.status_code == 200
    assert "bookingid" in resp.json()
    assert resp.json()["booking"] == booking_data


def test_get_booking(api, booking_id, booking_data):
    resp = api.get_booking(booking_id)

    assert resp.status_code == 200
    assert resp.json() == booking_data


def test_partial_update_booking(api, booking_id, booking_data, token):
    changes = {"firstname": "Alexander", "totalprice": 500}

    resp = api.partial_update_booking(booking_id, changes, token)

    assert resp.status_code == 200
    assert api.get_booking(booking_id).json() == {**booking_data, **changes}


def test_delete_booking(api, booking_id, token):
    resp = api.delete_booking(booking_id, token)

    assert resp.status_code == 201
    assert api.get_booking(booking_id).status_code == 404


def test_partial_update_with_invalid_token(api, booking_id, booking_data):
    resp = api.partial_update_booking(booking_id, {"firstname": "Hacker"}, "invalid_token")

    assert resp.status_code == 403
    assert api.get_booking(booking_id).json() == booking_data
