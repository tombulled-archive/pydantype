import pydantic

from typing import \
(
    Optional,
    List,
)

class BaseModel(pydantic.BaseModel): pass

class Validator(BaseModel):
    types: Optional[List[type]]
