import licos.json.element.lobby
import jsons
from typing import List
from dataclasses import dataclass


@dataclass
class JsonSearchResult(
        type: str,
        villages: Seq[JsonVillage],
        error: Optional[str],
        TypeSystem(type)):

    def _validType -> str:
        return JsonSearchResult.type


class JsonSearchResult:

    type: str = "searchResult"

    def generate(
            villages: Seq[JsonVillage],
            error: Optional[str]):

        return JsonSearchResult(type, villages, error)
