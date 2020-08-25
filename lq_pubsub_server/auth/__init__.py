import secrets

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from lq_pubsub_server.configs import config
from lq_pubsub_server.models.provider import Provider

security = HTTPBearer()
security_optional = HTTPBearer(auto_error=False)


def check_management_privilege(required: bool = False):
    def func(credentials: HTTPAuthorizationCredentials = Depends(security if required else security_optional)):
        if credentials is None:
            return False
        if not secrets.compare_digest(credentials.credentials, config.secrets.management):
            if required:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="You are not privileged to access the data.",
                    headers={"WWW-Authenticate": "Bearer"}
                )
            return False
        return True

    return func


def check_provider_token(required: bool = False):
    def func(credentials: HTTPAuthorizationCredentials = Depends(security if required else security_optional)):
        if credentials is None:
            return None
        # TODO return the matched provider
        return Provider(name="demo", topics=[])

    return func
