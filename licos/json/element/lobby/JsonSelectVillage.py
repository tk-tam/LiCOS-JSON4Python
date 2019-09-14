import licos.json.element.lobby
import jsons
from typing import List
from dataclasses import dataclass


@dataclasses
class JsonSelectVillage(
        type: str,
        token: str,
        villageId: str,
        TypeSystem(type)):

    def _validType -> str:
        return JsonSelectVillage.type


class JsonSelectVillage:

    type: str = "selectVillage"
