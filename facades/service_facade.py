from factories.service_factory import ServiceFactory
from models import TranslateModel, IllustrateModel
from typing import Union


# Facade to simplify interaction and encapsulate the AI services
class ServiceFacade:
    def __init__(self):
        self.factory = ServiceFactory()

    async def perform_task(self, request_data: Union[TranslateModel, IllustrateModel]):
        """

        :param request_data:
        :return:
        """
        service = self.factory.create_service(request_data.task)
        if service:
            return await service.execute(request_data.data)
        else:
            return {"error": "Invalid service type"}
