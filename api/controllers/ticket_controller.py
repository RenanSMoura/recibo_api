from ..gen.doc.ticket_implementation import TickedPDFImpl
from ..gen.model.Ticket import Ticket
from ..gen.model.User import User
from ..gen.text.text_implementation import TicketTextGeneratorImpl

import traceback

def generate_ticket(user: User):
    try:
        txt_gen = TicketTextGeneratorImpl(user)
        ticket = Ticket(
            final_text=txt_gen.createTicketDescription(),
            user=user
        )
        data = TickedPDFImpl(ticket).generate_ticket()

        return data
    except Exception:
        print(f"Exception{traceback.print_exc()}")
