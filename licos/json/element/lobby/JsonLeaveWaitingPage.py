import licos.json.element.lobby
import jsons
from typing import List
from dataclasses import dataclass


@dataclass
class JsonLeaveWaitingPage(
        type: str,
        token: str,
        villageId: long,
        lobby: str,
        TypeSystem(type)):

    def _validType -> str:
        return JsonLeaveWaitingPage.type


class JsonLeaveWaitingPage:

    type: str = "leaveWaitingpage"
