
from cmdu.validation.base import Validator
from cmdu.validation.exception import ValidationError


class TypeValidator(Validator):
    def __init__(self, value, valid_types):
        super().__init__(value)
        self.valid_types = valid_types

    def validate(self):
        if not isinstance(self.value, self.valid_types):
            raise ValidationError("Value was type '{}', but must be one of '{}'"
                                  .format(type(self.value), self.valid_types))
