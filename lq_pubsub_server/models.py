from typing import List, Optional, TypeVar

from pydantic import BaseModel, UUID5, UUID4, root_validator
from enum import Enum

SubscriptionID = TypeVar("SubscriptionID", bound=UUID4)
MessageID = TypeVar("MessageID", bound=UUID4)
TopicID = TypeVar("TopicID", bound=UUID5)


class SubscriptionMode(str, Enum):
    push: "push"
    pull: "pull"


class Subscription(BaseModel):
    _id: SubscriptionID
    mode: SubscriptionMode
    queue: List[MessageID]
    push_ep: Optional[str]

    @root_validator
    def check_push_ep(cls, obj):
        if obj.get("mode") == SubscriptionMode.push and obj.get("push_ep") is None:
            raise ValueError("Missing field: push_ep.")
        return obj


class TopicName(BaseModel):
    default: str

    @root_validator
    def check_lang(cls, obj):
        default_lang = obj["default"]
        if default_lang == "default" or default_lang not in obj:
            raise ValueError(f"Default language can't be '{default_lang}'.")
        return obj


class Topic(BaseModel):
    _id: TopicID
    token: str
    name: TopicName


class Message(BaseModel):
    _id: MessageID
    topic: TopicID
    data: str
    attrs: dict
