import licos.json.element.village.iri

import licos.WerewolfWorld

from abc import ABCMeta, abstractmethod
from typing import List

class Message(label: str):
    @abstractmethod
    def iri(villageId: long) -> str:
        WerewolfWorld.state()


class BoardMessage(Enum, Message("board"))
class ChatMessage(Enum, Message("chat"))
class ErrorMessage(Enum, Message("error"))
class ScrollMessage(Enum, Message("scroll"))
class SystemMessage(Enum, Message("system"))
class VoteMessage(Enum, Message("vote"))
class FlavorText(Enum, Message("flavorText"))
class DummyMessage(Enum, Message("dummy"))
