import licos.json.element.lobby
import jsons
from typing import List
from dataclasses import dataclass


@dataclass
class JsonEnterLobby(
        type: str,
        token: str,
        lobby: str,
        page: int,
        TypeSystem(type)):

    def _validType -> str:
        return JsonEnterLobby.type


class JsonEnterLobby:

    type: str = "enterLobby"
