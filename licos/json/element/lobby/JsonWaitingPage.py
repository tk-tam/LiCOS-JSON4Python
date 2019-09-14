import licos.json.element.lobby
import jsons
from typing import List
from dataclasses import dataclass


@dataclass
class JsonWaitingPage(
        type: str,
        village: JsonVillage,
        players: Seq[JsonPlayerForWaitingPage],
        error: str,
        TypeSystem(type)):

    def _validType -> str:
        return JsonWaitingPage.type


class JsonWaitingPage:

    type: str = "waitingPage"

    def generate(
            village: JsonVillage,
            players: Seq[JsonPlayerForWaitingPage],
            error: str):
        return JsonWaitingPage(type, village, players, error)


@dataclass
class JsonPlayerForWaitingPage(
    token: str,
    name: str,
    avatarImage: str,
    isAnonymous: bool,
    isHost: bool,
    isMe: bool)


class JsonPlayerForWaitingPage:
