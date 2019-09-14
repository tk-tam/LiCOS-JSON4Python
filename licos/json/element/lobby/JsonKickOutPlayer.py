import licos.json.element.lobby
import jsons
from typing import List
from dataclasses import dataclass


@dataclass
class JsonKickOutPlayer(
        type: str,
        token: str,
        players: seq[JsonPlayerToken],  # 要確認
        TypeSystem(type)):

    def _validType -> type:
        return JsonKickOutPlayer.type


class JsonKickOutPlayer:

    type: str = "kickOutPlayer"


@dataclass
class JsonPlayerToken:


class JsonPlayerToken:
    # ? フォーマット？
