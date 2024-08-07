import requests as req
from loguru import logger as log
from requests.exceptions import ConnectionError

from api.auth import authorization
from configs.env import API_URL
from schemes.parser_info import Parser


def get_parser_info(parser_id: int) -> Parser | None:
    try:
        data = req.get(
            f"{API_URL}/parser/{parser_id}",
            headers=authorization().model_dump(),
        )
    except Exception:
        return get_parser_info(parser_id)

    if data.status_code == 200:
        data = data.json()
        return Parser(
            id=data["id"],
            shop_id=data["shop_id"],
            status=data["status"],
            command=data["command"],
            last_parsed=data["last_parsed"],
            frequency=data["frequency"],
            auth_cookie=data["auth_cookie"],
            cookie_edited=data["cookie_edited"]
        )
    return None


def update_parser_command_to_default(parser_id: int):
    try:
        data = req.put(
            f"{API_URL}/parser/",
            headers=authorization().model_dump(),
            json={
                "id": parser_id,
                "command": 0,
            }
        )
    except ConnectionError:
        return update_parser_command_to_default(parser_id)
    if data.status_code != 200:
        log.error(f"Error with updating "
                  f"parser status to default"
                  f"Status code: {data.status_code}"
                  f"Text: {data.text}"
                  )
