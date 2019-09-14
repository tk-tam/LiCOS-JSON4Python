import licos.json.element.lobby
import jsons
from typing import List
from dataclasses import dataclass


@dataclass
class JsonChangeLang(
        type: str,
        lang: str,
        TypeSystem(type)):

    def _validType -> str:
        return JsonChangeLang.type


class JsonChangeLang():

    type: str = "changeLang"
