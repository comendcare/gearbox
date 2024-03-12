from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class TaskEnum(str, Enum):
    translation = "TRANSLATION"
    illustration = "ILLUSTRATION"
    question_and_answer = "Q&A"


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


class ImageSizeEnum(str, Enum):
    square = "SQUARE"
    vertical = "VERTICAL"
    horizontal = "HORIZONTAL"


class TranslationConfigData(BaseModel):
    user_text: str
    preset: Optional[PresetEnum] = None
    audience: Optional[AudienceEnum]
    temperature: float
    readability: float
    max_tokens: int
    tone: ToneEnum


class IllustrationConfigData(BaseModel):
    model_name: str
    prompt: str
    num_illustrations: int = Field(..., ge=0, le=10)
    image_size: ImageSizeEnum


class TranslateModel(BaseModel):
    task: TaskEnum
    data: TranslationConfigData

class IllustrateModel(BaseModel):
    task: TaskEnum
    data: IllustrationConfigData
