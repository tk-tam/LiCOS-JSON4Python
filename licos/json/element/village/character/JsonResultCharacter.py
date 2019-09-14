import licos.json.element.village.character

import licos.json.element.village.iri.CharacterContext
import licos.json.element.village.role.JsonSimpleRole
import licos.json.element.village.JsonAvatar
import licos.json.element.village.JsonName

from dataclasses import dataclass
from typing import List

@dataclass
class JsonResultCharacter(
    @context: str,
    @id: str,
    id: long,
    name: JsonName,
    image: str,
    isMine: bool,
    role: JsonSimpleRole,
    status: str,
    result: str,
    avatar: JsonAvatar
    JsonAbstractCharacter(
        @context: str,
        @id: str,
        id: long,
        name: JsonName,
        image: str)):

    def __init__(
        self,
        self.CharacterContext.iri : str = CharacterContext.iri,
        @id: str,
        id: long,
        name: JsonName,
        image: str,
        isMine: bool,
        role: JsonSimpleRole,
        status: str,
        result: str,
        avatar: JsonAvatar):
        pass
