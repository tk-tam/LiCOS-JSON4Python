import licos.json.element.village.character

import licos.json.element.village.JsonName
import licos.json.element.village.iri.CharacterContext
import licos.json.element.village.role.JsonSimpleRole


from typing import List
from dataclasses import dataclass

@dataclass
class JsonRoleCharacter(
    @context: str,
    @id: str,
    id: long,
    name: JsonName,
    image: str,
    role: JsonSimpleRole,
    JsonAbstractCharacter(
        @context: str,
        @id: str,
        id: long,
        name: JsonName,
        image:str)):

    def __init__(
        self,
        self.CharacterContext.iri: str = CharacterContext.iri
        @id: str,
        id: long,
        name: JsonName,
        image: str,
        role: JsonSimpleRole):
        pass


class JsonRoleCharacter:
