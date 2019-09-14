import licos.json.element.lobby
import jsons
from typing import List
from dataclasses import dataclass


@dataclass
class JsonBuildVillage(
        type: str,
        token: str,
        name: str,
        id: long,
        idForSearching: long,
        hostPlayer: JsonHostPlayer,
        playerSetting: JsonPlayerSetting,
        roleSetting: JsonRoleSetting,
        avatar: str,
        comment: str,
        TypeSystem(type)):

    def _validType -> str:
        return "buildVillage"


class JsonBuildVillage():

    def __init__(self, type):
        self.type = type

    def generate(
            token: str,
            name: str,
            id: long,
            idForSearching: long,
            hostPlayer: JsonHostPlayer,
            playerSetting: JsonPlayerSetting,
            roleSetting: JsonRoleSetting,
            avatar: str,
            comment: str,):

        return JsonBuildVillage(
            type,
            token,
            name,
            id,
            idForSearching,
            hostPlayer,
            playerSetting,
            roleSetting,
            avatar,
            comment)
