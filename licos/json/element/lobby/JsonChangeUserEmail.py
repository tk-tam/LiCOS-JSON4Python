import licos.json.element.lobby
import jsons
from typing import List
from dataclasses import dataclass


@dataclass
class JsonChangeUserEmail(
        type: str,
        userEmail: str,
        TypeSystem(type)):

    def _validType = > str:
        JsonChangeUserEmail.type


class JsonChangeUserEmail():

    type: str = "changeUserEmail"
