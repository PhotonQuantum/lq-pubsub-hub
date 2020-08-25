from pydantic.main import BaseModel
from pydantic.networks import stricturl
from pydantic.types import constr


class MongodbConfig(BaseModel):
    uri: stricturl(allowed_schemes={"mongodb"}, tld_required=False)
    database: str


class SecretsConfig(BaseModel):
    management: constr(min_length=32, max_length=32)


class GlobalConfig(BaseModel):
    mongodb: MongodbConfig
    secrets: SecretsConfig
