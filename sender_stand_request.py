import requests
import configuration


def create_order(order_body):
    return requests.post(
        configuration.BASE_URL + configuration.CREATE_ORDER_PATH,
        json=order_body
    )


def get_order_by_track(track):
    return requests.get(
        configuration.BASE_URL + configuration.GET_ORDER_PATH,
        params={"t": track}
    )