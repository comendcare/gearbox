import os
import openai
from services import AIService
from dotenv import load_dotenv
from builders.translation_prompt_builder import TranslationPromptBuilder
from config.logging_config import logger
from config.global_config import config
load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()


class AssistantService(AIService):
    def __init__(self):
        self.model_config = config["model_config"]

    async def execute(self, data):
        # Build prompt
        builder = TranslationPromptBuilder()
        prompt = (
            builder
            .add_audience(data.audience)
            .add_preset(data.preset)
            .add_readability_score(data.readability)
            .add_tone(data.tone)
            .build()
        )

        messages = [
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": data.user_text
            }
        ]

        assistant = openai.beta.assistants.acreate(
            instructions="You are a highly skilled AI trained in language comprehension and simplification. Do not use first person. Remember the key here is to simplify, not necessarily summarize.",
            model="gpt-4-turbo-preview",
            tools=[{"type": "retrieval"}],
            file_ids=data.file_ids
        )

        thread = openai.beta.threads.create_and_run_stream(
            messages=[
                {
                    "role": "user",
                    "content": data.user_text,
                }
            ]
        )

        # message = openai.beta.threads.messages.acreate(
        #     thread_id=thread.id, role="user", content=data.user_text
        # )

        messages = openai.beta.threads.messages.list(thread_id=thread.id)
        last_message = messages.data[0]
        response = last_message.content[0].text.valu
        print(response)
        logger.info("Request and response json", extra={"payload": data.dict(), "prompt": messages, "output": response})

        return {"output": output}
