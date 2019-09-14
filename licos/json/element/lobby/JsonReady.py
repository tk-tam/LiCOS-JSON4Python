import licos.json.element.lobby
import jsons
from typing import List
from dataclasses import dataclass


@dataclass
class JsonReady(
        type: str,
        token: str,
        villageId: long,
        TypeSystem(type)):

    def _validType -> str:
        return JsonReady.type


class JsonReady:

    type: str = "ready"
