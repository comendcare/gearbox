from factories.service_factory import ServiceFactory


# Facade to simplify interaction and encapsulate the AI services
class ServiceFacade:
    def __init__(self):
        self.factory = ServiceFactory()

    def perform_task(self, type, data):
        """

        :param type:
        :param data:
        :return:
        """
        service = self.factory.create_service(type)
        if service:
            return service.execute(data)
        else:
            return {"error": "Invalid service type"}
