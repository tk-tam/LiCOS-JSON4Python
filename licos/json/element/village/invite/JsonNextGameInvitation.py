import licos.json.element.village.invite

import licos.json.element.lobby.TypeSystem

from dataclasses import dataclass

@dataclass
class JsonNextGameInvitation(
    type: str,
    villageId: long,
    TypeSystem(type)):

    def _validType -> str:
        return JsonNextGameInvitation.type

    def __init__(villageId: long,
                 JsonNextGameInvitation.type):
        pass


class JsonNextGameInvitation:

    type: str = "nextGameInvitation"
