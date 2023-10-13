from pydantic import BaseModel
from enum import Enum


class ToneEnum(str, Enum):
    empathetic = "empathetic"
    informative = "informative"
    positive = "positive"
    realistic = "realistic"


class TaskData(BaseModel):
    user_text: str
    preset: str
    temperature: float
    readability: float
    max_tokens: int
    tone: ToneEnum


class TaskModel(BaseModel):
    type: str
    data: TaskData

