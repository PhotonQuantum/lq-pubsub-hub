from typing import TypeVar

from pydantic.types import UUID4, UUID5

SubscriptionID = TypeVar("SubscriptionID", bound=UUID4)
MessageID = TypeVar("MessageID", bound=UUID4)
TopicID = TypeVar("TopicID", bound=UUID5)
