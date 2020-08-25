import uuid
from datetime import datetime

from pydantic.fields import Field
from pydantic.main import BaseModel

from .types import MessageID, TopicID


class InputMessage(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.now)
    data: str
    attrs: dict

    class Config:
        json_encoders = {
            datetime: lambda dt: dt.timestamp()
        }


class Message(InputMessage):
    _id: MessageID = Field(default_factory=uuid.uuid4)
    topic: TopicID
