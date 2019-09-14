import licos.json.element.village.role

import licos.json.element.village.iri.RoleContext
import licos.json.element.village.JsonBoardPolarity
import licos.json.element.village.JsonName

import jsons
from typing import List
from dataclasses import dataclass

@dataclass
class JsonRole(
    @context: str,
    @id: str,
    name: JsonName,
    image: str,
    isMine: bool,
    numberOfCharacters: int,
    board: seq[JsonBoardPolarity],
    JsonAbstractRole(
        @context: str,
        @id: str,
        name: JsonName,
        image: str)):
