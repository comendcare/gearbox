import os
import openai
from services import AIService
from dotenv import load_dotenv
from builders.prompt_builder import PromptBuilder
from config.logging_config import logger
load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()


class TranslationService(AIService):
    def execute(self, data):
        # Build prompt
        builder = PromptBuilder()
        prompt = (
            builder
            .add_preset(data.preset)
            .add_readability_score(data.readability)
            .add_tone(data.tone)
            .build()
        )

        # Actual logic or API calls for translation
        completion = openai.ChatCompletion.create(model="ft:gpt-3.5-turbo-0613:personal::888oh06D",
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
        logger.info("Request and response json", extra={"payload": data.dict(), "output": output})

        return {"output": output}
