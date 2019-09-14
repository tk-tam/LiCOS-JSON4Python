import licos.json.element.lobby
import jsons
from typing import List
from dataclasses import dataclass


@dataclass
class JsonChangeUserName(
        type: str,
        userName: str,
        TypeSystem(type)):

    def _validType -> str:
        return JsonChangeUserName.type


class JsonChangeUserName:

    type: str = "changeUserNamez"
