import licos.json.element.lobby
import jsons
from typing import List
from dataclasses import dataclass


@dataclass
class JsonVillage(
    name: str,
    id: long,
    idForSearching: long,
    hostplayer: JsonHostPlayer,
    playerSetting: JsonPlayerSetting,
    roleSetting: JsonRoleSetting,
    avatar: str,
    comment: str)


class JsonVillage:


@dataclass
class JsonHostPlayer(
    name: str,
    isAnonymous: bool,
    isHuman: bool)


class JsonHostPlayer:


@dataclass
class JsonPlayerSetting(
    number: int,
    current: int,
    robot: JsonRobot,
    human: JsonHuman)


class JsonPlayerSetting:


@dataclass
class JsonRobot(
    min: int,
    current: int)


class JsonRobot:


@dataclass
class JsonHuman(
    max: int,
    current: int)


class JsonHuman:


@dataclass
class JsonRoleSetting(
    villager: int,
    werewolf: int,
    seer: int,
    medium: int,
    madman: int,
    hunter: int,
    mason: int,
    werehamster: int)


class JsonRoleSetting:
