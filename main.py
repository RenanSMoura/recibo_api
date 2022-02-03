# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from app.gen.doc.ticket_implementation import TickedPDFImpl
from app.gen.model.Session import Session
from app.gen.model.Ticket import Ticket
from app.gen.model.User import User
from app.gen.text.text_implementation import TicketTextGeneratorImpl


def print_hi(name):
    # Ok

    # subject_list = [gabriela, leandro, bianca, mayara, barbara, pamela_dezembro, pamela_janeiro]
    # subject_list = [ana_paula]
    #
    # clss = TextGenerationRepositoryImplementation()
    # image_generator = ImageGenerationRepositoryImplementation()
    #
    # for user in subject_list:
    #     final_text = clss.createTicketDescription(user)
    #     image_generator.generateSubjectTicket(
    #         description=final_text,
    #         user_file_name=get_file_name(user.name.lower()),
    #         paymentDate=user.payment_day
    #     )
    test()


def test():
    bruna = User(
        user_title="Sra",
        user_name="Bruna Bigal de Queiroz",
        user_email="1892182",
        payment_day="31/01/2022",
        session=Session(
            price="180",
            days=["06/01", "13/01", "20/01", "27/01"]
        )
    )

    barbara = User(
        user_title="Sra",
        user_name="Barbara Alves de Sousa",
        payment_day="31/01/2022",
        session=Session(
            price="135",
            days=["12/01", "26/01"]
        )
    )

    mayara = User(
        user_title="Sra",
        user_name="Mayara Culler dos Santos",
        payment_day="15/01/2022",
        session=Session(
            price="150",
            days=["19/01", "26/01"]
        )
    )

    bianca = User(
        user_title="Sra",
        user_name="Bianca Pedrina Manoel",
        payment_day="24/01",
        session=Session(
            price="140",
            days=["17/01", "24/01", "31/01"]
        )
    )
    leandro = User(
        user_title="Sr",
        user_name="Leandro dos Santos",
        payment_day="02/01/2022",
        session=Session(
            price="160",
            days=["05/01", "12/01", "19/01", "26/01"]
        )
    )
    gabriela = User(
        user_title="Sra",
        user_name="Gabriella Miraglia Egydio",
        payment_day="30/01/2022",
        session=Session(
            price="180",
            days=["5/01", "12/01", "19/01", "26/01"]
        )
    )

    ana = User(
        user_title="Sra",
        user_name="Ana Paula Munhoz",
        payment_day="10/01/2022",
        session=Session(
            price="125",
            days=["03/01", "09/01", "16/01", "22/01"]
        )
    )
    nathan = User(
        user_title="Sr",
        user_name="Nathan Felipe Caetano da Silva",
        payment_day="25/01/2022",
        session=Session(
            price="100",
            days=["6/01", "13/01", "20/01", "27/01"]
        )
    )
    users = [bruna, barbara, mayara, bianca, leandro, ana, nathan, gabriela]

    for i in users:
        txtGen = TicketTextGeneratorImpl(i)
        ticket = Ticket(
            final_text=txtGen.createTicketDescription(),
            user=i,
        )
        TickedPDFImpl(ticket).generate_ticket()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi("11")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
