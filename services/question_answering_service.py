import openai
from services import AIService
from builders.question_answering_prompt_builder import QuestionAnsweringPromptBuilder
from config.logging_config import logger
from config.global_config import config


class QuestionAnsweringService(AIService):
    def __init__(self):
        self.model_config = config["model_config"]

    async def execute(self, data):
        # Build prompt
        builder = QuestionAnsweringPromptBuilder()
        prompt = (
            builder
            .add_preset(data.preset)
            .build()
        )

        # Actual logic or API calls for translation
        completion = await openai.ChatCompletion.acreate(model=self.model_config["model_name"],
                                                         temperature=data.temperature,
                                                         max_tokens=data.max_tokens,
                                                         presence_penalty=self.model_config["presence_penalty"],
                                                         stop=self.model_config["stop_sequences"],
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
