import licos.json.element.lobby
import jsons
from typing import List
from dataclasses import dataclass


@dataclass
class JsonLobby(
    type: str,
    lobby: str,
    villages: str,
    error: Optional[str],
    TypeSystem(type):

    def _validType -> str:
        return JsonLobby.type

class JsonLobby:

    type: str="lobby"

    def generate(
        lobby: str,
        village: Seq[JsonVillage],
        error: Optional[str]):

        return JsonLobby(type, lobby, village, error)
