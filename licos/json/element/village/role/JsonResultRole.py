import licos.json.element.village.role


# import java.util.list ??

import licos.bson.element.village.BsonName
import licos.bson.element.village.agent.BsonSimpleAgent
import licos.bson.element.village.role.BsonResultRole
import licos.bson.element.village.JsonName
import licos.json.element.village.agent.JsonSimpleAgent
import licos.json.element.village.iri.RoleContext
import org.bson.types.ObjectId
#import play.api.libs.json.{Json,0Format}

import jsons
from typing import List
from dataclasses import dataclass


@dataclass
class JsonResultRole(
    @context: str,
    @id: str,
    isMine: bool,
    name: JsonName,
    image: str,
    numberOfAgents: int,
    agent: Seq[JsonSimpleAgent]
    JsonAbstractRole(
        @context: str,
        @id: str,
        name: JsonName,
        image: str)):

    def __init__(
        self,
        @id: str,
        isMine: bool,
        name: JsonName,
        image: str,
        numberOfAgents: int,
        agent: seq[JsonSimpleAgent]):
        pass
