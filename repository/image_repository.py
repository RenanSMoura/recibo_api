from abc import ABC, abstractmethod


class ImageRepository(ABC):

    @abstractmethod
    def generateSubjectTicket(self, description: str, user_file_name: str, payment_day: str):
        """abstractmethod"""

        raise Exception("Not Implemented")
