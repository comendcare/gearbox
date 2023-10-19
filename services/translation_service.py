import os
import openai
from services import AIService
from dotenv import load_dotenv
from builders.prompt_builder import PromptBuilder
from config.logging_config import logger
from config.global_config import config
load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()


class TranslationService(AIService):
    def __init__(self):
        self.model_config = config["model_config"]

    def execute(self, data):
        # Build prompt
        builder = PromptBuilder()
        prompt = (
            builder
            .add_audience(data.audience)
            .add_preset(data.preset)
            .add_readability_score(data.readability)
            .add_tone(data.tone)
            .build()
        )

        # Actual logic or API calls for translation
        completion = openai.ChatCompletion.create(model=self.model_config["model_name"],
                                                  temperature=data.temperature,
                                                  max_tokens=data.max_tokens,
                                                  presence_penalty=1,
                                                  messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": data.user_text
            }
        ])
        output = completion.choices[0].message.content
        logger.info("Request and response json", extra={"payload": data.dict(), "prompt": prompt, "output": output})

        return {"output": output}
