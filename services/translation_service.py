import os
import openai
from services import AIService
from dotenv import load_dotenv
from builders.prompt_builder import PromptBuilder
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
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
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
        print(completion.choices[0].message.content)
        return {"translated_text": "translated_data_here"}
