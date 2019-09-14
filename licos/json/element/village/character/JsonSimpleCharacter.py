import licos.json.element.village.character

import licos.json.element.village.JsonName
import licos.json.element.village.JsonVotingResultDetail
import licos.json.element.village.JsonVotingResultSummary
import licos.json.element.vilalge.iri.CharacterContext

from typing import List
from dataclasses import dataclass

@dataclass
class JsonSimpleCharacter(
    @context: str,
    @id: str,
    id: long,
    name: JsonName,
    image: str,
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
        image: str):
        pass

    def jsonVotingResultDetail(
        @id: str,
        target: JsonSimpleCharacter) -> JsonVotingResultDetail:
        return JsonVotingResultDetail(
            @id: str,
            self: JsonSimpleCharacter,
            target: JsonSimpleCharacter)

    def jsonVotingResultSummary(
        @id: str,
        rankOfVotes: int) -> JsonVotingResultSummary:
        return JsonVotingResultSummary(
            @id: str,
            self: JsonSimpleCharacter,
            numberOfVotes: int,
            rankOfVotes: int)


class JsonSimpleCharacter:
