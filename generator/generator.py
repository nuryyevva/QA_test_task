import logging
import random
import time

import httpx
from dotenv import dotenv_values
import json

config = dotenv_values("generator/.env")
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("httpx")


class SenderData:
    def __init__(self, sleep: int, username: str, password: str, url: str) -> None:
        self.url = url
        self.sleep = sleep
        self.username = username
        self.password = password

    @staticmethod
    def prepare_data_request() -> dict:
        return {
            "cam_id": random.randint(1, 99),
            "video_color": {
                "brightness": random.randint(0, 100),
                "contrast": random.randint(0, 100),
                "hue": random.randint(0, 100),
                "saturation": random.randint(0, 100),
            },
            "channel_no": random.randint(1, 2),
            "config_no": random.randint(0, 1),
        }

    def run(self) -> None:
        while True:
            data = self.prepare_data_request()
            path = f"{self.url}/api/v1/package/"
            with httpx.Client(auth=(self.username, self.password)) as client:
                response = client.post(path, json=data)
                try:
                    response = response.json()
                    logger.info(f"Response {response}")
                except json.decoder.JSONDecodeError:
                    logger.info(f"Не удалось распаковать ответ от сервиса. {response.content}")
            time.sleep(self.sleep)


data_for_sender: dict[str, int | str] = {
    "sleep": 1,
    "username": config.get("username"),
    "password": config.get("password"),
    "url": config.get("url"),
}
sender = SenderData(**data_for_sender)
sender.run()
