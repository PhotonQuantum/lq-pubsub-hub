from pydantic.main import BaseModel

from .types import MessageID, TopicID


class Message(BaseModel):
    _id: MessageID
    topic: TopicID
    data: str
    attrs: dict
