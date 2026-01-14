from sender_stand_request import create_order, get_order_by_track
from data import order_data


def test_create_order_and_get_by_track():
    create_response = create_order(order_data)
    assert create_response.status_code == 201

    track = create_response.json()["track"]
    get_response = get_order_by_track(track)

    assert get_response.status_code == 200