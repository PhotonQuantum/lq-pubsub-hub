import uuid
from typing import List, Optional

from fastapi import APIRouter, Depends, Query

from lq_pubsub_server.auth import check_management_privilege
from lq_pubsub_server.models.message import Message, MessageID
from lq_pubsub_server.models.subscription import InputSubscription, Subscription, SubscriptionAttrs, SubscriptionID, \
    SubscriptionMode

router = APIRouter()


# noinspection PyTypeChecker
@router.get("/", response_model=List[SubscriptionID])
async def get_all_subscriptions():
    return []


@router.post("/", response_model=SubscriptionID)
async def post_new_subscription(input_subscription: InputSubscription):
    return uuid.uuid4()


@router.get("/{subscription_id}", response_model=Subscription)
async def get_subscription_detail(subscription_id: SubscriptionID,
                                  management=Depends(check_management_privilege(required=True))):
    return Subscription(topic=uuid.uuid5(uuid.uuid4(), "test"), attrs=SubscriptionAttrs(), mode=SubscriptionMode.pull)


# noinspection PyTypeChecker
@router.get("/{subscription_id}/pull", response_model=List[Message])
async def pull_message(subscription_id: SubscriptionID, timeout: Optional[int] = Query(10, ge=0, le=30)):
    return []


# noinspection PyTypeChecker
@router.post("/{subscription_id}/ack")
async def ack_message(subscription_id: SubscriptionID, ack_ids: List[MessageID]):
    return


@router.delete("/{subscription_id}")
async def delete_subscription():
    return
