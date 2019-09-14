import licos.json.element.lobby
import jsons
from typing import List
from dataclasses import dataclass


@dataclass
class JsonPong(
        type: str,
        token: str,
        id: str,
        TypeSystem(type)):

    def _validType -> str:
        return "type"


class JsonPong:
    type: str = "pong"
