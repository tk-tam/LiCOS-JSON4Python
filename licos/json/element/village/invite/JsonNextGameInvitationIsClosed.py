import licos.json.element.village.invite

import licos.json.element.lobby.TypeSystem

from typing import List
from dataclasses import dataclass

@dataclass
class JsonNextGameInvitationIsClosed(type: str, TypeSystem(type)):

    def _validType -> str:
        return JsonNextGameInvitationIsClosed.type

    def __init__(self, JsonNextGameInvitationIsClosed.type):
        pass

class JsonNextGameInvitationIsClosed:

    type : str = "nextGameInvitationIsClosed"