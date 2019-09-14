import licos.json.element.village.receipt

import libos.json.element.village.JsonChatFromServer
from typing import List
from dataclasses import dataclass

@dataclass
class JsonReceivedPlayerMessage(
    type: str,
    token: str,
    villageId: long,
    serverTimestamp: str,
    clientTimestamp: str,
    JsonReceivedMessage(type, token, villageId)):

    def _validType -> str:
        return JsonReceivedPlayerMessage.type

    def __init__(
        self,
        chat: JsonChatFromServer,
        JsonReceivedPlayerMessage.types,
        chat.base.token,
        chat.base.village.id,
        chat.base.serverTimestamp,
        chat.base.clientTimestamp):
        pass


class JsonReceivedPlayerMessage:

    type: str = "receivedPlayerMessage"
