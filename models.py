from pydantic import BaseModel
from typing import Optional
from enum import Enum

class TaskEnum(str, Enum):
    translation = "TRANSLATION"


class AudienceEnum(str, Enum):
    family = "FAMILY"
    scientist = "SCIENTIST"
    industry = "INDUSTRY"
    investor = "INVESTOR"


class PresetEnum(str, Enum):
    simplify = "SIMPLIFY"
    terminology = "TERMINOLOGY"
    applications = "APPLICATIONS"
    optimistic = "OPTIMISTIC"
    analyzed = "ANALYZED"
    takeaways = "TAKEAWAYS"
    questions = "QUESTIONS"


class ToneEnum(str, Enum):
    empathetic = "EMPATHETIC"
    informative = "INFORMATIVE"
    positive = "POSITIVE"
    realistic = "REALISTIC"


class ConfigData(BaseModel):
    user_text: str
    preset: Optional[PresetEnum]
    audience: Optional[AudienceEnum]
    temperature: float
    readability: float
    max_tokens: int
    tone: ToneEnum


class TaskModel(BaseModel):
    task: TaskEnum
    data: ConfigData

