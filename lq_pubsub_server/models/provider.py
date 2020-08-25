import uuid
from datetime import datetime
from typing import List

from pydantic.fields import Field
from pydantic.main import BaseModel
from pydantic.types import UUID4

from .types import ProviderID, TopicID


class InputProvider(BaseModel):
    name: str
    topics: List[TopicID]


class DisplayProvider(InputProvider):
    _id: ProviderID = Field(default_factory=uuid.uuid4)
    last_active: datetime = Field(default_factory=datetime.now)

    class Config:
        json_encoders = {
            datetime: lambda dt: dt.timestamp()
        }


class Provider(DisplayProvider):
    token: UUID4 = Field(default_factory=uuid.uuid4)
