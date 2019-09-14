import licos.json.element.village.role

import licos.json.element.village.JsonName
import licos.json.element.village.iri.RoleContext

from typing import List
from dataclasses import dataclass

@dataclass
class JsonSimpleRole(
    @context: str,
    @id: str,
    name: JsonName,
    image: str,
    JsonAbstractRole(
        @context: str,
        @id: str,
        name: JsonName,
        image: str)):

    def __init__(
       @id: str,
       name: JsonName,
       image: str,
       ):
       self.@id = @id
       self.name = JsonName
       self.image = image
       self.RoleContext.iri = RoleContext.iri
