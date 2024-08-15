"""Factories following the factory design pattern"""
from services.illustration_service import IllustrationService
from services.translation_service import TranslationService
from services.content_moderation_service import ContentModerationService
from services.question_answering_service import QuestionAnsweringService
from services.speech_to_text_service import SpeechToTextService
from services.content_generation_service import ContentGenerationService
from services.file_service import FileService


# Factory to create instances of different AI services
class ServiceFactory:
    def create_service(self, type):
        if type == "TRANSLATION":
            return TranslationService()
        elif type == "ILLUSTRATION":
            return IllustrationService()
        elif type == "ASSISTANT":
            return IllustrationService()
        elif type == "FILE":
            return FileService()
        elif type == "Q&A":
            return QuestionAnsweringService()
        elif type == "content_moderation":
            return ContentModerationService()
        elif type == "content_generation":
            return ContentGenerationService()
        else:
            return None
