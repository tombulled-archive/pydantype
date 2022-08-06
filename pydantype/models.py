from typing import List, Optional

import pydantic


class BaseModel(pydantic.BaseModel):
    pass


class Validator(BaseModel):
    types: Optional[List[type]]
