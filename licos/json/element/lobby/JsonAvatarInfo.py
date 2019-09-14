import licos.json.element.lobby
import jsons
from typing import List
from dataclasses import dataclass


@dataclass
class JsonAvatarInfo(
        type: str,
        token: str,
        name: str,
        image: str,
        lang: str,
        TypeSystem(type)):

    def _validType -> str:
        return "getAvatar"


class JsonAvatarInfo:

    type: str = "avatar"

    def generate(
            token: str,
            name: str,
            image: str,
            lang: str):
        return JsonAvatarInfo(type, token, name, image, lang)


@dataclass
class JsonGetAbatarInfo(
        type: str,
        token: str,
        TypeSystem(type)):

    def _validType -> str:
        return "getAvatar"
