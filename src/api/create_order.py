import requests as req
from loguru import logger as log

from api.auth import authorization
from configs.env import API_URL
from schemes.order import Order


def create_order(order: Order) -> Order | None:
    try:
        response = req.post(
            f"{API_URL}/order/",
            headers=authorization().model_dump(),
            json=order.model_dump(),
        )
    except Exception:
        return create_order(order)

    if response.status_code != 200:
        log.error(f"""
            Some error when creating order.
            Order ID: {order.order_id}.
            Status code: {response.status_code}
            Details: {response.text}
        """)
        return None
    data = response.json()
    return Order(
        id=data['id'],
        status=data['status'],
        shop_id=data['shop_id'],
        order_id=data['order_id'],
        date=data['date'],
        quantity=data['quantity'],
        buyer_paid=data['buyer_paid'],
        tax=data['tax'],
        shipping=data['shipping'],
        purchased_after_ad=data['purchased_after_ad'],
        full_fee=data['full_fee'],
        profit=data['profit'],
    )
