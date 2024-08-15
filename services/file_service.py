import os
import openai

from builders.illustration_prompt_builder import IllustrationPromptBuilder
from services import AIService
from dotenv import load_dotenv
from builders.translation_prompt_builder import TranslationPromptBuilder
from config.logging_config import logger
from config.global_config import config
load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()


class FileService(AIService):
    def __init__(self):
        self.model_config = config["model_config"]

    def file_purpose_formatter(self, file_purpose):
        size_dict = {
            "ASSISTANT": "assistants",
            "FINETUNE": "fine-tune",
        }
        return size_dict[file_purpose]

    async def create_file(self, data):
        file = await openai.File.acreate(
            file=data.file,
            purpose=self.file_purpose_formatter(data.purpose)
        )

        openai.beta.assistants.files.create(
            assistant_id=file.assistant_id
        )

        return file

    async def delete_files(self, data):
        delete_file = await openai.File.delete({"file_id": data.file_id})

        openai.beta.assistants.files.delete(
            file_id=data.file_id
        )

    async def get_files(self, data):
        get_file = await openai.File.get({"file_id": data.file_id})

        openai.beta.assistants.files.retrieve(
            file_id=data.file_id
        )

    async def execute(self, data):

        if data.action == "create":
            file = await self.create_file(data)
        elif data.action == "create":
            deleted_file = await self.create_file(data)

        logger.info("Request and response json", extra={"payload": data.dict(), "file": data.file.name})

        return {"output": file.id}
