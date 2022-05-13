from abc import ABC, abstractmethod


class TicketPDFRepository(ABC):

    @abstractmethod
    def generate_ticket(self):
        """abstractmethod"""

        raise Exception("Not Implemented")