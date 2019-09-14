import licos.json.element.lobby
import jsons
from typing import List
from dataclasses import dataclass


@dataclass
class JsonPlayed(
        type: str,
        lang: str,
        TypeSystem(str)):

    def _validType -> str:
        return JsonPlayed.type


class JsonPlayed:

    def generate(lang: str):
        return JsonPlayed(type, lang)

    type: str = "played"
