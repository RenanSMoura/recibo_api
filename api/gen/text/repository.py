from abc import ABC, abstractmethod

class TextGeneratorRepository(ABC):

    @abstractmethod
    def createTicketDescription(self):
        """abstractmethod"""

        raise Exception("Not Implemented")
