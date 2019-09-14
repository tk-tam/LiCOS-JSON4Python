import licos.json.element.village.iri

from typing import List


class Contexts:
    def get(message: Message) -> seq[str]:
        if message == BoardMessage
            return list([BaseContext.iri, BoardContext.iri])
        elif message == ChatMeessage
            return list([BaseContext.iri, ChatContext.iri])
        elif message == ErrorMessage
            return list([BaseContext.iri, ErrorContext.iri])
        elif message == ScrollMessage
            return list([BaseContext.iri, ScrollContext.iri])
        elif message == SystemMessage
            return list([BaseContext.iri, VotingResultContext.iri])
        elif message == VoteMessage
            return list([BaseContext.iri, VoteContext.iri])
        elif message == FlavorTextMessage
            return list([BaseContext.iri, FlavorTextContext.iri])
        else message == DummyMessage
            return list([])
