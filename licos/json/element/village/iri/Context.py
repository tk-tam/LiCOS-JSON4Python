import licos.json.element.village.iri

import licos.WerewolfWorld

from enum import Enum
from abc import ABCMeta, abstractmethod
from typing import List

# sealed省いてます　方法https://blog.7nobo.me/2016/08/10/200000.htmlか？


class Context(label: str):
    @abstractmethod
    def iri -> str:
        return WerewolfWorld.context(label)


class BaseContext(Enum, Context("base"))
class ErrorContext(Enum, Context("error"))
class CharacterContext(Enum, Context("character"))
class AvatarContext(Enum, Context("avatar"))
class RoleContext(Enum, Context("role"))
class BoardContext(Enum, Context("board"))
class ChatContext(Enum, Context("chat"))
class VillageContext(Enum, Context("village"))
class VoteContext(Enum, Context("vote"))
class VotingResultContext(Enum, Context("votingResult"))
class scrollContext(Enum, Context("scroll"))
class FlavorTextContext(Enum, Context("flavorText"))
