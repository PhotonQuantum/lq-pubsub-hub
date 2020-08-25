from fastapi import FastAPI
from .endpoints import subscription

app = FastAPI()
app.include_router(subscription.router, prefix="/subscriptions")