import licos.json.element.lobby
import jsons
from typing import List
from dataclasses import dataclass


@dataclass
class JsonIdSearch(
        type: str,
        token: str,
        lobby: str,
        idForSearching: int,
        TypeSystem(type)):

    def _validType -> str:
        return JsonIdSearch.type


class JsonIdSearch:

    type: str = "idSearch"
