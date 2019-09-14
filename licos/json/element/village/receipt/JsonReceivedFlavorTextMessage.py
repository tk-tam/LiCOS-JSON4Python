import licos.json.element.village.receipt

import licos.json.element.village.JsonFlavorText
from typing import List
from dataclasses import dataclass

@dataclass
class JsonReceivedFlavorTextMessage(
    type: str,
    token: str,
    villageId: long,
    phase: str,
    date: int,
    JsonReceivedMessage(type, token, villageId)):

    def _validType -> str:
        return JsonReceivedFlavorTextMessage.type

    def __init__(
        self,
        flavorText: JsonFlavorText,
        JsonReceivedFlavorTextMessage.type,
        flavorText.base.token,
        flavorText.base.village.id,
        flavorText.base.phase,
        flaborText.base.date):
        pass


class JsonReceivedFlavorTextMessage:

    type: str = "receivedFlavorTextMessage"
