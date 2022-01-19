from abc import ABC, abstractmethod

from model.User import User


class TextGeneratorRepository(ABC):

    @abstractmethod
    def createTicketDescription(self):
        """abstractmethod"""

        raise Exception("Not Implemented")
