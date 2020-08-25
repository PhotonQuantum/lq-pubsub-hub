from pydantic.class_validators import root_validator
from pydantic.main import BaseModel

from .types import TopicID


class InputTopic(BaseModel):
    default: str

    @root_validator
    def check_lang(cls, obj):
        default_lang = obj["default"]
        if default_lang == "default" or default_lang not in obj:
            raise ValueError(f"Default language can't be '{default_lang}'.")
        return obj


class Topic(InputTopic):
    _id: TopicID
