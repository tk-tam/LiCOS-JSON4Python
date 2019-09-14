import licos.json.element.lobby
import jsons
from typing import List
from dataclasses import dataclass


@dataclass
class JsonAdvancedSearch(
        type: str,
        token: str,
        lobby: str,
        villageName: Optional[str],
        hostName: Optional[str],
        minimum: Optional[int],
        maximum: Optional[int]
        avatar: str,
        comment: Optional[str],
        TypeSystem(type)):

    def _validType -> str:
        return "advancedSearch"
