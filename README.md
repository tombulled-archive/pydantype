# pydantype
Custom validated types that work with pydantic

## Installation
The `innertube` library uses [Poetry](https://github.com/python-poetry/poetry) and can easily be installed from source, or using *pip*

### Using *pip* (from source)
```console
pip install git+https://github.com/tombulled/pydantype.git
```

## Usage
```python
>>> import pydantype
>>>
>>> # Use a provided type
>>> pydantype.Integer(187583583803)
Integer(187,583,583,803)
>>>
>>>
>>> # Create your own custom type
>>> class PositiveInteger(pydantype.Integer):
        @pydantype.validator()
        def validate_any(cls, value):
            value = cls.new(value)

            if value < 0:
                raise ValueError('Value must be positive (>= 0)')

            return value

>>>
>>> PositiveInteger(123)
PositiveInteger(123)
>>> PositiveInteger(-123)
ValueError: Value must be positive (>= 0)
>>>
>>> # Use with pydantic
>>> import pydantic
>>>
>>> class Model(pydantic.BaseModel):
        integer: PositiveInteger

>>>
>>> Model(integer = 123)
Model(integer=PositiveInteger(123))
>>> Model(integer = -123)
pydantic.error_wrappers.ValidationError: 1 validation error for Model
integer
  Value must be positive (>= 0) (type=value_error)
>>>
```
