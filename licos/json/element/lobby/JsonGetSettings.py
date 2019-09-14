import licos.json.element.lobby
import jsons
from typing import List
from dataclasses import dataclass


@dataclass
class JsonGetSettings(
        type: str,
        TypeSystem(type)):

    def _validType -> str:
        return JsonGetSettings.type


class JsonGetSettings:

    type: str = "getSettings"
