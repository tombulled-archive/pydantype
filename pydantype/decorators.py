import functools
from . import models

from typing import \
(
    Callable,
    Any,
)

def validator(*types: type) -> Callable:
    def decorator(func: Callable) -> classmethod:
        @functools.wraps(func)
        def wrapper(cls: type, value: Any) -> Any:
            return func(cls, value)

        wrapper.validator = models.Validator \
        (
            types = types,
        )

        return classmethod(wrapper)

    return decorator
