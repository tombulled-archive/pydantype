import humanize

from . import base
from . import decorators

from typing import \
(
    Any,
)

class String(base.BaseType, str):
    @decorators.validator()
    def validate_any(cls, value: Any):
        return cls.new(value, validated = True)

class Integer(base.BaseType, int):
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({humanize.intcomma(int(self))})'

    @decorators.validator()
    def validate_any(cls, value: Any):
        return cls.new(value, validated = True)

class PositiveInteger(Integer):
    @decorators.validator()
    def validate_any(cls, value):
        value = cls.new(value, validated = True)

        if value < 0:
            raise ValueError('Value must be positive (>= 0)')

        return value
