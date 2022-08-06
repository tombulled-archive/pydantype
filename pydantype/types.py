from typing import Any, Union

import humanize

from . import base, decorators


class BaseBuiltinType(base.BaseType):
    @decorators.validator()
    def validate_any(cls, value: Any):
        return cls.new(value)


class String(BaseBuiltinType, str):
    pass


class Float(BaseBuiltinType, float):
    pass


class Integer(BaseBuiltinType, int):
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({humanize.intcomma(int(self))})"


class Boolean(base.BaseType):
    def __new__(cls, value, *, validated: bool = False):
        return cls.validate(value)

    @decorators.validator(bool, int)
    def validate_truthy(cls, value: Union[bool, int]) -> bool:
        return bool(value)

    @decorators.validator(str)
    def validate_str(cls, value: str) -> bool:
        value = value.lower()

        values = {
            True: (
                "true",
                "t",
                "1",
                "on",
                "yes",
                "y",
            ),
            False: (
                "false",
                "f",
                "0",
                "off",
                "no",
                "n",
            ),
        }

        for bool_value, cases in values.items():
            if value in cases:
                return bool_value

        raise ValueError("Unable to parse value as a boolean")
