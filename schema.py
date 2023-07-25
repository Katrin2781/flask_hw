from typing import Optional, Type, Union

import pydantic
from pydantic import BaseModel


class CreateAdverts(BaseModel):
    title_advert: str
    description: str
    user: str


class UpdateAdverts(BaseModel):
    title_advert: Optional[str]
    description: Optional[str]
    user: Optional[str]
