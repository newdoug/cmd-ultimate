from abc import ABC, abstractmethod


class Validator(ABC):
    """
    Base validation class
    """
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def validate(self) -> None:
        raise NotImplementedError()

    def validate_multiple(self, config_dict: dict) -> None:
        pass
