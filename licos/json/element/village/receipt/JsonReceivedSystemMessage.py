import licos.json.element.village.receipt

import licos.json.element.village.JsonPhase
from typing import List
from dataclasses import dataclass

@dataclass
class JsonReceivedSystemMessage(
    type: str,
    token: str,
    villageId: long,
    phase: str,
    date: int,
    JsonReceivedMessage(type, token, villageId)):

    def _validType -> str:
        return JsonReceivedSystemMessage.type

    def __init__(
        self,
        phase: JsonPhase,
        JsonReceivedSystemMessage.type,
        phase.base.token,
        phase.base.village.id,
        phase.base.phase,
        phase.base.date):
        pass


class JsonReceivedSystemMessage:

    type: str = "receivedSystemMessage"
