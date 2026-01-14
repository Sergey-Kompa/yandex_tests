import requests

BASE_URL = "https://7581c5c4-db3b-4d53-a988-65de7ac2b709.serverhub.praktikum-services.ru"

ORDER_BODY = {
    "firstName": "Тест",
    "lastName": "Тестович",
    "address": "ул. Тестовая, 10",
    "metroStation": 1,
    "phone": "+79001234567",
    "rentTime": 3,
    "deliveryDate": "2026-01-20",
    "comment": "Автотестовый заказ",
    "color": ["BLACK"]
}

def test_create_order_and_get_by_track():
    response = requests.post(
        f"{BASE_URL}/api/v1/orders",
        json=ORDER_BODY
    )

    assert response.status_code == 201

    track = response.json().get("track")
    assert track is not None

    get_response = requests.get(
        f"{BASE_URL}/api/v1/orders/track",
        params={"t": track}
    )

    assert get_response.status_code == 200
    assert "order" in get_response.json()

