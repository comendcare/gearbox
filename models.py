from pydantic import BaseModel, Field, field_validator
from typing import Optional, List, Any
from enum import Enum


class TaskEnum(str, Enum):
    translation = "TRANSLATION"
    illustration = "ILLUSTRATION"
    assistant = "ASSISTANT"
    file = "FILE"
    question_and_answer = "Q&A"


class FilePurposeEnum(str, Enum):
    finetune = "FINETUNE"
    assistant = "ASSISTANT"


class AudienceEnum(str, Enum):
    family = "FAMILY"
    scientist = "SCIENTIST"
    industry = "INDUSTRY"
    donor = "DONOR"
    wikipedia = "WIKIPEDIA"
    socials = "SOCIALS"


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

class StyleEnum(str, Enum):
    any = "ANY"
    vector = "VECTOR"
    realistic = "REALISTIC"
    artistic = "ARTISTIC"


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
    style: StyleEnum
    num_illustrations: int = Field(..., ge=1, le=10)
    image_size: ImageSizeEnum


class AssistantConfigData(BaseModel):
    assistant_name: str
    assistant_description: str
    instructions: str
    file_ids: List[str]


class FileConfigData(BaseModel):
    # To check what kind of file action is being requested by the client and that the appropriate data is provided.

    action: str
    file_id: Optional[str] = None
    file: Optional[Any] = None
    purpose: FilePurposeEnum

    @field_validator('action')
    def validate_action(cls, v):
        if v not in ['create', 'read', 'delete']:
            raise ValueError('Invalid action')
        return v

    @field_validator('file')
    def validate_file(cls, v, values, **kwargs):
        action = values.data.get("action")
        if action == 'create' and not v:
            raise ValueError('File object must be provided for create action')
        if not hasattr(v, "read"):
            raise ValueError("File must be a file-like object")
        return v

    @field_validator('file_id')
    def validate_file_id(cls, v, values, **kwargs):
        action = values.data.get("action")
        if action in ['read', 'delete'] and not v:
            raise ValueError('file_id must be provided for read or delete action')
        return v


class TranslateModel(BaseModel):
    task: TaskEnum
    data: TranslationConfigData


class IllustrateModel(BaseModel):
    task: TaskEnum
    data: IllustrationConfigData


class AssistantModel(BaseModel):
    task: TaskEnum
    data: AssistantConfigData


class FileModel(BaseModel):
    task: TaskEnum
    data: FileConfigData
