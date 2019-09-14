import licos.json.element.village.character

import licos.json.element.village.iri.CharacterContext
import licos.json.element.village.role.JsonSimpleRole
import licos.json.element.village.JsonAvatar
import licos.json.element.village.JsonName

from typing import List
from dataclasses import dataclass

@dataclass
class JsonStatusCharacter(
    @context: str,
    @id: str,
    id: str,
    name: JsonName,
    image: str,
    role: JsonSimpleRole,
    status: str,
    avatar: JsonAvatar,
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
        role: JsonSimpleRole,
        status: str,
        avatar: JsonAvatar):
        pass


class JsonStatusCharacter:
