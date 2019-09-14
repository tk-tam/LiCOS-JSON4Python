import licos.json.element.lobby
import jsons
from typing import List
from dataclasses import dataclass


@dataclass
class JsonPing(
        type: str,
        id: str,
        results: Seq[JsonPingResult],
        TypeSystem(type)):

    def _validType -> str:
        return Jsonping.type


class JsonPing:

    type: str = "ping"


@dataclass
class JsonPingResult(
        type: str,
        ping: str,
        status: str):


class JsonPingResult:
