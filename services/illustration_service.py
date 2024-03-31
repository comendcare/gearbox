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


class IllustrationService(AIService):
    def __init__(self):
        self.model_config = config["model_config"]

    def image_size_to_resolution(self, image_size):
        size_dict = {
            "SQUARE": "1024x1024",
            "HORIZONTAL": "1792x1024",
            "VERTICAL": "1024x1792"
        }
        return size_dict[image_size]

    async def execute(self, data):
        builder = IllustrationPromptBuilder()
        prompt = (
            builder
            .add_style(data.style)
            .build()
        )

        prompt = prompt + " Your prompt is: " + data.prompt

        # Actual logic or API calls for illustrations
        illustrations = await openai.Image.acreate(
            model=data.model_name,
            quality="hd" if data.model_name == "dall-e-3" else "standard",
            prompt=prompt,
            n=data.num_illustrations,
            size=self.image_size_to_resolution(data.image_size)
        )
        output = illustrations.data
        logger.info("Request and response json", extra={"payload": data.dict(), "prompt": prompt, "output": output})

        return {"output": illustrations}
