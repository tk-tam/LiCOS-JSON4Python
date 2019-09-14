import licos.json.element.lobby
from typing import List


class TypeSystem(type: str):

    @abstractmethod
    def _validType -> str:
        pass

        def isValid　-> str:
            return type == _validType
