import requests as req

from api.auth import authorization
from configs.env import API_URL
from schemes.order_item import GoodInOrder, GoodInOrderCreate


def good_in_order_by_order_id(order_id: int):
    list_of_goods_in_order = []
    response = req.get(
        f"{API_URL}/good_in_order/by_order_id/{order_id}",
        headers=authorization().model_dump(),
    )
    if response.status_code == 200:
        data = response.json()
        for good_in_order in data:
            list_of_goods_in_order.append(
                GoodInOrder(
                    id=good_in_order['id'],
                    order_id=good_in_order['order_id'],
                    good_id=good_in_order['good_id'],
                    quantity=good_in_order['quantity'],
                    amount=good_in_order['amount'],
                )
            )
        return list_of_goods_in_order
    return None


def create_good_in_order(good: GoodInOrderCreate) -> GoodInOrder | None:
    response = req.post(
        f"{API_URL}/good_in_order/",
        headers=authorization().model_dump(),
        json=good.model_dump()
    )
    if response.status_code == 200:
        data = response.json()
        return GoodInOrder(
            id=data['id'],
            order_id=data['order_id'],
            good_id=data['good_id'],
            quantity=data['quantity'],
            amount=data['amount'],
        )
    return None


def update_good_in_order(good: GoodInOrder) -> GoodInOrder | None:
    response = req.put(
        f"{API_URL}/good_in_order",
        headers=authorization().model_dump(),
        json=good.model_dump()
    )
    if response.status_code == 200:
        data = response.json()
        return GoodInOrder(
            id=data['id'],
            order_id=data['order_id'],
            good_id=data['good_id'],
            quantity=data['quantity'],
            amount=data['amount'],
        )
    return None
