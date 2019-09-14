import licos.json.element.village.character

import licos.json.element.village.iri.CharacterContext
import licos.json.element.village.JsonName
import licos.json.element.village.JsonUpdate

from dataclasses import dataclass
from typing import List

@dataclass
class JsonCharacter(
    @context: str,
    @id: str,
    id: long,
    name: JsonName,
    image: str,
    isMine: bool,
    status: str,
    update: JsonUpdate,
    isAChoice: bool,
    JsonAbstractCharacter(
        @context: str,
        @id: str,
        id: long,
        name: JsonName,
        image: str)):

    def __init__(
        self,
        self.CharacterContext.iri: str = CharacterContext.iri,
        @context: str,
        @id: str,
        id: long,
        name: JsonName,
        image: str,
        isMine: bool,
        status: str,
        update: JsonUpdate,
        isAChoice: bool):
        pass





class JsonCharacter:
