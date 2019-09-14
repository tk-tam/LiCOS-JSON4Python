import licos.json.element.lobby
import jsons
from typing import List
from dataclasses import dataclass


@dataclass
class JsonSettings(
        type: str,
        userName: str,
        userEmail: str,
        lang: str,
        TypeSystem(type)):

    def _validType -> str:
        return JsonSetting.type


class JsonSettings:

    type: str = "settings"

    def generate(
            userName: str,
            userEmail: str,
            lang: str):

        return JsonSettings(type, userName, userEmail, lang)
