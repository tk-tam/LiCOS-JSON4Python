import licos.json.element.lobby
import jsons
from typing import List
from dataclasses import dataclass


@dataclass
class JsonChangeUserPassword(
        type: str,
        userPassword: str,
        TypeSystem(type)):

    def _validType -> str:
        return JsonChangeUserPassword.type


class JsonChangeUserPassword:

    type: str = "changeUserPassword"
