from enum import Enum
from typing import List, Optional

from pydantic.class_validators import root_validator
from pydantic.main import BaseModel

from .types import MessageID, SubscriptionID


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
