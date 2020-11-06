# pylint: disable=missing-module-docstring,missing-class-docstring
from typing import Optional

from pydantic import BaseModel, Field  # pylint: disable=no-name-in-module

import uuid


# pylint: disable=too-few-public-methods
class Task(BaseModel):
    description: Optional[str] = Field(
        'no description',
        title='Task description',
        max_length=1024,
    )
    completed: Optional[bool] = Field(
        False,
        title='Shows whether the task was completed',
    )

    user_uuid: Optional[str] = Field(
        "user_uuid",
        title='Task user owner',
        max_length=40,
    )


    class Config:
        schema_extra = {
            'example': {
                'description': 'Buy baby diapers',
                'completed': False,
                'user_uuid' : '4c7abd5a-d8d5-491f-abcf-f9379fc5d95d'
            }
        }

class User(BaseModel):
    name: Optional[str] = Field(
        'joseph',
        title='Name of the user',
        max_length=32
    )

