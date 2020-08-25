import uuid
from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic.class_validators import root_validator
from pydantic.fields import Field
from pydantic.main import BaseModel
from pydantic.networks import AnyHttpUrl

from .types import MessageID, SubscriptionID, TopicID


class SubscriptionMode(str, Enum):
    push: "push"
    pull: "pull"


class SubscriptionAttrs(BaseModel):
    push_accepted: Optional[bool]
    next_push: Optional[datetime]


class InputSubscription(BaseModel):
    topic: TopicID
    mode: SubscriptionMode
    queue: List[MessageID]
    push_endpoint: Optional[AnyHttpUrl]

    @root_validator
    def check_push_ep(cls, obj):
        if obj["mode"] == SubscriptionMode.push and obj.get("push_endpoint") is None:
            raise ValueError("Missing field: push_endpoint.")
        return obj


class Subscription(InputSubscription):
    _id: SubscriptionID = Field(default_factory=uuid.uuid4)
    last_active: datetime = Field(default_factory=datetime.now)
    attrs: SubscriptionAttrs

    class Config:
        json_encoders = {
            datetime: lambda dt: dt.timestamp()
        }
