import licos.json.element.village

import jsons
from typing import List
from dataclasses import dataclass


@dataclass
class JsonAudienceChat(
    base: JsonBase,
    sub: JsonSubAudienceChat,
    JsonElement):

    def __init__(
        self,

        base:
    ):
        #mada

    def avatarOpt -> Optional[JsonAvatar]:
        return sub.avatar

    def isMine -> bool:
        return sub.isMine

    def text -> JsonChatText:
        return sub.text

    def characterLimit -> int:
        return sub.charaterLimit

    def isFromServer -> bool:
        return sub.isFromServer


@dataclass
class JsonSubAudienceChat(
    avatar: Optional[JsonAvatar],
    isMine: bool,
    text: JsonChatText,
    characterLimit: int,
    isFromServer: bool):
