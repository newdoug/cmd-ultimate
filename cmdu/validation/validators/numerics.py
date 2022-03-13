from cmdu.validation import limits
from cmdu.validation.base import Validator
from cmdu.validation.exception import ValidationError
from cmdu.validation.validators.types import TypeValidator


class IntRangeValidator(Validator):
    def __init__(self, value, low=None, high=None):
        super().__init__(value)
        self.low = low
        self.high = high

    def validate(self):
        TypeValidator(self.value, [int]).validate()
        if self.low is not None and self.high is not None:
            if not (self.low < self.value < self.high):
                raise ValidationError("Value was '{}', must be in range [{}, {}]"
                                      .format(self.value, self.low, self.high))
        elif self.high is not None:
            if self.value > self.high:
                raise ValidationError("Value '{}' must be <= '{}'".format(self.value, self.high))
        elif self.low is not None:
            if self.value < self.low:
                raise ValidationError("Value '{}' must be >= '{}'".format(self.value, self.low))
        else:
            # both are None
            raise ValidationError("Invalid validator. One of low or high must be provided")


class Int64Validator(IntRangeValidator):
    def __init__(self, value):
        super().__init__(value, limits.MIN_INT64, limits.MAX_INT64)


class UInt64Validator(IntRangeValidator):
    def __init__(self, value):
        super().__init__(value, limits.MIN_UINT64, limits.MAX_UINT64)


class Int32Validator(IntRangeValidator):
    def __init__(self, value):
        super().__init__(value, limits.MIN_INT32, limits.MAX_INT32)


class UInt32Validator(IntRangeValidator):
    def __init__(self, value):
        super().__init__(value, limits.MIN_UINT32, limits.MAX_UINT32)


class Int16Validator(IntRangeValidator):
    def __init__(self, value):
        super().__init__(value, limits.MIN_INT16, limits.MAX_INT16)


class UInt16Validator(IntRangeValidator):
    def __init__(self, value):
        super().__init__(value, limits.MIN_UINT16, limits.MAX_UINT16)


class Int8Validator(IntRangeValidator):
    def __init__(self, value):
        super().__init__(value, limits.MIN_INT8, limits.MAX_INT8)


class UInt8Validator(IntRangeValidator):
    def __init__(self, value):
        super().__init__(value, limits.MIN_UINT8, limits.MAX_UINT8)
