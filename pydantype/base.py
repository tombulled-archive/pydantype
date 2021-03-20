import functools

from typing import \
(
    Any,
)

class BaseType(object):
    def __new__(cls, value, *, validated: bool = False):
        return super().__new__ \
        (
            cls,
            value if validated else cls.validate(value),
        )

    def __repr__(self):
        return f'{self.__class__.__name__}({super().__repr__()})'

    @classmethod
    def new(cls, *args, **kwargs):
        return cls.__new__(cls, *args, **kwargs)

    @classmethod
    def validate(cls, value: Any):
        return functools.reduce \
        (
            lambda value, validator: validator(value),
            cls.__get_validators__(),
            value,
        )

    @classmethod
    def __get_validators__(cls):
        def validate(value):
            if type(value) == cls:
                return value

            validators = tuple \
            (
                method
                for attribute_name in dir(cls)
                if (method := getattr(cls, attribute_name, None))
                if (validator := getattr(method, 'validator', None))
                if not validator.types or type(value) in validator.types
            )

            if not validators:
                raise TypeError(f'No validators found for type: {type(value)}')

            return functools.reduce \
            (
                lambda value, validator: validator.__func__(cls, value),
                validators,
                value,
            )

        yield validate
