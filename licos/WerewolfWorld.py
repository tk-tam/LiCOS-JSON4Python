import licos
from typing import List

class WerewolfWorld:

    __baseUrl: str = "https://werewolf.world"
    __version: str = "0.2"

    def context(jsonldFileName: str) -> str:
        return '%s/context/%s/$%s.jsonld' % (
            __baseUrl, __version, jsonldFileName)

    stateVillage = 'https://licos.online/state/%s/vilage' % (__version)

    def state(path: str) -> str:
        return stateVillage.concat(path)
